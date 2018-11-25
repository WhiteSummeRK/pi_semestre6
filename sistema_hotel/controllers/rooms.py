"""Modulo para as rotas de login."""
from datetime import datetime
from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    session,
    url_for,
    jsonify
)
from sistema_hotel.models.db_functions import (query_all_residents,
                                               query_resident_by_name,
                                               query_room_by_room_number,
                                               create_new_account,
                                               query_all_rooms,
                                               update_room_state,
                                               query_all_resident_accounts,
                                               query_resident_by_id,
                                               query_room_by_id,
                                               query_all_busy_rooms,
                                               query_all_free_rooms)
from flask_login import login_required, current_user
from sistema_hotel.controllers.languages import messages

app = Blueprint('rooms', __name__)

@app.route('/', methods=['GET'])
@login_required
def view_rooms():
    error = request.args.get('error')
    types = request.args.get('rooms')
    if types == 'free_rooms':
        rooms_query = query_all_free_rooms()
    elif types == 'busy_rooms':
        rooms_query = query_all_busy_rooms()
    else:
        rooms_query = query_all_rooms()

    return render_template('rooms.html',
                           rooms=rooms_query,
                           language=messages[session['languages']],
                           error=error)

@app.route('/checkin', methods=['POST'])
@login_required
def post_checkin():
    resident_name = request.json.get('name')
    room_number = request.json.get('id')

    resident = query_resident_by_name(resident_name)

    if resident:
        update_room_state(room_number, 'Ocupado')
        new_account = create_new_account(
            resident=resident_name,
            room=query_room_by_room_number(room_number),
            openned=datetime.now(),
            closed=datetime.now(),
            status='Não pago',
            value=0.0
        )
        return jsonify({"error": 'success',
                        "id": room_number})
    return jsonify({"error": 'no_guests',
                    "id": room_number})



@app.route('/checkout', methods=['GET'])
@login_required
def view_checkout():
    # act_query = query_all_resident_accounts()
    # acts = [act.id_resident for act in act_query]
    # rooms = [rooms.id_room for rooms in act_query]
    #
    # users = [query_resident_by_id(item) for item in acts]
    # all_rooms = [query_room_by_id(room_id) for room_id in rooms]

    return render_template('Checkout.html', language=messages[session['languages']])


@app.route('/checkout', methods=['POST'])
@login_required
def post_checkout():
    room = request.form.get('fake_input')
    user = query_resident_by_room(int(room), 'Diogo')
