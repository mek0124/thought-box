from typing import Tuple, Union

from ..models.user import User
from ..models.entry import Entry


class ThoughtBoxLogic:
    def __init__(self, db):
        self.db = db

    def get_user_data(self) -> Tuple[bool, Union[User, str]]:
        pass