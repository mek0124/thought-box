from PySide6.QtWidgets import QApplication, QMessageBox
from pathlib import Path

from app.app import ThoughtBox

from app.database.db import get_base, get_engine, get_db
from app.models.user import User
from app.models.entry import Entry
from app.utils.json import JsonEngine
from app.utils.color_theme import COLOR_THEME

import sys


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


def get_user_agreement(json_engine: JsonEngine) -> bool:
    rw_agree = get_read_write_perms()
    if not rw_agree:
        return False
    
    did_update = json_engine.update_config_file()
    return did_update


def check_perms(json_engine: JsonEngine) -> bool:
    has_valid_perms = json_engine.check_existing_perms()
    
    if has_valid_perms:
        return True
    
    return get_user_agreement(json_engine)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    root_dir = Path(__file__).parent
    storage_dir = root_dir / "app" / "storage"
    
    json_engine = JsonEngine(storage_dir)
    did_agree = check_perms(json_engine)
    
    if not did_agree:
        sys.exit(0)

    get_base().metadata.create_all(bind=get_engine())
    db = next(get_db())
    
    window = ThoughtBox(COLOR_THEME, db)
    window.show()
    sys.exit(app.exec())