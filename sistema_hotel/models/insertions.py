from sistema_hotel.models.tables import session, User


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
