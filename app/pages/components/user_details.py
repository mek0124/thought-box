from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton
)

from PySide6.QtCore import Qt


class UserDetails(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.user = parent.user
        self.color_theme = parent.color_theme

        self.setup_ui()
        self.apply_style_sheet()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        title = QLabel("Details")
        title.setObjectName("title")
        
        details_container = QWidget()
        details_container.setObjectName("body-container")

        details_conatiner_layout = QVBoxLayout(details_container)
        details_conatiner_layout.setContentsMargins(0, 0, 0, 0)
        details_conatiner_layout.setSpacing(0)
        details_conatiner_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

    def apply_style_sheet(self):
        self.setStyleSheet(
            f"""
                QWidget {{
                    border: none;
                }}

                QLabel#title {{
                    font-weight: bold;
                    font-style: italic;
                    font-size: 14px;
                    color: {self.color_theme['primary']};
                    letter-spacing: 0.2em;
                }}
            """
        )