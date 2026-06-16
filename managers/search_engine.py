class SearchEngine:
    def search_by_name(self,files,keyword):
        result = []
        for file in files:
            if keyword.lower() in file.name.lower():
                result.append(file)


        return result
    

    def search_by_extension(self,files,ext):
        result = []
        for file in files:
            if file.extension.lower() == ext.lower():
                result.append(file)

        return result
    
    def search_by_size(self, files, min_size, max_size):
        result = []
        for file in files:
            if   min_size <= file.size <= max_size:
                result.append(file)

        return result
    