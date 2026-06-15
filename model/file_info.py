class FileInfo:
    def __init__(self,name,extension,size,path,created_date,modified_date):
        self.name = name
        self.extension = extension
        self.size = size
        self.path = path
        self.created_date = created_date
        self.modified_date = modified_date


    def show_detail(self):
        print("Showing file details")
        print(f"Name:{self.name}")
        print(f"Extension:{self.extension}")
        print(f"Size:{self.size}")
        print(f"Path:{self.path}")
        print(f"Created Date:{self.created_date}")
        print(f"Modified Date:{self.modified_date}")


        
       
        