from pathlib import Path
import json
class ConfigLoader:
    def __init__(self):
        self.config_file = Path("config.json")
        try:
            self.config = self.load_config()

        except Exception as e:

            print(
                f"Config Initialization Error: {e}"
            )

            self.config = {}

    def load_config(self):
        try:
            if not self.config_file.exists():
                raise FileNotFoundError(
                    "Config.json not found"
                )  
            
            with open(self.config_file,'r',encoding='utf-8') as file:
                    return json.load(file)
            
        except FileNotFoundError as e:

            print(
                f"Config Error: {e}"
            )

            raise

        except json.JSONDecodeError as e:

            print(
                f"Invalid JSON Format: {e}"
            )

            raise

        except PermissionError:

            print(
                "Permission denied while "
                "reading config.json"
            )

            raise

        except OSError as e:

            print(
                f"File System Error: {e}"
            )

            raise

    def get(self,key,default=None):
        return self.config.get(
            key,
            default
        )
        