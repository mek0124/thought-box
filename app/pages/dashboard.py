from PySide6.QtWidgets import (
    QWidget, QVBoxLayout
)

from ..models.entry import EntryModel


class Dashboard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Dashboard")

        self.db = parent.db

        self.all_entries = self.db.query(EntryModel).all()

        self.setup_ui()

    def setup_ui(self):
        if self.layout() is None:
            layout = QVBoxLayout(self)

        else:
            layout = self.layout()

            while layout.count():
                item = layout.takeAt(0)

                if item.widget():
                    item.widget().deleteLater()

        