"""Modulo para as rotas de login."""
from datetime import datetime
from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    session,
    url_for,
    jsonify,
    abort
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
                                               query_all_free_rooms,
                                               query_resident_account_by_room_number,
                                               update_account_status,
                                               do_checkout_date,
                                               reset_account_value)
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
    try:
        id = request.args.get("btn_checkout")
        account = query_resident_account_by_room_number(id)
        res = query_resident_by_id(account.id_resident)
        return render_template('checkout.html',
                                language=messages[session['languages']],
                                room_number=id,
                                account=account,
                                res=res,
                                date=datetime.now())
    except AttributeError as e:
        abort(406)

@app.route('/checkout', methods=['POST'])
@login_required
def post_checkout():
    try:
        id = request.form.get("btn_checkout")

        account = query_resident_account_by_room_number(id)
        update_account_status(id, "Pago")
        do_checkout_date(id)
        reset_account_value(id)
        return jsonify({"error": "success"})
    except Exception as e:
        return jsonify({"error": "error"})
