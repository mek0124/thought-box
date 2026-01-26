from qfluentwidgets import (
    MSFluentWindow, setTheme, Theme,
    setThemeColor, FluentIcon
)

from .pages.dashboard import Dashboard
from .pages.entry import Entry

from .utils.color_theme import COLOR_THEME


class ThoughtBox(MSFluentWindow):
    def __init__(self, db):
        super().__init__()

        self.db = db
        self.dashboard = Dashboard(self)
        self.entry = Entry(self)

        self.set_app_theme()
        self.init_navigation()

    def set_app_theme(self):
        setTheme(Theme.DARK)
        setThemeColor(COLOR_THEME['primary'])

        self.setStyleSheet(
            f"background-color: {COLOR_THEME['background']};"
        )

    def init_navigation(self):
        self.addSubInterface(self.dashboard, FluentIcon.HOME, "Dashboard")
        self.addSubInterface(self.entry, FluentIcon.PENCIL_INK, "Entry")

    def closeEvent(self, event):
        self.db.close()
        event.accept()