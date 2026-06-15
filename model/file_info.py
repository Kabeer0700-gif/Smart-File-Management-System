from datetime import datetime
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

    def time_ago(self, timestamp):

        difference = datetime.now() - timestamp

        seconds = difference.total_seconds()

        if seconds < 60:
            return f"{int(seconds)} seconds ago"

        elif seconds < 3600:
            return f"{int(seconds//60)} minutes ago"

        elif seconds < 86400:
            return f"{int(seconds//3600)} hours ago"

        elif seconds < 2592000:
            return f"{difference.days} days ago"

        else:
            return timestamp.strftime("%Y-%m-%d")

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Extension: {self.extension}\n"
            f"Size: {self.size} bytes\n"
            f"Path: {self.path}\n"
            f"Created: {self.time_ago(self.created_date)}\n"
            f"Modified: {self.time_ago(self.modified_date)}\n"
        )

    def __repr__(self):
        return (
            f"FileInfo("
            f"name='{self.name}', "
            f"extension='{self.extension}', "
            f"size={self.size}, "
            f"path='{self.path}')"
        )  
       
        