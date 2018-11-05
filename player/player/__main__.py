from time import sleep
from ydl import ydl
from requests import get

def playloop():
    next_song = get("https://127.0.0.1/api/next", verify=False)
    if 'Next' in next_song.json():
        ydl.download([next_song.json()['Next']])
    else:
        print('no songs! - Waiting 1 min')
        sleep(60)
    return playloop()

if __name__ == '__main__':
    playloop()
