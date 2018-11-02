"""Modulo para as rotas de login."""
from flask import (
    abort,
    Blueprint,
    redirect,
    render_template,
    request,
    session,
    url_for,
    jsonify,
    json
)
from flask_login import login_user, logout_user

from sistema_hotel.models.db_functions import query_user,query_resident
from sistema_hotel.controllers.languages import messages

app = Blueprint('login', __name__)


@app.route('/', methods=['GET'])
def view():
    logout_user()
    return render_template('login.html',
                           login_error='false')


@app.route('/', methods=['POST'])
def do_login():
    username = request.form.get('username')
    pwd = request.form.get('pwd')
    language = request.form.get('fooby[1][]')
    user = query_user(username=username, pwd=pwd)
    if user and pwd == user.pwd:
        login_user(user)
        session['languages'] = language
        return render_template('menu.html', language=messages[language]) #NOQA
    return render_template('login.html',
                           login_error='true')


@app.route('/api_login', methods=['POST', 'GET'])
def login_api():
    username = request.form.get('username')
    pwd = request.form.get('pwd')
    user = query_resident(username=username, pwd=pwd)
    if user and pwd == user.pwd:
        result = {'user':user.username,
                  'name':user.name,
                  'room_description':user.description,
                  'room_id': user.id_room,
                  'room_number': user.number,
                  'room_floor': user.floor,
                  'room_daily_value':user.daily_value,
                  'is_authenticated':1}
    else:
        result = {'user':username,
                  'is_authenticated':0}
    return jsonify(result)
