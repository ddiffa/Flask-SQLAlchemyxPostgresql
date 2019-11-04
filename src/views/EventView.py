from flask import request, json, Response, Blueprint,g
from models.EventModel import *
from shared.Authentication import Auth

event_api = Blueprint('events',__name__)

event_schema = EventSchema()

@event_api.route('/',methods=['GET'])
@Auth.auth_required
def get_all():
    events = EventModel.get_all_event()
    ser_event = event_schema.dump(events,many=True).data

    return custom_response(ser_event,200)

@event_api.route('/<int:event_id>', methods=['GET'])
@Auth.auth_required
def get_a_event(event_id):
    event = EventModel.get_one_event(event_id)
    if not event:
        return custom_response({'error':'event not found'},400)
    
    ser_event = event_schema.dump(event).data
    return custom_response(ser_event,200)

@event_api.route('/',methods=['PUT'])
@Auth.auth_required
def update():
    req_data = request.get_json()
    data,error = event_schema.load(req_data,partial=True)
    if error:
        return custom_response(error,400)
    
    event = EventModel.get_one_event(g.event.get('id'))
    event.update(data)
    ser_event = event_schema.dump(event).data
    return custom_response(ser_event,200)

@event_api.route('/',methods=['DELETE'])
@Auth.auth_required
def delete():
    event = EventModel.get_one_event(g.event.get('id'))
    event.delete()
    return custom_response({'message':'deleted'},204)

@event_api.route('/me',methods=['GET'])
@Auth.auth_required
def get_event():
    event = EventModel.get_event_by_user(g.event.get('user_id'))
    ser_event=event_schema.dump(event).data
    return custom_response(ser_event,200)

def custom_response(res,status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )