from sistema_hotel.models.tables import (session,
                                         Resident,
                                         Room,
                                         Employee,
                                         Service,
                                         ResidentAccount,
                                         Order,
                                         ItemOrder)
from datetime import datetime
from sqlalchemy import update

def query_insert_order(json):
    for item in json['service']:
        order = Order(
            id_resident=int(json['id_resident']),
            id_room=int(json['id_room']),
            date=str(datetime.datetime.utcnow()),
            status='0',
            total_value=float(item['unit_value'])
        )
        session.add(order)
        session.commit()
        session.query_property()
        item_order = ItemOrder(
        id_order =order.id_order,
        id_service = int(item['id_service']),
        id_employee = 1,
        amount = str(item['qtde']), #parabéns pra quem modelou isso como varchar no banco
        value =int(item['unit_value'])*float(item['qtde']),
        status = 0)
        session.add(item_order)
        session.commit()
        session.query_property()

def query_employee(*, name: str, pwd: str):
    """Busca usuarios no banco de dados através do nome e senha"""
    return session.query(Employee)\
        .filter_by(name=name, pwd=pwd).first()



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


def save_resident(*, name: str, rg: str, cpf: str, phone: str, username: str, pwd: str):
    try:
        resident = Resident(
            username=username,
            name=name,
            rg=rg,
            cpf=cpf,
            phone=phone,
            pwd=pwd
        )
        session.add(resident)
        session.commit()
    except Exception as e:
        session.rollback()


def save_employee(*, name: str, pwd: str, rg: str, cpf: str, phone: str):
        try:
            employee = Employee(
                name=name,
                pwd=pwd,
                rg=rg,
                cpf=cpf,
                phone=phone
            )
            session.add(employee)
            session.commit()
        except Exception as e:
            session.rollback()


def query_all_residents():
    return session.query(Resident).all()


def query_all_employees():
    return session.query(Employee).all()


def query_all_rooms():
    return session.query(Room).all()


def query_all_free_rooms():
    return session.query(Room).filter_by(status='Livre').all()


def query_all_busy_rooms():
    return session.query(Room).filter_by(status='Ocupado').all()


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
    room_state = update(Room).where(Room.number == room_number).\
        values(status=updade_to)
    session.execute(room_state)
    session.commit()


def query_all_resident_accounts():
    return session.query(ResidentAccount).all()

def query_resident_account_by_room_id(id):
    return session.query(ResidentAccount).filter(ResidentAccount.id_room == id, ResidentAccount.status == "Aberto").first()


def update_account_status(id, new_status):
    state = update(ResidentAccount).where(ResidentAccount.id_account == id).\
        values(status=new_status)
    session.execute(state)
    session.commit()

def do_checkout_date(id):
    date = update(ResidentAccount).where(ResidentAccount.id_account == id).\
        values(closed=datetime.now())
    session.execute(date)
    session.commit()


def reset_account_value(id):
    reseted = update(ResidentAccount).where(ResidentAccount.id_account == id).\
        values(value=0.0)
    session.execute(reseted)
    session.commit()


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
        .join(Service,Service.id_service==ItemOrder.id_service).filter(Order.id_resident==id_user).filter(Order.status != '3').all()
    return value

def service_status(id_user,id_room):
    value = session.query(Order.id_order,Order.total_value,Order.date,Order.status,ItemOrder.amount,ItemOrder.value,
                          Service.name,Service.id_service,Service.description).join(ItemOrder,
                                                                                    Order.id_order==ItemOrder.id_order)\
        .join(Service,Service.id_service==ItemOrder.id_service).filter(Order.id_resident==id_user).filter(Order.id_room==id_room).all()
    return value


def query_resident_by_id(id):
    return session.query(Resident).filter_by(id_resident=id).first()


def query_all_orders(amount):
    return session.query(Order).limit(int(amount)).all()


def query_order_by_id(id):
    return session.query(Order).filter_by(id_order=id).first()


def query_specific_status_orders(status, amount):
    return session.query(Order).filter_by(status=status).limit(int(amount)).all() # NOQA


def update_order_status(id, new_status):
    state = update(Order).where(Order.id_order == id).\
        values(status=new_status)
    session.execute(state)
    session.commit()
