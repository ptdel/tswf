from collections import deque

class PlayList(deque):
    def __init__(self, maxlen = None):
        super().__init__(maxlen = maxlen)

    def __call__(self, song=None):
        if song is not None:
            self.appendleft(song)

playlist = PlayList()
