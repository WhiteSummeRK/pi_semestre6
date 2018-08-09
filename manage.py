"""Modulo para criar os comandos de inicialização da aplicação."""
from flask_script import Manager
from sistema_hotel import app

manager = Manager(app)


@manager.command
def runserver():
    app.run(debug=True)


if __name__ == '__main__':
    manager.run()
