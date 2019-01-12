from queue import playlist
from errors import Unauthorized, MethodNotAllowed

class Skip(list):
    def __init__(self):
        self.currentsong = playlist.current()
        self.votecount = 0
        
    def __call__(self, username):
        if self.currentsong != playlist.current():
            self.currentsong = playlist.current()
            self.clear()
            
        if username is not None:
            for x in self:
                if x == username:
                    raise Unauthorized
            self.append(username)
            self.votecount += 1
            
            if self.votecount >= 4:
                playlist.pop()
                self.votecount = 0
                self.clear()
            
votetoskip = Skip()