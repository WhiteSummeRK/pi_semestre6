from sistema_hotel.models.tables import session, User, Room


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
