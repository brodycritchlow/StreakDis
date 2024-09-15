class UserNotFound(Exception):
    """
    Raised when trying to access a user that does not exist.
    """

    pass

class UserAlreadyExists(Exception):
    """
    Raised when trying to create a user that already exists.
    """
    
    pass

