from time import sleep
import threading
from bottle import Bottle, run
from ydl import ydl
from requests import get
from player import stream

app = Bottle()

@app.route('/restart')
def restart():
    if stream.process != None:
        stream.process.terminate()
    return

def playloop():
    if stream.process == None or stream.process.poll() != None:
        next_song = get("https://127.0.0.1/api/next", verify=False)
        if "Next" in next_song.json():
            ydl.download([next_song.json()["Next"]])
        else:
            print ("no songs")

    sleep(5)
    return playloop()

player = threading.Thread(name='player', target=playloop)
if __name__ == "__main__":
    player.start()
    run(app, host='localhost', port=8081)
    player.join()