from  flask import Flask, abort, request
import json
from users_commands import get_all_users, add_user, remove_user, recently_logged, user_info, user_commands
app = Flask(__name__)
api_url = '/v1.0'

@app.route(api_url+'/users',methods=['POST'])
def create_user():
  content = request.get_json(silent=True)
  username = content['username']
  password = content['password']
  if not username or not password:
    return "empty username or password", 400
  if username in get_all_users():
    return "user already exist", 400
  if add_user(username,password):
    return "user created", 201
  else:
    return "error while creating user", 400


@app.route(api_url+'/users/<string:username>', methods=['GET'])
def get_user_info(username):
	info = user_info(""+username)
        return info, 200

@app.route(api_url+'/users/recently_logged',methods=['GET'])
def get_recent():
        list = {}
        list = recently_logged()
        return json.dumps(list), 200


@app.route(api_url+'/users/<string:username>/commands',methods=['GET'])
def get_user_commands(username):
        commands = {}
        commands = user_commands(""+username)
        return json.dumps(commands), 200



@app.route(api_url+'/users',methods=['GET'])
def read_user():
  list = {}
  list["users"] = get_all_users()
  return json.dumps(list), 200

@app.route(api_url+'/users',methods=['PUT'])
def update_user():
  return "not implemented", 501 # Not found


@app.route(api_url+'/users',methods=['DELETE'])
def delete_user():
  error = False
  for username in get_all_users():
    if not remove_user(username):
        error = True

  if error:
    return 'some users were not deleted', 400
  else:
    return 'all users were deleted', 200

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8080,debug='True')
