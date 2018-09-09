from sistema_hotel.models.tables import session, User, Resident, Room, Service


def query_user(*, username: str, pwd: str):
    """Busca usuarios no banco de dados através do nome e senha"""
    return session.query(User)\
        .filter_by(username=username, pwd=pwd).first()

def query_services_names():
    """Retorna dados dos serviços cadastradps"""
    return session.query(Service).all()

def save_resident(*, name: str, rg: str, cpf: str, phone: str):
    resident = Resident(
        name=name,
        rg=rg,
        cpf=cpf,
        phone=phone
    )
    session.add(resident)
    session.commit()

def query_all_residents():
    return session.query(Resident).all()

def query_all_rooms():
    return session.query(Room).all()

def update_room_state(room_number, updade_to):
    update(Room).where(number=room_number).\
        values(status=updade_to)
