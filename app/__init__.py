from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "Hello, World!"

    return app

# This `app` will be imported by `main.py` or by the Flask CLI.
app = create_app()
