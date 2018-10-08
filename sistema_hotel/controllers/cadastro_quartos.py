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

app = Blueprint('cadastro_quartos', __name__)


@app.route('/', methods=['GET'])
@login_required
def view():
    return render_template('Cadastro_Quartos.html')
