"""Modulo para as rotas de login."""
from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    session,
    url_for
)
from flask_login import login_required, current_user
from sistema_hotel.controllers.languages import messages


app = Blueprint('residents', __name__)


@app.route('/', methods=['GET'])
@login_required
def view_users():
    return render_template('residents.html', language=messages[session['languages']])
