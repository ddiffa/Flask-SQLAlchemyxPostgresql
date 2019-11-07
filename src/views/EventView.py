from flask import request, json, Response, Blueprint,g
from models.EventModel import *
from shared.Authentication import Auth
from flask import send_from_directory, redirect, url_for
from werkzeug.utils import secure_filename
import os
import app
event_api = Blueprint('events',__name__)

event_schema = EventSchema()


@event_api.route('/',methods=['POST'])
@Auth.auth_required
def create_event():
    event = EventModel()
    event.fk_userid = request.form.get('fk_userid')
    event.event_name = request.form.get('name')
    event.event_date = request.form.get('date')
    event.event_place = request.form.get('place')
    event.event_detail = request.form.get('detail')
    event.event_category = request.form.get('category')
    event.event_talent = request.form.get('talent')
    event.event_quota = request.form.get('quota')

    if 'file' not in request.files:
        flash('No File Part')
        return redirect(request.url)
    f = request.files['file']

    if f.filename == '':
        flash('No selected file')
    if f:
        filename = secure_filename(f.filename)
        f.save(os.path.abspath("../image/"+filename))
        event.event_image = request.host_url+'image/'+filename
    event.save()
    
    ser_data = event_schema.dump(event).data

    return custom_response({'messages':'success','event':ser_data},200)

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

@event_api.route('/<int:event_id>',methods=['PUT'])
@Auth.auth_required
def update(event_id):
    req_data = request.get_json()
    data,error = event_schema.load(req_data,partial=True)
    if error:
        return custom_response(error,400)
    
    event = EventModel.get_one_event(event_id)
    event.update(data)
    ser_event = event_schema.dump(event).data
    return custom_response(ser_event,200)

@event_api.route('/<int:event_id>',methods=['DELETE'])
@Auth.auth_required
def delete(event_id):
    event = EventModel.get_one_event(event_id)
    event.delete()
    return custom_response({'message':'deleted'},204)

@event_api.route('/me',methods=['GET'])
@Auth.auth_required
def get_event():
    event = EventModel.get_event_by_user(g.user.get('id'))
    ser_event=event_schema.dump(event,many=True).data
    return custom_response(ser_event,200)

@event_api.route('/upload/files',methods=['POST'])
def upload_file():
    print(request.form)
    event = EventModel()
    event.fk_userid = request.form.get('fk_userid')
    event.event_name = request.form.get('name')
    event.event_date = request.form.get('date')
    event.event_place = request.form.get('place')
    event.event_detail = request.form.get('detail')
    event.event_category = request.form.get('category')
    event.event_talent = request.form.get('talent')
    event.event_quota = request.form.get('quota')

    if 'file' not in request.files:
        flash('No File Part')
        return redirect(request.url)
    f = request.files['file']

    if f.filename == '':
        flash('No selected file')
    if f:
        filename = secure_filename(f.filename)
        f.save(filename)
        event.event_image = filename
    event.save()

    return 'susccess'


def custom_response(res,status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )