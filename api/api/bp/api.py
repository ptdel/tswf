"""
API
---

This blueprint provides routes for the song queue
utilized by the player container.

"""
from flask import Blueprint, jsonify, request, g
from queue import playlist
from errors import InternalError

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


@api.teardown_app_request
def app_request_teardown(error=None):
    if error is not None:
        print([str(_) for _ in error.args])
