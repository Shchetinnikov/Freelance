import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['PORT'] = config.FLASK_APP_PORT
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/freelance_api"

db = SQLAlchemy(app)

from views import *

if __name__ == "__main__":
    from schemas import init_db

    with app.app_context():
        init_db()

    app.run()
