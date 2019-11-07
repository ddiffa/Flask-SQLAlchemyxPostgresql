from flask import Flask

from config import app_config
from models import db
from views.UserView import user_api as user_blueprint
from views.EventView import event_api as event_blueprint
from views.TicketView import ticket_api as ticket_blueprint
from views.ParticipantView import participant_api as participant_blueprint
from views.QrView import qr_api as qr_blueprint
def create_app(env_name):
    app = Flask(__name__,static_folder='image/')

    UPLOAD_FOLDER = 'path/src'
    app.config.from_object(app_config[env_name])
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    db.init_app(app)


    app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')
    app.register_blueprint(event_blueprint,url_prefix='/api/v1/events')
    app.register_blueprint(ticket_blueprint,url_prefix='/api/v1/tickets')
    app.register_blueprint(participant_blueprint,url_prefix='/api/v1/participants')
    app.register_blueprint(qr_blueprint,url_prefix='/api/v1/scanqr')

    @app.route('/',methods=['GET'])
    def index():
        return 'Free Event API'
    
    return app