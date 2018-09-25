"""Modulo para as rotas de login."""
from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    session,
    url_for
)
from sistema_hotel.models.db_functions import (query_all_resident_accounts,
                                               query_resident_by_id,
                                               query_room_by_id,
                                               query_resident_by_room,
                                               update_room_state)

app = Blueprint('checkout', __name__)


@app.route('/', methods=['GET'])
def view():
    act_query = query_all_resident_accounts()
    acts = [act.id_resident for act in act_query]
    rooms = [rooms.id_room for rooms in act_query]

    users = [query_resident_by_id(item) for item in acts]
    all_rooms = [query_room_by_id(room_id) for room_id in rooms]

    return render_template('Checkout.html',
                           rooms=all_rooms,
                           users=users)


@app.route('/', methods=['POST'])
def post_checkout():
    room = request.form.get('fake_input')
    import ipdb; ipdb.set_trace()
    user = query_resident_by_room(int(room), 'Diogo')
