from os import access
from flask import Blueprint
from flask import jsonify
from flask import request
from flask import redirect
from ..models.Users import User
from ..utils.db import db

# Use jwt
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


users_routes = Blueprint("users_routes", __name__)


@users_routes.route("/register", methods=["POST"])
def create_user():
    if request.method == "POST":

        try:
            name = request.json["name"]
            username = request.json["username"]
            password = request.json["password"]
            email = request.json["email"]
            phone = request.json["phone"]

            new_user = User(name, username, password, email, phone)
            db.session.add(new_user)
            db.session.commit()

            return jsonify({"msg": "User create succesfully"}), 201

        except Exception:
            return jsonify({"msg": "User has not create, please verify the data"}), 406

    else:
        return jsonify({"msg": "method not allow"}), 405


@users_routes.route("/login", methods=["POST"])
def login_user():
    if request.method == "POST":

        try:
            email = request.json["email"]
            password = request.json["password"]
            user = User.query.filter_by(email=email).first()

            if user is not None and user._verify_secure_password(password):
                access_token = create_access_token(identity=email)
                return jsonify({"access_token": access_token}), 202

            elif user is not None and user._verify_secure_password(password) == False:
                return jsonify({"msg": "Wrong password please verify"}), 401

            else:
                return jsonify({"msg": "User not found"}), 404

        except:
            return jsonify({"msg": "Something was wrong"}), 400

    else:
        return jsonify({"msg": "method not allow"}), 405


@users_routes.route("/users", methods=["GET"])
@jwt_required()
def get_users():
    if request.method == "GET":

        try:
            users = []

            for user in User.query.all():
                users.append(
                    {
                        "id": user.id,
                        "name": user.fullname,
                        "username": user.username,
                        "email": user.email,
                        "phone": user.phone,
                    }
                )

            return jsonify(users), 200

        except:
            return jsonify({"Users": "Something was wrong"})

    else:
        return jsonify({"Users": "method not allow"}), 405
