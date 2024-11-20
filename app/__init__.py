from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////app/db/site.db'  # Note the four slashes (////) for an absolute path

    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a real secret key for production
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)  # Session lasts for 30 minutes


    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app
