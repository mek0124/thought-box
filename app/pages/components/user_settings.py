from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton
)

from PySide6.QtCore import Qt


class UserSettings(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.user = parent.user
        self.color_theme = parent.color_theme

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        title = QLabel("Settings")
        title.setObjectName("title")
        
        details_container = QWidget()