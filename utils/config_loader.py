from pathlib import Path
import json
class ConfigLoader:
    def __init__(self):
        self.config_file = Path("config.json")
        self.config = self.load_config()

    def load_config(self):
        if not self.config_file.exists():
            raise FileNotFoundError(
                "Config.json not found"
            )
        
        with open(self.config_file,'r',encoding='utf-8') as file:
                return json.load(file)
        
    def get(self, key):
        return self.config.get(key)