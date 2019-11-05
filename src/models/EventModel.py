from marshmallow import fields, Schema
import datetime
from . import db
from sqlalchemy import ForeignKey

class EventModel(db.Model):

    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    fk_userid = db.Column(db.Integer,ForeignKey('users.id'))
    event_name = db.Column(db.String(400), nullable=False)
    event_date = db.Column(db.DateTime)
    event_place = db.Column(db.String(300), nullable=False)
    event_detail = db.Column(db.String(500),nullable=False)
    event_image = db.Column(db.String(250),nullable=False)
    event_category = db.Column(db.String(100),nullable=False)
    event_talent = db.Column(db.String(200),nullable=False)
    event_quota = db.Column(db.Integer, nullable=False)

    def __init__(self,data):
        self.fk_userid = data.get('fk_userid')
        self.event_name = data.get('event_name')
        self.event_date = data.get('event_date')
        self.event_place = data.get('event_place')
        self.event_detail = data.get('event_detail')
        self.event_image = data.get('event_image')
        self.event_category = data.get('event_category')
        self.event_talent = data.get('event_talent')
        self.event_quota = data.get('event_quota')
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self,data):
        for key, item in data.items():
            setattr(self,key,item)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    

    @staticmethod
    def get_all_event():
        return EventModel.query.all()
    
    @staticmethod
    def get_one_event(id):
        return EventModel.query.get(id)
    
    @staticmethod
    def get_event_by_name(value):
        return EventModel.query.filter_by(evet_name=value).first()
    
    @staticmethod
    def get_event_by_user(value):
        return EventModel.query.filter_by(fk_userid=value).all()
        
    def __repr(self):
        return '<id {}>'.format(self.id)
    
class EventSchema(Schema):

    id = fields.Int(dump_only=True)
    fk_userid = fields.Int(required=True)
    event_name = fields.Str(required=True)
    event_date = fields.DateTime(required=True)
    event_place = fields.Str(required=True)
    event_detail = fields.Str(required=True)
    event_image = fields.Str(required=True)
    event_category = fields.Str(required=True)
    event_talent = fields.Str(required=True)
    event_quota = fields.Int(required=True)

