from queue import playlist

class VoteToSkip(list):
    def __init__(self):
        self.currentsong = playlist.current()
        
    def __call__(self, username):
        if playlist.current() != self.currentsong:
            self.currentsong = playlist.current()
            self.clear()
        if username is not None:
            for x in self:
                if x == username:
                    return "vote already cast"
            self.append(username)
            print (username)
            print (self.currentsong)
            
votetoskip = VoteToSkip()