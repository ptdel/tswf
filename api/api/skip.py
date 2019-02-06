from requests import get
from errors import Unauthorized, MethodNotAllowed

class Skip(list):
    
    status = False
    votecount = 0

    def __init__(self):
        self.status == False
        self.votecount = 0
        
    def __call__(self, username):
        if username is not None:
            for x in self:
                if x == username:
                    raise Unauthorized
            self.append(username)
            self.votecount += 1
            
            if self.votecount >= 4:
                get("https://127.0.0.1:8081/restart", verify=False)
                
    def reset(self):
        self.status = False
        self.votecount = 0
        self.clear()
            
votetoskip = Skip()