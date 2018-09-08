"""Modulo para as rotas de login."""
from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    session,
    url_for
)
from sistema_hotel.models.db_functions import (query_all_residents,
                                               query_all_rooms,
                                               update_room_state)

app = Blueprint('checkin', __name__)


@app.route('/', methods=['GET'])
def view():
    residents_query = query_all_residents()
    residents_name = [residents.name for residents in residents_query]

    rooms_query = query_all_rooms()
    rooms = [room.number for room in rooms_query]

    return render_template('Checkin.html',
                           residents=residents_name,
                           rooms=rooms)

@app.route('/', methods=['POST'])
def post_checkin():
    resident = request.form.get('resident')
    checkin_date = request.form.get('checkin')
    checkout_date = request.form.get('checkout')
