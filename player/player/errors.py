from werkzeug.exceptions import HTTPException

class InternalError(HTTPException):
    """
    Just a basic internal server error (500) to throw for now.  We can add
    more error classes later and re-use this __init__ format.

    """
    def __init__(self, description = None, response = none):
        super().__init__(description = description, response = response)
        self.msg = self.__class__.__name__
        self.code = 500
