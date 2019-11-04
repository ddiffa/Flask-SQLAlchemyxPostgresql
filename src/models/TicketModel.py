from marshmallow import fields, Schema
import datetime
from . import db

class EventModel(db.Model):

    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)
    fk_userid = db.Column(db.Integer,ForeignKey('users.id'))
    fk_eventid = db.Column(db.Integer,ForeignKey('events.id'))
    ticket_name = db.Column(db.String(400), nullable=False)
    ticket_phone = db.Column(db.String(300), nullable=Fal
    ticket_qty = db.Column(db.Integer, nullable=False)

    def __init__(self,data):
        self.fk_userid = data.get('user_id')
        self.fk_eventid = data.get('event_id')
        self.ticket_name = data.get('ticket_name')
        self.ticket_phone = data.get('ticket_phone')
        self.ticket_qty = data.get('ticket_qty')
    
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
    def get_all_ticket():
        return TicketModel.query.all()
    
    @staticmethod
    def get_one_ticket(id):
        return TicketModel.query.get(id)
    
    @staticmethod
    def get_ticket_by_userid(value):
        return TicketModel.query.filter_by(user_id=value).first()
    
    def __repr(self):
        return '<id {}>'.format(self.id)
    
class TicketSchema(Schema):

    id = fields.Int(dump_only=True)
    fk_userid = fields.Int(required=True)
    fk_eventid = fields.Int(required=True)
    ticket_name = fields.Str(required=True)
    ticket_phone = fields.Str(required=True)
    ticket_qty = fields.Int(required=True)

