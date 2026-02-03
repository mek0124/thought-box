from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout
)

from ..models.entry import Entry


class Dashboard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Dashboard")