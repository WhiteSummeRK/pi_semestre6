"""Modulo para as rotas de login."""
from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    session,
    url_for
)
from sistema_hotel.models.db_functions import (query_all_rooms,
                                               query_resident_by_room,
                                               update_room_state)

app = Blueprint('checkout', __name__)


@app.route('/', methods=['GET'])
def view():
    rooms_query = query_all_rooms()
    rooms = [room.number for room in rooms_query if room.status == 'Ocupado']

    return render_template('Checkout.html',
                           rooms=rooms)

@app.route('/', methods=['POST'])
def post_checkout():
    room = request.form.get('fake_input')
    user = query_resident_by_room(int(room), 'Diogo')
