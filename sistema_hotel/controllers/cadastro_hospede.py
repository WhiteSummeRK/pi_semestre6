"""Modulo para as rotas de login."""
from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    session,
    url_for
)
from sistema_hotel.models.db_functions import save_resident

app = Blueprint('cadastro_hospede', __name__)


@app.route('/', methods=['GET'])
def view():
    return render_template('Cadastro_Hospede.html')


@app.route('/', methods=['POST'])
def post_view():
    name = request.form.get('nome')
    rg = request.form.get('rg')
    cpf = request.form.get('cpf')
    phone = request.form.get('phone')

    try:
        save_resident(name=name, rg=rg, cpf=cpf, phone=phone)
        return render_template('Cadastro_Hospede.html', insertion_code=201)
    except Exception:
        return render_template('Cadastro_Hospede.html', insertion_code=500)
