from flask import Flask

from config import app_config
from models import db
from views.UserView import user_api as user_blueprint

def create_app(env_name):
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')

    @app.route('/',methods=['GET'])
    def index():
        return 'Congratulations'
    
    return app