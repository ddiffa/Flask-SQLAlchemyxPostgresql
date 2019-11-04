from flask import request, json, Response, Blueprint,g
from models.TicketModel import TicketSchema,TicketModel
from shared.Authentication import Auth


ticket_api = Blueprint('tickets',__name__)

ticket_schema = TicketSchema()

@ticket_api.route('/',methods=['POST'])
@Auth.auth_required
def create_ticket():
    req_data = request.get_json()

    data,error = ticket_schema.load(req_data)

    if error:
        return custom_response(error,400)

    ticket = TicketModel(data)
    ticket.save()

    ser_ticket = ticket_schema.dump(ticket).data

    

    return custom_response({ser_ticket},200)

@ticket_api.route('/',methods=['GET'])
@Auth.auth_required
def get_all():
    ticket = TicketModel.get_all_ticket()
    ser_ticket = ticket_schema.dump(ticket,many=True).data

    return custom_response(ticket,200)

@ticket_api.route('/<int:ticket_id>',methods=['GET'])
@Auth.auth_required
def get_a_ticket(ticket_id):
    ticket = TicketModel.get_one_ticket(ticket_id)
    if not ticket:
        return custom_response({'error':'ticket not found'},400)
    
    ser_ticket = ticket_schema.dump(ticket).data
    return custom_response(ser_ticket,200)

def custom_response(res,status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )