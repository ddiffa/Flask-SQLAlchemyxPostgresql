from marshmallow import fields, Schema
import datetime
from . import db
from sqlalchemy import ForeignKey
from ParticipantModel import ParticipantSchema

class TicketModel(db.Model):

    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)
    fk_userid = db.Column(db.Integer,ForeignKey('users.id'),nullable=False)
    fk_eventid = db.Column(db.Integer,ForeignKey('events.id'),nullable=False)
    ticket_qty = db.Column(db.Integer, nullable=False)
    participans = db.relationship('ParticipantModel',backref=db.backref("tickets",lazy=True))

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
        return TicketModel.query.filter_by(fk_userid=value).all()
    
    def __repr(self):
        return '<id {}>'.format(self.id)
    
class TicketSchema(Schema):

    id = fields.Int(dump_only=True)
    fk_userid = fields.Int(required=True)
    fk_eventid = fields.Int(required=True)
    ticket_qty = fields.Int(required=True)
    participans = fields.Nested(ParticipantSchema,many=True)

