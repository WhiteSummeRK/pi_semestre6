from sistema_hotel.models.tables import (session,
                                         User,
                                         Resident,
                                         Room,
                                         Service,
                                         ResidentAccount,
                                         Order,
                                         ItemOrder)
from sqlalchemy import update,join


def query_user(*, username: str, pwd: str):
    """Busca usuarios no banco de dados através do nome e senha"""
    return session.query(User)\
        .filter_by(username=username, pwd=pwd).first()

def query_resident(*, username: str, pwd: str):
    result = ''
    try:
        result = session.query(Resident.id_resident,Resident.name,Resident.username,Resident.pwd,Room.description,
                               Room.number,Room.id_room,Room.floor,Room.daily_value).join(ResidentAccount,
                                                                                          Resident.id_resident==ResidentAccount.id_resident).\
            join(Room,Room.id_room==ResidentAccount.id_room).filter(Resident.username==username,Resident.pwd==pwd).first()
    except Exception as e:
        print(e)
    return result

def query_services_names():
    """Retorna dados dos serviços cadastradps"""
    return session.query(Service).all()

def save_resident(*, name: str, rg: str, cpf: str, phone: str, username: str):
    try:
        resident = Resident(
            username=username,
            name=name,
            rg=rg,
            cpf=cpf,
            phone=phone,
        )
        session.add(resident)
        session.commit()
    except Exception as e:
        session.rollback()

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
    id_resident=resident.id_resident,
    id_room=room.id_room,
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

def query_all_resident_accounts():
    return session.query(ResidentAccount).all()

def query_room_by_id(room_id):
    return session.query(Room).first()

def query_resident_by_room(room_number, resident_name):
    room = query_room_by_room_number(room_number)
    resident = query_resident_by_name(resident_name)

    user = session.query(ResidentAccount).filter_by(id_resident=resident.id_resident,
                                                    id_room=room.id_room).first()
    return user

def query_outstanding(id_user):
    value = session.query(Order.id_order,Order.total_value,Order.date,Order.status,ItemOrder.amount,ItemOrder.value,
                          Service.name,Service.id_service,Service.description).join(ItemOrder,
                                                                                    Order.id_order==ItemOrder.id_order)\
        .join(Service,Service.id_service==ItemOrder.id_service).filter(Order.id_resident==id_user).all()
    return value


def query_resident_by_id(id):
    return session.query(Resident).filter_by(id_resident=id).first()

def query_all_orders():
    return session.query(Order).all()
