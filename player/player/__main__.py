from time import sleep
from ydl import ydl
from requests import get
from bottle import Bottle, run
from player import stream

app = Bottle()

def playloop():
    next_song = get("https://127.0.0.1/api/next", verify=False)
    if "Next" in next_song.json():
        ydl.download([next_song.json()["Next"]])
    else:
        print("no songs! - Waiting 1 min")
        sleep(60)
    return playloop()

@app.route("/restart")
def restart():
    stream(None)

if __name__ == "__main__":
    playloop()
