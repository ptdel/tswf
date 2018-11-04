from flask import Blueprint, jsonify
from werkzeug.exceptions import HTTPException

error_handlers = Blueprint('error_handlers', __name__)

@error_handlers.app_errorhandler(HTTPException)
def http_error_handler(error):
    return jsonify(dict(error=dict((k, getattr(error, k))
        for k in dir(error)
        if not callable(getattr(error, k))
        and not k.startswith('__')))), error.code

@error_handlers.app_errorhandler(Exception)
def unexpected_error_handler(error):
    resp = { "code": 500, "description": [ str(_) for _ in error.args ] }
    return jsonify(dict(error=str(resp))), 500
