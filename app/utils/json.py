from pathlib import Path
import json

class JsonEngine:
    def __init__(self, storage_dir: Path):
        self.storage_dir = storage_dir
    
    def update_config_file(self) -> bool:
        config_path = self.storage_dir / "config.json"
        config_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            if not config_path.exists():
                data = {"read_write_perm": 1}
            else:
                with open(config_path, 'r', encoding="utf-8-sig") as curr_agree:
                    data = json.load(curr_agree)
                data["read_write_perm"] = 1
            
            with open(config_path, 'w', encoding="utf-8-sig") as updated_agree:
                json.dump(data, updated_agree, indent=2)
            return True
        
        except Exception as e:
            print(f"Unknown Exception: {e}")
            return False

    def read_config(self):
        config_path = self.storage_dir / "config.json"
        try:
            if not config_path.exists():
                return None
            with open(config_path, 'r', encoding="utf-8-sig") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return None
        except Exception as e:
            print(f"Unknown Exception: {e}")
            return None

    def check_existing_perms(self) -> bool:
        config_path = self.storage_dir / "config.json"
        try:
            if not config_path.exists():
                return False
            
            data = self.read_config()
            if not data:
                return False
            
            rw_perm = data.get("read_write_perm", 0)
            return rw_perm == 1
        except Exception as e:
            print(f"Unknown Exception: {e}")
            return False