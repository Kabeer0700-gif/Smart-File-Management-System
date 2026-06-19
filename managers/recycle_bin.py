from pathlib import Path
import shutil
import json
class RecycleBinManager:
    def __init__(self):
        try:
            self.recycle_bin = Path('recycle_bin')
            self.recycle_bin.mkdir(exist_ok=True)

            self.metadata_file = Path('recycle_bin_metadata.json')

            if not self.metadata_file.exists():

                self.metadata_file.write_text(
                    "{}"
                )
        except Exception as e:
            print(
                f"Recycle Bin Initialization Error: {e}"
            )

    def move_to_recycle_bin(self, file):
        try:
            source = Path(file.path)

            destination = (
                self.recycle_bin /
                source.name
            )

            shutil.move(
                str(source),
                str(destination)
            )

            metadata = json.loads(
                self.metadata_file.read_text()
            )

            metadata[source.name] = str(source)

            self.metadata_file.write_text(
                json.dumps(
                    metadata,
                    indent=4
                )
            )
        except FileNotFoundError as e:

            print(
                f"Move Error: {e}"
            )

        except PermissionError:

            print(
                "Permission denied while "
                "moving file."
            )

        except json.JSONDecodeError:

            print(
                "Metadata file contains "
                "invalid JSON."
            )

        except Exception as e:

            print(
                f"Unexpected Error: {e}"
            )

    def restore_file(self,filename):
        try:
            metadata = json.loads(
                self.metadata_file.read_text()
            )

            if filename not in metadata:

                print(
                    "File not found"
                )

                return

            original_path = Path(
                metadata[filename]
            )

            source = (
                self.recycle_bin /
                filename
            )

            original_path.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            shutil.move(
                str(source),
                str(original_path)
            )

            del metadata[filename]

            self.metadata_file.write_text(
                json.dumps(
                    metadata,
                    indent=4
                )
            )

            print(
                f"Restored: {filename}"
            )
        
        except FileNotFoundError as e:

            print(
                f"Move Error: {e}"
            )

        except PermissionError:

            print(
                "Permission denied while "
                "moving file."
            )

        except json.JSONDecodeError:

            print(
                "Metadata file contains "
                "invalid JSON."
            )

        except Exception as e:

            print(
                f"Unexpected Error: {e}"
            )

    def delete_permanently(self,filename):

        file_path = (
            self.recycle_bin /
            filename
        )

        if file_path.exists():

            file_path.unlink()

            print(
                f"Deleted: {filename}"
            )    

    def list_files(self):
        return list(self.recycle_bin.iterdir())