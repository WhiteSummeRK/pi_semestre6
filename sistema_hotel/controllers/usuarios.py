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

app = Blueprint('usuarios', __name__)


@app.route('/', methods=['GET'])
@login_required
def view_users():
    return render_template('usuarios.html')


@app.route('/', methods=['POST'])
@login_required
def cadastrar_user():
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    confirmarsenha = request.form.get('confirmarsenha')
    tipo = request.form.get('tipo')
    erro = True if senha != confirmarsenha or tipo == '0' else False
    return 'ok'
