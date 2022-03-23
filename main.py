from src.app import app
from src.utils.db import db
import src.configs

HOST = "localhost"
PORT = 4000
DEBUG = True

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(HOST, PORT, DEBUG)
