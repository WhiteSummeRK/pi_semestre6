from sistema_hotel.models.tables import session, User, Room, Service, \
    Category, Employee, Order, Resident


def insert_users():
    kauan = User(
        username='WhiteSummeRK',
        pwd='123',
        name='Kauan Alves',
        is_adm=True,
        activity=True
    )
    session.add(kauan)
    session.commit()

    hospede01 = User(
        username='Hospede01',
        pwd='123',
        name='Hospede 01',
        is_adm=False,
        activity=False
    )
    session.add(hospede01)
    session.commit()


def insert_rooms():
    room1 = Room(
        number=10,
        floor=1,
        description="Quarto do primeiro andar",
        daily_value=89.90,
        status='Livre'
    )

    session.add(room1)
    session.commit()

    room2 = Room(
        number=20,
        floor=1,
        description="Quarto do primeiro andar",
        daily_value=89.90,
        status='Livre'
    )

    session.add(room2)
    session.commit()

    room3 = Room(
        number=30,
        floor=1,
        description="Quarto do primeiro andar",
        daily_value=89.90,
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
        value=500
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
        nome='Jaime Ossada',
        cpf='4605552220',
        cargo='Cozinheiro',
        setor='Cozinha'
    )
    session.add(employe)
    session.commit()


def insert_order():
    order = Order(
        id_resident=1,
        id_room=1,
        date='2018-05-12',
        status='a',
        total_value='1000'
    )
    session.add(order)
    session.commit()


def insert_resident():
    resident = Resident(
        name='Kauan',
        rg='45646545',
        cpf='123132',
        phone='465465'
    )
    session.add(resident)
    session.commit()