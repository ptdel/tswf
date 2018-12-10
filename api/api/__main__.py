from flask import Flask
from config import Settings
from bp.api import api
from bp.error_handlers import error_handlers

app = Flask(__name__)

app.config.from_object(Settings)

app.register_blueprint(error_handlers)
app.register_blueprint(api)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
