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

from sistema_hotel.models.db_functions import (save_resident,
                                               save_employee,
                                               query_all_residents,
                                               query_all_employees)
from sistema_hotel.controllers.languages import messages


app = Blueprint('usuarios', __name__)


@app.route('/', methods=['GET'])
@login_required
def view_users():
    error = request.args.get('error')
    users = request.args.get('users')
    if users == 'adm_only':
        return_users = query_all_employees()
    else:
        return_users = query_all_residents()
    return render_template('usuarios.html', error=error, language=messages[session['languages']], users=return_users)


@app.route('/', methods=['POST'])
@login_required
def cadastrar_user():
    nome = request.form.get('nome')
    rg = request.form.get('rg')
    cpf = request.form.get('cpf')
    telefone = request.form.get('telefone')
    senha = request.form.get('senha')
    confirmarsenha = request.form.get('confirmarsenha')
    tipo = request.form.get('tipo')
    erro = True if senha != confirmarsenha or tipo == '0' else False

    if senha != confirmarsenha:
        return redirect(url_for('usuarios.view_users', error='pwds'))
    if tipo == 'ADM':
        save_employee(name=nome, rg=rg, cpf=cpf, phone=telefone, pwd=senha)
        return redirect(url_for('usuarios.view_users', error='emp_saved'))

    if tipo == 'Hóspede':
        save_resident(username='ARRUMAR', rg=rg, cpf=cpf, phone=telefone, name=nome, pwd=senha)
        return redirect(url_for('usuarios.view_users', error='hos_saved'))

    return redirect(url_for('usuarios.view_users', error='selecionar_tipo'))
