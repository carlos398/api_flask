from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from .configs import DATABASE_CONECTION_URI, JWT_SECRET_KEY, SECRET_KEY

# Blueprints - routes
from .routes.users_routes import users_routes


app = Flask(__name__)

app.secret_key = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Config jwt
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY  # Change this!

JWTManager(app)
SQLAlchemy(app)
CORS(app)

app.register_blueprint(users_routes, url_prefix='/api')