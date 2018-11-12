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

app = Blueprint('menu', __name__)


@app.route('/', methods=['GET'])
@login_required
def view():
    return render_template('menu.html', language=messages[session['languages']])
