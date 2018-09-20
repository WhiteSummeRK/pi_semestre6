from sistema_hotel.models.tables import session, User, Resident, Room, Service, ResidentAccount
from sqlalchemy import update


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

def query_resident_by_name(name):
    return session.query(Resident).filter_by(name=name).first()

def query_room_by_room_number(room_number):
    return session.query(Room).filter_by(number=room_number).first()

def create_new_account(*, resident, room, openned, closed, status, value):
    account = ResidentAccount(
    id_resident=resident,
    id_room=room,
    openned=openned,
    closed=closed,
    status=status,
    value=value
    )
    session.add(account)
    session.commit()
    return account

def update_room_state(room_number, updade_to):
    room_state = update(Room).where(Room.number==room_number).\
        values(status=updade_to)
    session.execute(room_state)
    session.commit()

def query_resident_by_room(room_number, resident_name):
    room = query_room_by_room_number(room_number)
    resident = query_resident_by_name(resident_name)

    user = session.query(ResidentAccount).filter_by(id_resident=resident.id_resident,
                                                    id_room=room.id_room).first()
    return user
