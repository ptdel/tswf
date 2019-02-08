from collections import deque

class PlayList(deque):
    def __init__(self, maxlen=None):
        super().__init__(maxlen=maxlen)
        self.current_song = None

    def __call__(self, song=None):
        if song is not None:
            self.appendleft(song)
            
    def next(self):
        self.current_song = self.pop()
        return self.current_song
            
playlist = PlayList()
