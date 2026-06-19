import hashlib

class HashGenerator:

    @staticmethod
    def generate(filepath):
        try:
            sha256 = hashlib.sha256()

            with open(filepath, "rb") as file:

                while chunk := file.read(4096):

                    sha256.update(chunk)
        except Exception as e:
            print(
                f"Error Occured as {e}"
            )

        return sha256.hexdigest()