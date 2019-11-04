from marshmallow import fields, Schema
import datetime
from . import db
from hashlib import md5

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128),nullable=False)
    email = db.Column(db.String(128), unique=True,nullable=False)
    password = db.Column(db.String(128),nullable=True)
    phone = db.Column(db.String(128),nullable=False)
    role = db.Column(db.Integer,nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __init__(self,data):
        self.name = data.get('name')
        self.email = data.get('email')
        self.password = md5(data.get('password').encode('UTF-8')).hexdigest()
        self.phone = data.get('password')
        self.role = data.get('role')
        self.created_at = datetime.datetime.now()
        self.modified_at = datetime.datetime.now()
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self,data):
        for key, item in data.items():
            if key == 'password':
                self.password = md5(data.get('password').encode('UTF-8')).hexdigest()
            setattr(self,key,item)
        self.modified_at = datetime.datetime.now()
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @staticmethod
    def get_all_users():
        return UserModel.query.all()
    
    @staticmethod
    def get_one_user(id):
        return UserModel.query.get(id)
    
    @staticmethod
    def get_user_by_email(value):
        return UserModel.query.filter_by(email=value).first()

    def __repr(self):
        return '<id {}>'.format(self.id)
    
class UserSchema(Schema):

    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    phone = fields.Str(required=True)
    role = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
