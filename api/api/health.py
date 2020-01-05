from flask import jsonify

def health():
    return jsonify({"status_code": 200})
