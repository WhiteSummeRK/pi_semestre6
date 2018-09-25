"""Modulo para as rotas de login."""
from datetime import datetime
from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    session,
    url_for
)
from sistema_hotel.models.db_functions import (query_all_residents,
                                               query_resident_by_name,
                                               query_room_by_room_number,
                                               create_new_account,
                                               query_all_rooms,
                                               update_room_state)

app = Blueprint('checkin', __name__)


@app.route('/', methods=['GET'])
def view():
    residents_query = query_all_residents()
    residents_name = [residents.name for residents in residents_query]

    rooms_query = query_all_rooms()
    rooms = [room.number for room in rooms_query if room.status == 'Livre']

    return render_template('Checkin.html',
                           residents=residents_name,
                           rooms=rooms)


@app.route('/', methods=['POST'])
def post_checkin():
    resident_name = request.form.get('resident')
    checkin_date = request.form.get('checkin')
    checkout_date = request.form.get('checkout')
    room_number = request.form.get('fake_input')

    update_room_state(room_number, 'Ocupado')

    resident = query_resident_by_name(resident_name)
    new_account = create_new_account(
        resident=resident,
        room=query_room_by_room_number(room_number),
        openned=datetime.now(),
        closed=datetime.now(),
        status='Não pago',
        value=0.0
    )

    return redirect(url_for('checkin.view'))
