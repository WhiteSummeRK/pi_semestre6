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
                                               update_room_state,
                                               query_all_resident_accounts,
                                               query_resident_by_id,
                                               query_room_by_id)
from flask_login import login_required, current_user
from sistema_hotel.controllers.languages import messages

app = Blueprint('rooms', __name__)

@app.route('/', methods=['GET'])
@login_required
def view_rooms():
    rooms_query = query_all_rooms()

    return render_template('rooms.html',
                           rooms=rooms_query,
                           language=messages[session['languages']])

@app.route('/checkin', methods=['GET'])
@login_required
def view_checkin():
    residents_query = query_all_residents()
    residents_name = [residents.name for residents in residents_query]

    rooms_query = query_all_rooms()
    rooms = [room.number for room in rooms_query if room.status == 'Livre']

    return render_template('Checkin.html',
                           residents=residents_name,
                           rooms=rooms)


@app.route('/checkin', methods=['POST'])
@login_required
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

    return redirect(url_for('rooms.view_checkin'))

@app.route('/checkout', methods=['GET'])
@login_required
def view_checkout():
    act_query = query_all_resident_accounts()
    acts = [act.id_resident for act in act_query]
    rooms = [rooms.id_room for rooms in act_query]

    users = [query_resident_by_id(item) for item in acts]
    all_rooms = [query_room_by_id(room_id) for room_id in rooms]

    return render_template('Checkout.html',
                           rooms=all_rooms,
                           users=users)


@app.route('/checkout', methods=['POST'])
@login_required
def post_checkout():
    room = request.form.get('fake_input')
    user = query_resident_by_room(int(room), 'Diogo')
