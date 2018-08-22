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
