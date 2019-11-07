from flask import request, json, Response, Blueprint,g
from models.TicketModel import TicketSchema,TicketModel
from shared.Authentication import Auth
from models import db
from models.ParticipantModel import ParticipantModel,ParticipantSchema
from models.EventModel import EventModel,EventSchema


ticket_api = Blueprint('tickets',__name__)

ticket_schema = TicketSchema()
p_schema = ParticipantSchema(many=True)
event_schema = EventSchema()

@ticket_api.route('/',methods=['POST'])
@Auth.auth_required
def create_ticket():
    req_data = request.get_json()

    data,error = ticket_schema.load(req_data)

    if error:
        return custom_response(error,400)
    

    event = EventModel.get_one_event(data.get('fk_eventid'))

    ser_event = event_schema.dump(event).data

    if ser_event.get('event_quota') == 0:
        return custom_response({'message':'ticket sold out'},400)
    elif data.get('ticket_qty') > ser_event.get('event_quota'):
        return custom_response({'message':'ticket gak cukup mas'},400)

    tp =  p_schema.load(data.get('participans')).data
    ticket = TicketModel()
    ticket.fk_userid=data.get('fk_userid')
    ticket.fk_eventid=data.get('fk_eventid')
    ticket.ticket_qty=data.get('ticket_qty')
    db.session.add(ticket)
    db.session.commit()
    
    event.update_stock(data.get('ticket_qty'))

    fk_ticket = ticket.id

    for i in range(0,len(tp)):
        part = ParticipantModel()
        part.name =tp[i]['name']
        part.phone=tp[i]['phone']
        part.qrcode=Auth.generate_qrcode(tp[i]['phone']+tp[i]['name'])
        part.status=True
        part.fk_ticket=fk_ticket
        part.save()
        

    ser_ticket = ticket_schema.dump(TicketModel.get_one_ticket(ticket.id)).data
    
    return custom_response({'ticket':ser_ticket},200)

@ticket_api.route('/',methods=['GET'])
@Auth.auth_required
def get_all():
    ticket = TicketModel.get_all_ticket()
    ser_ticket = ticket_schema.dump(ticket,many=True).data

    return custom_response(ser_ticket,200)

@ticket_api.route('/<int:ticket_id>',methods=['GET'])
@Auth.auth_required
def get_a_ticket(ticket_id):
    ticket = TicketModel.get_one_ticket(ticket_id)
    if not ticket:
        return custom_response({'error':'ticket not found'},400)
    
    ser_ticket = ticket_schema.dump(ticket).data
    return custom_response(ser_ticket,200)

@ticket_api.route('/me',methods=['GET'])
@Auth.auth_required
def get_my_ticket():
    ticket = TicketModel.get_ticket_by_userid(g.user.get('id'))
    if not ticket:
        return custom_response({'error':'ticket not found'},400)
    
    ser_ticket = ticket_schema.dump(ticket,many=True).data
    return custom_response(ser_ticket,200)

@ticket_api.route('/<int:ticket_id>',methods=['PUT'])
@Auth.auth_required
def update(ticket_id):
    req_data =request.get_json()
    data, error = ticket_schema.load(req_data,partial=True)
    if error:
        return custom_response(error,400)
    
    ticket = TicketModel.get_one_ticket(ticket_id)
    ticket.update(data)
    ser_ticket = ticket_schema.dump(ticket).data
    return custom_response(ser_ticket,200)

@ticket_api.route('/<int:ticket_id>', methods=['DELETE'])
@Auth.auth_required
def delete(ticket_id):
    ticket = TicketModel.get_one_ticket(ticket_id)
    if not ticket:
        return custom_response({'messages':'Ticket not found'},404)
    ticket.delete()
    if ticket:
        return custom_response({'messages':'Ticket has been deleted.'},200)
   
    return custom_response({'messages':'error'},400)

def custom_response(res,status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )