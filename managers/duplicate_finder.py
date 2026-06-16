from utils.hash_generator import HashGenerator

class duplicateFinder:

    def find_duplicate(self,files):

        hashmap = {}
        duplicates = {}

        for file in files:
            file_hash = HashGenerator.generate(file.path)

            if file_hash in hashmap:
                duplicates.setdefault(file_hash,[]).append(file)
            else:
                hashmap[file_hash] = file

        return duplicates
    

    