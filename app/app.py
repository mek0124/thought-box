from qfluentwidgets import (
    MSFluentWindow, setTheme, Theme,
    setThemeColor, FluentIcon, NavigationItemPosition
)

from .pages.dashboard import Dashboard
from .pages.profile import Profile

from .utils.color_theme import COLOR_THEME


class ThoughtBox(MSFluentWindow):
    def __init__(self):
        super().__init__()

        self.dashboard = Dashboard(self)
        self.profile = Profile(self)

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
        self.addSubInterface(self.profile, FluentIcon.PEOPLE, "Profile", position=NavigationItemPosition.BOTTOM)

    def closeEvent(self, event):
        event.accept()