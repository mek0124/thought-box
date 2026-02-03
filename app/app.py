from qfluentwidgets import (
    MSFluentWindow, FluentIcon as fi,
    setTheme, Theme, setThemeColor
)

from .pages.dashboard import Dashboard


class ThoughtBox(MSFluentWindow):
    def __init__(self, color_theme, db):
        super().__init__()

        self.color_theme = color_theme
        self.db = db

        self.dashboard = Dashboard(self)

        self.apply_app_styles()
        self.init_navigation()

    def apply_app_styles(self):
        setTheme(Theme.DARK)
        setThemeColor(self.color_theme['primary'])
        self.setStyleSheet(f"background-color: {self.color_theme['background']}")

    def init_navigation(self):
        self.addSubInterface(self.dashboard, fi.APPLICATION, "Dashboard")
