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

from sistema_hotel.models.db_functions import query_all_orders

app = Blueprint('pedidos_abertos', __name__)


@app.route('/', methods=['GET'])
@login_required
def view():
    orders = query_all_orders()
    import ipdb; ipdb.set_trace()
    return render_template('Pedidos_Abertos.html')
