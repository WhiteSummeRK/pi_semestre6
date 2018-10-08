"""Modulo para a criação das blueprints do flask"""
from flask import Flask, session
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

from .controllers.login import app as login
from .controllers.mobile_api_services import app as Service

from .controllers.check_out import app as check_out
from .controllers.check_in import app as check_in

from .controllers.cadastro_usuarios import app as cadastro_usuarios
from .controllers.cadastro_pedidos import app as cadastro_pedidos
from .controllers.cadastro_hospede import app as cadastro_hospede
from .controllers.cadastro_quartos import app as cadastro_quartos
from .controllers.menu_principal import app as menu_principal
from .controllers.pedidos_abertos import app as pedidos_abertos
from .controllers.pedidos_cancelados import app as pedidos_cancelados
from .controllers.pedidos_finalizados import app as pedidos_finalizados
from .models.tables import db_url, db, User
from sistema_hotel.models.tables import session as db_session


login_manager = LoginManager()


app = Flask(__name__, template_folder='views', static_folder='assets')

login_manager.init_app(app)
app.secret_key = b'67f54d66374c116022d7ed12c94961022a9ecc3372ba56a6'
app.config['SESSION_TYPE'] = 'filesystem'
app.register_blueprint(login, url_prefix='/')
app.register_blueprint(login, url_prefix='/api_login')
app.register_blueprint(Service, url_prefix='/')
app.register_blueprint(check_out, url_prefix='/check_out')
app.register_blueprint(check_in, url_prefix='/check_in')
app.register_blueprint(cadastro_usuarios, url_prefix='/cadastro_usuarios')
app.register_blueprint(cadastro_pedidos, url_prefix='/cadastro_pedidos')
app.register_blueprint(cadastro_hospede, url_prefix='/cadastro_hospede')
app.register_blueprint(cadastro_quartos, url_prefix='/cadastro_quartos')
app.register_blueprint(menu_principal, url_prefix='/menu_principal')
app.register_blueprint(pedidos_abertos, url_prefix='/pedidos_abertos')
app.register_blueprint(pedidos_finalizados, url_prefix='/pedidos_finalizados')
app.register_blueprint(pedidos_cancelados, url_prefix='/pedidos_cancelados')


Session(app)

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@login_manager.user_loader
def load_user(id):
    return db_session.query(User).filter_by(id=ord(id)).first()
