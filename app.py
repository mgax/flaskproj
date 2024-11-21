import flask

def create_app():
    app = flask.Flask(__name__)

    @app.route("/")
    def home():
        return("Hello from flaskproj!")

    return app
