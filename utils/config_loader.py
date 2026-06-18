from pathlib import Path
import json
class ConfigLoader:
    def __init__(self):
        self.config_file = Path("config.json")