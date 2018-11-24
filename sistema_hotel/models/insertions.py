from datetime import datetime

from sistema_hotel.models.tables import session, Room, Service, \
    Category, Employee, Order, Resident, ResidentAccount, ItemOrder


def insert_rooms():
    room1 = Room(
        number=12,
        floor=1,
        description="Quarto do primeiro andar",
        daily_value=120.90,
        status='Livre'
    )

    session.add(room1)
    session.commit()

    room2 = Room(
        number=13,
        floor=1,
        description="Quarto do segundo andar",
        daily_value=110.90,
        status='Livre'
    )

    session.add(room2)
    session.commit()

    room3 = Room(
        number=14,
        floor=1,
        description="Quarto do primeiro andar",
        daily_value=23.90,
        status='Livre'
    )

    session.add(room3)
    session.commit()


def insert_services():
    service = Service(
        id_category=1,
        id_employee=1,
        name='coca cola',
        description='beba uma cocacola e seja feliz para sempre',
        value=500,
        image ='teste'
    )

    session.add(service)
    session.commit()


def insert_category():
    category = Category(
        name='comida',
        description='nada além disso, estamos todos com fome, então vamos comer'
    )
    session.add(category)
    session.commit()


def insert_employee():
    employe = Employee(
        name='WhiteSummeRK',
        cpf='4605552220',
        rg='475294403',
        phone='19989648989',
        pwd='123',
    )
    session.add(employe)
    session.commit()


def insert_resident():
    resident = Resident(
        name='Kauan',
        rg='45646545',
        cpf='123132',
        phone='465465',
        username='WhiteSummeRK',
        pwd='123',
    )
    session.add(resident)
    session.commit()

def insert_resident_account():
    resident_account = ResidentAccount(
    id_resident=1,
    id_room = 1,
    openned = '2018-05-12',
    closed = '2018-05-12',
    status = 'a',
    value = 200

    )
    session.add(resident_account)
    session.commit()


def insert_orders():
    pedido1 = Order(
        id_resident=1,
        id_room=1,
        date=datetime.now(),
        status='0',
        total_value=199.00
    )
    session.add(pedido1)
    session.commit()

    pedido2 = Order(
        id_resident=1,
        id_room=1,
        date=datetime.now(),
        status='1',
        total_value=199.00
    )
    session.add(pedido2)
    session.commit()

    pedido3 = Order(
        id_resident=1,
        id_room=1,
        date=datetime.now(),
        status='2',
        total_value=199.00
    )
    session.add(pedido3)
    session.commit()
