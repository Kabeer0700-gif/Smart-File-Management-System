from pathlib import Path
from model.file_info import FileInfo
from datetime import datetime
class FileManager:
    def scan_directory(self,path):
        files = []
        try:
            directory = Path(path)
            if not directory.exists():
                raise FileNotFoundError(
                    f"Directory '{path}' does not exist."
                )

            if not directory.is_dir():
                raise NotADirectoryError(
                    f"'{path}' is not a directory."
                )
            for item in directory.rglob("*"):
                try:
                    if item.is_file():
                        file_info = self.get_file_metaData(item)
                        files.append(file_info)

                except PermissionError:
                    print(
                        f"Permission denied: {item}"
                    )

                except Exception as e:
                    print(
                        f"Error processing {item}: {e}"
                    )

        except (FileNotFoundError,
                NotADirectoryError) as e:
            print(e)

        except Exception as e:
            print(
                f"Unexpected error: {e}"
            )
        
        return files

    def get_file_metaData(self,file_path):
        stat = file_path.stat()
        created = datetime.fromtimestamp(stat.st_ctime)
        modified = datetime.fromtimestamp(stat.st_mtime)
        return FileInfo(name=file_path.name,
                        extension=file_path.suffix,
                        size=stat.st_size,
                        path=str(file_path.resolve()),
                        created_date=created,
                        modified_date=modified)
    

    def get_total_files(self,files):
        return len(files)
    
    def get_total_size(self,files):
        total = 0

        for s in files:
            total+=s.size

        return total
    

    def filter_by_extension(self,files,extension):
        filter_files = []

        for item in files:
            if item.extension.lower() == extension.lower():
                filter_files.append(item)

        return filter_files
    


