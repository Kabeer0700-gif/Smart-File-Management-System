from utils.hash_generator import HashGenerator
from pathlib import Path
from managers.recycle_bin import RecycleBinManager
class duplicateFinder:

    def __init__(self):
        self.recycle_bin = RecycleBinManager()

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
    

    def display_duplicates(self,duplicates):
        print("Displaying duplicates")
        for file_hash,file_list in duplicates.items():
            print("Duplicate Group")
            for file in file_list:
                print(file)

            print("")


    def remove_duplicate(self,duplicates):
        for file_list in duplicates.values():
            if len(file_list) < 2:
                continue
            original = file_list[0]
            print(f"\nKeeping Original: {original.path}")
            for duplicate in file_list[1:]:
                self.recycle_bin.move_to_recycle_bin(duplicate)
                print("Deleted: ",duplicate.path)

    

    

