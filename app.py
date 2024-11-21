import flask

def create_app():
    app = flask.Flask(__name__)

    app.config["BANNER_TEXT"] = "Hello from flaskproj!"

    @app.route("/")
    def home():
        return f"""
            <h1>{app.config["BANNER_TEXT"]}</h1>
            <p>Welcome to our product!</p>
        """

    return app
