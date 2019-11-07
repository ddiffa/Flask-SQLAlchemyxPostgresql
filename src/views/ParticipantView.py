from flask import request, json, Response, Blueprint,g
from models.ParticipantModel import *
from shared.Authentication import Auth
from models.TicketModel import TicketModel
from models import db

participant_api = Blueprint('participants',__name__)

participant_schema = ParticipantSchema()
participants_schema = ParticipantSchema(many=True)

@participant_api.route('/',methods=['GET'])
@Auth.auth_required
def get_all():
    participant = ParticipantModel.get_all_participant()
    ser_participant = participant_schema.dump(participant,many=True).data

    return custom_response(ser_participant,200)

@participant_api.route('/<int:participant_id>',methods=['GET'])
@Auth.auth_required
def get_a_participant(participant_id):
    participant = ParticipantModel.get_one_participant(participant_id)
    if not participant:
        return custom_response({'error':'participant not found'},400)
    
    ser_participant = participant_schema.dump(participant).data
    return custom_response(ser_participant,200)

@participant_api.route('/<int:participant_id>',methods=['PUT'])
@Auth.auth_required
def update(participant_id):
    req_data =request.get_json()
    data, error = participant_schema.load(req_data,partial=True)
    if error:
        return custom_response(error,400)
    
    participant = ParticipantModel.get_one_participant(participant_id)
    participant.update(data)
    ser_participant = participant_schema.dump(ticket).data
    return custom_response(ser_participant,200)

@participant_api.route('/<int:participant_id>', methods=['DELETE'])
@Auth.auth_required
def delete(participant_id):
    participant = ParticipantModel.get_one_participant(participant_id)
    if not participant:
        return custom_response({'messages':'Participant not found'},404)
    participant.delete()
    if participant:
        return custom_response({'messages':'Participant has been deleted.'},200)
   
    return custom_response({'messages':'error'},400)

def custom_response(res,status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )