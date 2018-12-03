"""Modulo para a criação das blueprints do flask"""
from flask import Flask, session
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

from .controllers.login import app as login
from .controllers.mobile_api_services import app as Service

from .controllers.rooms import app as rooms

from .controllers.usuarios import app as usuarios
from .controllers.residents import app as residents
from .controllers.cadastro_hospede import app as cadastro_hospede
from .controllers.cadastro_quartos import app as cadastro_quartos
from .controllers.menu_principal import app as menu
from .controllers.pedidos import app as pedidos
from .models.tables import db_url, db, Employee
from sistema_hotel.models.tables import session as db_session


login_manager = LoginManager()


app = Flask(__name__, template_folder='views', static_folder='assets')

login_manager.init_app(app)
app.secret_key = b'67f54d66374c116022d7ed12c94961022a9ecc3372ba56a6'
app.config['SESSION_TYPE'] = 'filesystem'
app.register_blueprint(login, url_prefix='/')
app.register_blueprint(login, url_prefix='/api_login')
app.register_blueprint(Service, url_prefix='/')
app.register_blueprint(rooms, url_prefix='/rooms')
app.register_blueprint(usuarios, url_prefix='/usuarios')
app.register_blueprint(cadastro_hospede, url_prefix='/cadastro_hospede')
app.register_blueprint(cadastro_quartos, url_prefix='/cadastro_quartos')
app.register_blueprint(menu, url_prefix='/menu')
app.register_blueprint(pedidos, url_prefix='/pedidos')
app.register_blueprint(residents, url_prefix='/residents')



Session(app)

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@login_manager.user_loader
def load_user(id):
    return db_session.query(Employee).filter_by(id=ord(id)).first()
