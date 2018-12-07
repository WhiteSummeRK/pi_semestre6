"""Modulo para criar os comandos de inicialização da aplicação."""
from flask_script import Manager
from sistema_hotel import app
from sistema_hotel.models.insertions import (insert_rooms,
                                             insert_orders,
                                             insert_resident,
                                             insert_services,
                                             insert_employee,
                                             insert_resident_account,
                                             insert_category)

manager = Manager(app)


@manager.command
def runserver():
    app.run(debug=True, host="192.168.0.4", port=5000)

@manager.command
def insertions():
    insert_rooms()
    insert_category()
    insert_employee()
    insert_services()
    insert_resident()
    insert_resident_account()
    insert_orders()

@manager.command
def orders():
    insert_orders()

@manager.command
def rooms():
    insert_rooms()

if __name__ == '__main__':
    manager.run()

runserver()
