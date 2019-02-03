"""
API
---

This blueprint provides routes for the song queue
utilized by the player container.

"""

from flask import Blueprint, jsonify, request
from requests import get
from music_queue import playlist
from errors import InternalError, BadRequest, MethodNotAllowed
from skip import votetoskip

api = Blueprint("api", __name__, url_prefix="/api")

@api.route("/submit")
def submit():
    """
    provides a route to submit song reqeusts

    """
    if not "song" in request.args:
        raise InternalError
    song = request.args.get("song")
    playlist(song)
    return jsonify({"Added": song})

@api.route("/next")
def up_next():
    """
    provide a route to pop next song from queue.

    """
    playlist.current_song = playlist[0]
    votetoskip.reset()
    return jsonify({"Next": playlist.pop()})

@api.route("/stat")
def stat():
    """
    provides information about the song queue

    """
    return jsonify({"QueueLen": len(playlist)})


@api.route("/queue")
def queue():
    """
    provides the song queue as a dictionary

    """
    return jsonify(list(playlist))


@api.route("/clear")
def clear():
    """
    provides a route to clear the queue

    """
    playlist.clear()
    return jsonify({"Cleared": "playlist"})

@api.route('/np')
def np():
    """
    provides the currently playing song
    
    """
    return jsonify({"Current": playlist.current_song})
    
@api.route("/skip")
def skip():
    """
    votes by users to skip currently playing song
    
    """   
    if not 'username' in request.args:
        return jsonify({"Skip": votetoskip.status})
    if len(playlist) == 0:
        raise MethodNotAllowed
        
    votetoskip(request.args.get('username'))
    return jsonify({"Skip": "200"})

@api.teardown_app_request
def app_request_teardown(error=None):
    if error is not None:
        print([str(_) for _ in error.args])
