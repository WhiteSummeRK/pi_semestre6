"""Modulo para as rotas de login."""
from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    session,
    url_for
)
from flask_login import login_required

from sistema_hotel.controllers.languages import messages
from sistema_hotel.models.db_functions import (query_all_orders,
                                               query_specific_status_orders,
                                               query_room_by_id,
                                               query_resident_by_id)


app = Blueprint('pedidos', __name__)


@app.route('/', methods=['GET'])
@login_required
def view():
    orders = query_all_orders(10)
    payload = []
    for item in orders:
        room = query_room_by_id(item.id_room)
        resident = query_resident_by_id(item.id_resident)
        payload.append([room.number, resident.name, room.floor, item.total_value, item.date, item.status]) # NOQA

    return render_template('services.html',
                           language=messages[session['languages']],
                           payload=payload)


@app.route('/', methods=['POST'])
@login_required
def post_pedidos():
    users = request.form.get('users')
    amount = request.form.get('amount')
    payload = []

    if users == 'all':
        orders = query_all_orders(amount)
    if users == 'closed':
        orders = query_specific_status_orders('2', amount)
    if users == 'doing':
        orders = query_specific_status_orders('1', amount)
    if users == 'waiting':
        orders = query_specific_status_orders('0', amount)
    for item in orders:
        room = query_room_by_id(item.id_room)
        resident = query_resident_by_id(item.id_resident)
        payload.append([room.number, resident.name, room.floor, item.total_value, item.date, item.status]) # NOQA

    return render_template('services.html',
                           language=messages[session['languages']],
                           payload=payload)
