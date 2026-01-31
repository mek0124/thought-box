from PySide6.QtWidgets import QApplication
from pathlib import Path

from app.app import ThoughtBox

import sys


def run():
    app = QApplication(sys.argv)

    root_dir = Path(__file__).parent
    storage_dir = root_dir / "app" / "storage"
    storage_dir.mkdir(parents=True, exist_ok=True)

    window = ThoughtBox()
    window.setWindowTitle("Thought Box")
    window.setMinimumWidth(1200)
    window.setMinimumHeight(800)
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    run()