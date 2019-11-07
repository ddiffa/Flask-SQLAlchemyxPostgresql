from flask import request, json, Response, Blueprint,g
from models.ParticipantModel import *
from shared.Authentication import Auth
from models.TicketModel import TicketModel
from models import db

qr_api = Blueprint('scanqr',__name__)

qr_schema = ParticipantSchema()

@qr_api.route('/',methods=['POST'])
@Auth.auth_required
def scan_qr():
    qrcode = request.form.get('qrcode')

    participant = ParticipantModel.get_partcipant_by_qrcode(qrcode)
    
    if not participant:
        return custom_response({'message':'QRCode not found'},400)
    
    ser_data = qr_schema.dumps(participant).data
    
    if not json.loads(ser_data).get('status'):
        return custom_response({'message' : 'QRCode is already in use'},400)
    else:
        participant.update_status(False)
    
    return custom_response({'message':'Success'},200)
    #return custom_response({'message':'Success'},200)

def custom_response(res,status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )



