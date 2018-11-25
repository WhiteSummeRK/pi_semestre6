"""Modulo para criar os comandos de inicialização da aplicação."""
from flask_script import Manager
from sistema_hotel import app
from sistema_hotel.models.insertions import (insert_users,
                                             insert_rooms,
                                             insert_orders,
                                             insert_resident,
                                             insert_services,
                                             insert_employee,
                                             insert_resident_account,
                                             insert_category)

manager = Manager(app)


@manager.command
def runserver():
    app.run(debug=True)





runserver()
