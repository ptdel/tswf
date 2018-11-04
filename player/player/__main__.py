from flask import Flask
from config import Settings
from bp.muu import muu
from bp.error_handlers import error_handlers

app = Flask(__name__)
app.config.from_object(Settings)
app.register_blueprint(error_handlers)
app.register_blueprint(muu)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
