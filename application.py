from flask import Flask, request
import json

users = {'jay':{"password": "112233"}}

app = Flask(__name__)
print(users.keys())

@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        data = request.data.decode('utf-8')
        data = json.loads(data)
        if data['name'] in users.keys():
            return '{"error": {"error_code": "Account axists"}, "rep": "/sign_up"}'
        else:
            users[data['name']] = {"password": data["password"]}
            print(users)
            return '{"error": False, "rep": "/login_in"}'
        

    return 'Error'

@app.route('/login_in', methods=['POST', 'GET'])
def login_in():
    if request.method == 'POST':
        data = request.data.decode('utf-8')
        data = json.loads(data)
        if data['name'] in users.keys():
            password = users.get(data['name'])
            password = password.get('password')
            if password == data.get('password'):
                return_data = {"login_sucess": "True", "cred": {"name": data.get('name'), "password": data.get('password')}, "rep": "/home"}
                return str(return_data)
        else:
            return '{"error": {"code": "True", "name": "Invaild username/password"}}'

if __name__ == '__main__':
        app.run(debug=True)