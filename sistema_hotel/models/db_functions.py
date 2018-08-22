from sistema_hotel.models.tables import session, User


def query_user(*, username: str, pwd: str):
    return session.query(User)\
        .filter_by(username=username, pwd=pwd).first()
