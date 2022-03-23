from ..utils.db import db
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))
    username = db.Column(db.String(100))
    password = db.Column(db.String(255))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))


    def __init__(self, fullname, username, password, email, phone) :
        self.fullname = fullname
        self.username = username
        self.password = self._create_secure_password(password)
        self.email = email
        self.phone = phone
        
    
    def _create_secure_password(self, password):
        return generate_password_hash(password)
    
    def _verify_secure_password(self, password):
        return check_password_hash(self.password, password)