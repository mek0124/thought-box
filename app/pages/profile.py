from PySide6.QtWidgets import QWidget, QHBoxLayout
from PySide6.QtCore import Qt

from .components.user_details import UserDetails
from .components.user_settings import UserSettings


class Profile(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Profile")

        self.user = parent.user
        self.color_theme = parent.color_theme

        self.setStyleSheet("QWidget {{ border: none; }}")

        self.setup_ui()

    def setup_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignCenter)

        layout.addWidget(UserDetails(self))
        layout.addWidget(UserSettings(self))

        layout.addStretch()