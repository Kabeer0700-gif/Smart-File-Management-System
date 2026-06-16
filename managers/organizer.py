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

        folder = Path(base_path) / category
        folder.mkdir(exist_ok=True)
        return folder
    

    def move_file(self,source,destination):
        shutil.move(str(source),str(destination))

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
    

