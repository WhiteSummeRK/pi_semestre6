"""Modulo para a criação das blueprints do flask"""
from flask import Flask

from .controllers.login import app as login
from .controllers.check_out import app as check_out
from .controllers.check_in import app as check_in
from .controllers.cadastro_usuarios import app as cadastro_usuarios
from .controllers.cadastro_pedidos import app as cadastro_pedidos
from .controllers.cadastro_hospede import app as cadastro_hospede


app = Flask(__name__, template_folder='views', static_folder='assets')

app.register_blueprint(login, url_prefix='/')
app.register_blueprint(check_out, url_prefix='/check_out')
app.register_blueprint(check_in, url_prefix='/check_in')
app.register_blueprint(cadastro_usuarios, url_prefix='/cadastro_usuarios')
app.register_blueprint(cadastro_pedidos, url_prefix='/cadastro_pedidos')
app.register_blueprint(cadastro_hospede, url_prefix='/cadastro_hospede')
