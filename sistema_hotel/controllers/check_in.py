"""Modulo para as rotas de login."""
from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    session,
    url_for
)

app = Blueprint('checkin', __name__)


@app.route('/', methods=['GET'])
def view():
    return render_template('Checkin.html')
