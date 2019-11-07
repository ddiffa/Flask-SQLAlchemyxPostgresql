from marshmallow import fields, Schema
import datetime
from . import db
from sqlalchemy import ForeignKey

class ParticipantModel(db.Model):

    __tablename__ = 'participans'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(400), nullable=False)
    phone = db.Column(db.String(300), nullable=False)
    qrcode = db.Column(db.String, nullable=False)
    fk_ticket = db.Column(db.Integer,ForeignKey("tickets.id"))
    status = db.Column(db.Boolean, nullable=False)
    
    def save(self):
        print(self.name)
        db.session.add(self)
        db.session.commit()
    
    def update(self,data):
        for key, item in data.items():
            setattr(self,key,item)
        db.session.commit()

    def update_status(self,data):
        setattr(self,'status',data)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


    @staticmethod
    def save_all(part,ticket):
        db.session.add(part)
        db.session.add(ticket)
        db.session.commit()

    @staticmethod
    def get_all_participant():
        return ParticipantModel.query.all()
    
    @staticmethod
    def get_one_participant(id):
        return ParticipantModel.query.get(id)
    
    @staticmethod
    def get_participant_by_ticket(value):
        return ParticipantModel.query.filter_by(fk_ticket=value).all()
    
    @staticmethod
    def get_partcipant_by_qrcode(value):
        return ParticipantModel.query.filter_by(qrcode=value).first()

    def __repr(self):
        return '<id {}>'.format(self.id)
    
class ParticipantSchema(Schema):

    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    phone = fields.Str(required=True)
    qrcode = fields.Str()
    status = fields.Bool()


