"""Modulo para criar os comandos de inicialização da aplicação."""
from flask_script import Manager
from sistema_hotel import app
from sistema_hotel.models.insertions import insert_users, insert_rooms

manager = Manager(app)


@manager.command
def runserver():
    app.run(debug=True)


@manager.command
def insertions():
    insert_users()
    insert_rooms()


if __name__ == '__main__':
    manager.run()
