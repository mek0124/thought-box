from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtGui import QPixmap
from pathlib import Path

from app.app import ThoughtBox
from app.database.db import get_base, get_engine, get_db
from app.models.entry import Entry
from app.utils.color_theme import COLOR_THEME

import json
import sys


def update_config_file(ua_file: Path) -> bool:
    storage_folder = ua_file.parent
    storage_folder.mkdir(parents=True, exist_ok=True)
    
    try:
        if not ua_file.exists():
            data = {"read_write_perm": 1, "use_browser": 1}

        else:
            with open(ua_file, 'r', encoding="utf-8-sig") as curr_agree:
                data = json.load(curr_agree)
            
            data["read_write_perm"] = 1
            data["use_browser"] = 1
        
        with open(ua_file, 'w', encoding="utf-8-sig") as updated_agree:
            json.dump(data, updated_agree, indent=2)
        
        get_base().metadata.create_all(bind=get_engine())
        return True
    
    except Exception as e:
        print(f"Unknown Exception: {e}")
        return False


def get_read_write_perms() -> bool:
    try:
        rw_agreement = QMessageBox.question(
            None,
            "Read/Write Permissions",
            "This application requires read/write permissions " \
            "to maintain its own database. Do you agree to allow " \
            "this application to have read/write permissions?\n\n**NOTE: " \
            "This application does not read/write to any files outside " \
            "of its own codebase!**",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )

        if rw_agreement == QMessageBox.No or rw_agreement == QMessageBox.Rejected:
            QMessageBox.warning(
                None,
                "Read/Write Permissions - Denied",
                "You denied read/write permissions for this application. " \
                "This application cannot run without these permissions. " \
                "If you change your mind, run the application again."
            )
            return False
                
        return True
    
    except Exception as e:
        print(f"Unknown Exception: {e}")
        return False
    

def get_browser_usage_agreement() -> bool:
    try:
        browser_agree = QMessageBox.question(
            None,
            "Browser Usage Permissions",
            "This application requires permission to use your browser " \
            "to open and display pages like 'About The App' and 'About The " \
            "Developer' and 'Support'. Do you agree to allow this application " \
            "to use your browser only when you click to open these pages?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )

        if browser_agree == QMessageBox.No or browser_agree == QMessageBox.Rejected:
            QMessageBox.warning(
                None,
                "Browser Usage Permissions - Denied",
                "You denied browser usage permissions for this application. " \
                "This application requires browser usage permissions in order to " \
                "properly run and allow you to obtain support when needed. If you change " \
                "your mind, run the application again."
            )
            return False
        
        return True
    
    except Exception as e:
        print(f"Unknown Exception: {e}")
        return False


def get_user_agreement(root_dir: Path) -> bool:
    ua_file = root_dir / "app" / "storage" / "config.json"
    
    rw_agree = get_read_write_perms()
    if not rw_agree:
        return False
    
    browser_agree = get_browser_usage_agreement()
    if not browser_agree:
        return False
    
    did_update = update_config_file(ua_file)
    return did_update


def check_perms(root_dir: Path) -> bool:
    ua_file = root_dir / "app" / "storage" / "config.json"
    
    try:
        if not ua_file.exists():
            return get_user_agreement(root_dir)
        
        with open(ua_file, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)
        
        rw_perm = data.get("read_write_perm", 0)
        browser_perm = data.get("use_browser", 0)
        
        if rw_perm == 0 or browser_perm == 0:
            return get_user_agreement(root_dir)
        
        return True
        
    except json.JSONDecodeError:
        return get_user_agreement(root_dir)
    
    except Exception as e:
        print(f"Unknown Exception: {e}")
        return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    root_dir = Path(__file__).parent
    did_agree = check_perms(root_dir)
    db = next(get_db())
    
    if not did_agree:
        sys.exit(0)
    
    window = ThoughtBox(COLOR_THEME, db)
    window.setWindowIcon(QPixmap("./app/assets/original.png"))
    window.showMaximized()
    
    sys.exit(app.exec())