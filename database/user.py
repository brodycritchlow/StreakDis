import os

import discobase
from database import db
from exceptions import UserAlreadyExists, UserNotFound

from .streak import Streak


@db.table
class User(discobase.Table):
    """
    The basic representation of a user in our system, holds data such as:

    - name: The name of the user
    - user_id: The Discord ID of the user
    - streak: The current streak of the user
    """

    name: str
    user_id: int


class UserManager():
    def __init__(self):
        self.db = db

    async def get_user(self, user_id: int) -> User:
        """
        Get a user from the database.

        :param user_id: The Discord ID of the user
        :return: The user

        :raises UserNotFound: If a user with the given ID does not exist
        """
        print("test")
        return await self.db.tables[User.__name__.lower()].find(user_id=user_id) or "user not found" # self._raise_user_not_found(user_id)

    async def create_user(self, user_id: int, name: str) -> User:
        """
        Create a new user in the database.
        
        :param user_id: The Discord ID of the user
        :param name: The name of the user
        :return: The newly created user

        :raises UserAlreadyExists: If a user with the given ID already exists
        """
        print(self.db.tables[User.__name__.lower()])
        existing_user = await self.db.tables[User.__name__.lower()].find(user_id=user_id)
        if existing_user:
            return f"User with ID {user_id} already exists."
        
        user = User(name=name, user_id=user_id).save()
        streak = Streak(user_id=user_id, streak=0, previous_streak=0, expires_at=0, expired_at=0).save()

        return f"Created user successfully! {repr(await self.db.tables[User.__name__.lower()].find(user_id=user_id))}"

    def _raise_user_not_found(self, user_id: int):
        raise UserNotFound(f"User with ID {user_id} not found.")
