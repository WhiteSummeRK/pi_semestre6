from sistema_hotel.models.tables import session, User, Resident


def query_user(*, username: str, pwd: str):
    """Busca usuarios no banco de dados através do nome e senha"""
    return session.query(User)\
        .filter_by(username=username, pwd=pwd).first()

def save_resident(*, name: str, rg: str, cpf: str, phone: str):
    resident = Resident(
        name=name,
        rg=rg,
        cpf=cpf,
        phone=phone
    )
    session.add(resident)
    session.commit()
