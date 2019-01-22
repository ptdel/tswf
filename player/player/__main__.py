from time import sleep
from ydl import ydl
from bottle import Bottle, run, request, get
from player import stream_song

app = Bottle()

@app.route("/restart")
def restart():
    playloop()
    return "200"
    
@app.route("/play")
def play():
    song = request.query.song
    
    if song != None:
        ydl.download([song])
        return "200"
    else:
        return "No Songs"

#def playloop():
#    next_song = get("https://127.0.0.1/api/next", verify=False)
#    if "Next" in next_song.json():
#        ydl.download([next_song.json()["Next"]])
#    else:
#        print("no songs! - Waiting 1 min")
#        sleep(60)
#    return playloop()


if __name__ == "__main__":
    run(app, host="localhost", port=8070, debug=True)
