from PySide6.QtWidgets import (
    QWidget, QVBoxLayout
)

from PySide6.QtCore import Qt


class Profile(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Profile")

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignCenter)