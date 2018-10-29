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

from sistema_hotel.models.db_functions import (query_all_orders,
                                               query_room_by_id,
                                               query_resident_by_id)

app = Blueprint('pedidos_abertos', __name__)


@app.route('/', methods=['GET'])
@login_required
def view():
    payload = []
    orders = query_all_orders()
    for item in orders:
        if item.status == 'Aberto':
            room = query_room_by_id(item.id_room)
            resident = query_resident_by_id(item.id_resident)
            payload.append([resident.name, room.number, room.floor, item.date, 'TESTE']) # NOQA

    return render_template('Pedidos_Abertos.html', payload=payload)
