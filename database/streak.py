from . import db, discobase

@db.table
class Streak(discobase.Table):
    """
    The basic representation of a streak in our system, holds data such as:

    - streak: The current streak of the user
    - previous_streak: The previous streak of the user
    - expires_at: The time at which the streak expires
    - expired_at: The time at which the streak expired
    """

    user_id: int
    streak: int
    previous_streak: int
    expires_at: int
    expired_at: int

