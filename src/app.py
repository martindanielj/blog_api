# /src/app.py

from flask import Flask
from src.config import app_config

def create_app(env_name):
    """
    Create app
    """

    # app initialization
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    @app.route('/', methods=['GET'])
    def index():
        """
        example endpoint
        ----------------

        This example differs from the sample documentation because we've
        replaced the standard text return with an HTML return.
        """

        end_html = """
        <html>
        <title>Congratulations!</title>
        <body>Congratulations! Your first endpoint is workin</body>
        </html>
        """
        return end_html

    return app