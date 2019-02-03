from time import sleep
from ydl import ydl
from requests import get
from player import stream

def playloop():
    
    if stream.process == None:
        next_song = get("https://127.0.0.1/api/next", verify=False)
        if "Next" in next_song.json():
            ydl.download([next_song.json()["Next"]])
        else:
            print ("no songs")
    
    skip = get("https://127.0.0.1/api/skip", verify=False)
    if skip.json()["Skip"] == True and process != None:
        stream.process.terminate()

    sleep(5)
    
    return playloop()

if __name__ == "__main__":
    playloop()