from qfluentwidgets import (
    MSFluentWindow, setTheme, Theme,
    setThemeColor, FluentIcon, NavigationItemPosition
)

from .core.logic import ThoughtBoxLogic
from .models.user import User
from .models.entry import Entry
from .pages.dashboard import Dashboard
from .pages.profile import Profile


class ThoughtBox(MSFluentWindow):
    def __init__(self, db, color_theme):
        super().__init__()

        self.db = db
        self.color_theme = color_theme
        
        self.logic = ThoughtBoxLogic(self.db)

        self.user = self.logic.get_user_data()

        self.dashboard = Dashboard(self)
        self.profile = Profile(self)

        self.set_app_theme()
        self.init_navigation()

    def set_app_theme(self):
        setTheme(Theme.DARK)
        setThemeColor(self.color_theme['primary'])

        self.setStyleSheet(
            f"background-color: {self.color_theme['background']};"
        )

    def init_navigation(self):
        # self.addSubInterface(self.dashboard, FluentIcon.HOME, "Dashboard")
        self.addSubInterface(self.profile, FluentIcon.PEOPLE, "Profile", position=NavigationItemPosition.BOTTOM)

    def closeEvent(self, event):
        event.accept()