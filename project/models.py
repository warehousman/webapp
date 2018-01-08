from project import db
from sqlalchemy_utils.types import UUIDType

class TmpLog(db.Model):
    __tablename__ = 'templog'

    id = db.Column(db.Integer, primary_key=True)
    temp_value = db.Column(db.Integer, nullable=False)
    temp_data = db.Column(db.DateTime, nullable=False)

    def __init__(self, temp_value, temp_data):
        self.temp_value = temp_value
        self.temp_data = temp_data

    def __repr__(self):
        return self.temp_value


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(UUIDType, server_default="gen_random_uuid()", primary_key=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_plaintext = db.Column(db.String, nullable=False)  # TEMPORARY - TO BE DELETED IN FAVOR OF HASHED PASSWORD

    def __init__(self, email, password_plaintext):
        self.email = email
        self.password_plaintext = password_plaintext

    def __repr__(self):
        return '<User {0}>'.format(self.name)