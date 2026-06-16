import hashlib

class HashGenerator:

    @staticmethod
    def generate(filepath):

        sha256 = hashlib.sha256()

        with open(filepath, "rb") as file:

            while chunk := file.read(4096):

                sha256.update(chunk)

        return sha256.hexdigest()