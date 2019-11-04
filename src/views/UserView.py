from flask import request, json, Response, Blueprint,g
from models.UserModel import UserModel,UserSchema
from shared.Authentication import Auth
from flask import jsonify

user_api = Blueprint('users',__name__)

user_schema = UserSchema()


@user_api.route('/login',methods=['POST'])
def login():
    req_data = request.get_json()

    data,error = user_schema.load(req_data,partial=True)

    if error:
        return custom_response(error,400)
    
    if not data.get('email') or not data.get('password'):
        return custom_response({'error' : 'you need email and password to sign in'},400)
    
    user = UserModel.get_user_by_email(data.get('email'))

    if not user:
        return custom_response({'error':'invalid credentials'},400)
    
    ser_data = user_schema.dump(user).data

    token = Auth.generate_token(ser_data.get('id'))

    return custom_response({'token':token},200)
    
@user_api.route('/register',methods=['POST'])
@Auth.auth_required
def create():
    req_data = request.get_json()
    data,error = user_schema.load(req_data)

    if error:
        return custom_response(error,400)
    
    user_in_db = UserModel.get_user_by_email(data.get('email'))

    if user_in_db:
        message = {
            'error': 'User already exist, please supply another email address'
        }
        return custom_response(message,400)
    
    user = UserModel(data)
    user.save()

    ser_data = user_schema.dump(user).data
    user = {}
    user.update({'id': ser_data.get('id'), 'name': ser_data.get('name'), 'email':ser_data.get('email'), 'phone': ser_data.get('phone'), 'role':ser_data.get('role')})
    return custom_response({'messages':'Register success','user':user},200)

@user_api.route('/',methods=['GET'])
def get_all():
    users = UserModel.get_all_users()
    ser_users = user_schema.dump(users,many=True).data
    
    for i in range(0,len(ser_users)):
        del ser_users[i]['password']
    users = {}
    users.update({'users' : ser_users})
    return custom_response(users,200)

@user_api.route('/<int:user_id>', methods=['GET'])
@Auth.auth_required
def get_a_user(user_id):
    user = UserModel.get_one_user(user_id)
    if not user:
        return custom_response({'error':'user not found'},404)
    
    ser_user =user_schema.dump(user).data
    del ser_user['password']
    return custom_response(ser_user,200)

@user_api.route('/me',methods=['PUT'])
@Auth.auth_required
def update():
    req_data =request.get_json()
    data, error = user_schema.load(req_data,partial=True)
    if error:
        return custom_response(error,400)
    
    user = UserModel.get_one_user(g.user.get('id'))
    user.update(data)
    ser_user = user_schema.dump(user).data
    return custom_response(ser_user,200)

@user_api.route('/<int:user_id>', methods=['DELETE'])
@Auth.auth_required
def delete(user_id):
    user = UserModel.get_one_user(user_id)
    if not user:
        return custom_response({'messages':'User not found'},404)
    user.delete()
    if user:
        return custom_response({'messages':'user has been deleted.'},200)
   
    return custom_response({'messages':'error'},400)

@user_api.route('/me', methods=['GET'])
@Auth.auth_required
def get_me():
    user = UserModel.get_one_user(g.user.get('id'))
    ser_user = user_schema.dump(user).data
    return custom_response(ser_user,200)


def custom_response(res,status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )