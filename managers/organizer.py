from pathlib import Path
import shutil

class Organizer:
    categories = {
        "Documents" : [".pdf",".cct",".txt",".docx",".ppt"],
        "Images" : [".jpg",".jpeg",".png",".gif"],
        "Videos" : [".mp4",".mkv",".avi"],
        "Audio" : [".mp3",".wav"]
    }

    def get_category(self,extension):
        for category,extensions in self.categories.items():
            if extension.lower() in extensions:
                return category
            
        return "Others"
    

    def create_category_folder(self,base_path,category):
        try:
            folder = Path(base_path) / category
            folder.mkdir(exist_ok=True)
            return folder
        
        except PermissionError:
            print(
                f"Permission denied while creating "
                f"folder '{category}'"
            )

        except Exception as e:
            print(
                f"Folder creation error: {e}"
            )

        return None
    

    def move_file(self,source,destination):
        try:
            shutil.move(str(source),str(destination))
            
        except FileNotFoundError:
            print(
                f"File not found: {source}"
            )

        except PermissionError:
            print(
                f"Permission denied: {source}"
            )

        except shutil.Error as e:
            print(
                f"Move error: {e}"
            )

        except Exception as e:
            print(
                f"Unexpected error: {e}"
            )

    def organize_file(self,files):
        for file in files:
            category = self.get_category(file.extension)
            source = Path(file.path)
            folder = self.create_category_folder(source.parent,category)

            destination = (folder / category)

            self.move_file(source,destination)

            print(
                    f"Moved: {source.name} ---> {destination.name}"
                )
    

