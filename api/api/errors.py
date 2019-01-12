from werkzeug.exceptions import HTTPException


class InternalError(HTTPException):
    """
    Just a basic internal server error (500) to throw for now.  We can add
    more error classes later and re-use this __init__ format.

    """

    def __init__(self, description=None, response=None):
        super().__init__(description=description, response=response)
        self.msg = self.__class__.__name__
        self.code = 500

class BadRequest(HTTPException):
    
    def __init__(self, description=None, response=None):
        super().__init__(description=description, response=response)
        self.msg = self.__class__.__name__
        self.code = 400
        
class Unauthorized(HTTPException):

    def __init__(self, description=None, response=None):
        super().__init__(description=description, response=response)
        self.msg = self.__class__.__name__
        self.code = 403
        
class MethodNotAllowed(HTTPException):
    """
    Using for queue being empty but someone trying to effect it
    like voting to skip on an empty queue
    """
    
    def __init__(self, description=None, response=None):
        super().__init__(description=description, response=response)
        self.msg = self.__class__.__name__
        self.code = 405