"""Modulo destinado a criação das tabelas do banco"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy import (
    create_engine,
    Column,
    Boolean,
    Integer,
    String,
    Date,
    Float,
    ForeignKey,
    UniqueConstraint,
    DateTime)
from sqlalchemy.orm import scoped_session, sessionmaker

db_url = 'postgres://hirronkobnwdgi:2fc41fb09b46120693deab8e4ebd311bdbe5a04d3b77587ed064de3f6d4a6c5c@ec2-23-23-153-145.compute-1.amazonaws.com:5432/d3f3tbmraot5nq'

db = SQLAlchemy()

class Resident(db.Model):
    """Tabela de Hospedes."""

    __tablename__ = 'resident'

    id_resident = Column(Integer, primary_key=True,
                         unique=True, autoincrement=True)
    username = Column(String(255), nullable=False)
    pwd = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    rg = Column(String(9), nullable=False)
    cpf = Column(String(11), nullable=False)
    phone = Column(String(11), nullable=False)

    def __repr__(self):
        """Alteração do __repr__ para representar os elementos da tabela."""
        return 'Resident(id_resident={}, \
                name={}, rg={}, cpf={}, phone={}'.format(
                     self.id_resident,
                     self.name,
                     self.rg,
                     self.cpf,
                     self.phone
                    )


class Category(db.Model):
    """Tabela de categorias."""

    __tablename__ = 'category'

    id_category = Column(Integer, primary_key=True,
                         unique=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)

    def __repr__(self):
        """Alteração do __repr__ para representar os elementos da tabela."""
        return 'Category(nome={}, descricao={})'.format(self.nome,
                                                        self.descricao)


class ResidentAccount(db.Model):
    """Tabela de contas dos hospedes."""

    __tablename__ = 'resident_account'

    id_account = Column(Integer, primary_key=True,
                        unique=True, autoincrement=True)
    id_resident = Column(Integer, ForeignKey('resident.id_resident'))
    id_room = Column(Integer, ForeignKey('room.id_room'))
    openned = Column(DateTime, nullable=False)
    closed = Column(DateTime, nullable=False)
    status = Column(String(255), nullable=False)
    value = Column(Float, nullable=False)

    def __repr__(self):
        """Alteração do __repr__ para representar os elementos da tabela."""
        return 'Category(id_account={}, id_resident={}, \
                openned={}, closed={}, status={}, value={})'.format(
                    self.id_account,
                    self.id_resident,
                    self.openned,
                    self.closed,
                    self.status,
                    self.value
                )


class Employee(db.Model):
    """Tabela de funcionarios."""

    __tablename__ = "employee"

    id = Column(Integer, primary_key=True,
                         unique=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    pwd = Column(String(255), nullable=False)
    rg = Column(String(9), nullable=False)
    cpf = Column(String(11), nullable=False)
    phone = Column(String(11), nullable=False)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return not is_authenticated()

    def get_id(self):
        return chr(self.id)

    def __repr__(self):
        """Alteração do __repr__ para representar os elementos da tabela."""
        return 'Employee(id={}, \
                name={}, pwd={}, rg={}, cpf={}, phone={})'.format(
                    self.id,
                    self.name,
                    self.pwd,
                    self.rg,
                    self.cpf,
                    self.phone
                )


class Room(db.Model):
    """Tabela de quartos."""

    __tablename__ = 'room'

    id_room = Column(Integer, primary_key=True,
                     unique=True, autoincrement=True)
    number = Column(Integer, nullable=False)
    floor = Column(Integer, nullable=False)
    description = Column(String(255), nullable=False)
    daily_value = Column(Float, nullable=False)
    status = Column(String(15), default='Livre', nullable=False)

    def __repr__(self):
        """Alteração do __repr__ para representar os elementos da tabela."""
        return 'Room(id_room={}, number={}, \
                floor={}, description={}, daily_value={}, status={})'.format(
                    self.id_room,
                    self.number,
                    self.floor,
                    self.description,
                    self.daily_value,
                    self.status
                )


class Service(db.Model):
    """Tabela de serviços."""

    __tablename__ = 'service'

    id_service = Column(Integer, primary_key=True,
                        unique=True, autoincrement=True)
    id_category = Column(Integer, ForeignKey('category.id_category'))
    id_employee = Column(Integer, ForeignKey('employee.id'))
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    image = Column(String(255), nullable=False)
    value = Column(Float, nullable=False)

    def __repr__(self):
        """Alteração do __repr__ para representar os elementos da tabela."""
        return 'Service(id_service={}, id_category={}, \
                id_employee={}, name={}, description={}, value={})'.format(
                    self.id_service,
                    self.id_category,
                    self.id_employee,
                    self.name,
                    self.description,
                    self.value,
                    self.image_url
                )


class Order(db.Model):
    """Tabela de Pedidos."""

    __tablename__ = "order"

    id_order = Column(Integer, primary_key=True,
                      unique=True, autoincrement=True)
    id_resident = Column(Integer, ForeignKey('resident.id_resident'))
    id_room = Column(Integer, ForeignKey('room.id_room'))
    date = Column(DateTime, default='0000-00-00', nullable=False)
    status = Column(String(255), nullable=False)
    total_value = Column(Float, nullable=False)

    def __repr__(self):
        """Alteração do __repr__ para representar os elementos da tabela."""
        return 'Order(id_order={}, id_resident={}, \
                id_room={}, date={}, status={}, \
                total_value={})'.format(
                    self.id_order,
                    self.id_resident,
                    self.id_room,
                    self.date,
                    self.status,
                    self.total_value
                )

class ItemOrder(db.Model):
    """Tabela de Items e pedidos."""

    __tablename__ = "item_order"

    id_item_order = Column(Integer, primary_key=True,
                           unique=True, autoincrement=True)
    id_order = Column(Integer, ForeignKey('order.id_order'))
    id_service = Column(Integer, ForeignKey('service.id_service'))
    id_employee = Column(Integer, ForeignKey('employee.id'))
    amount = Column(Integer, nullable=False)
    value = Column(Float, nullable=False)
    status = Column(String(255), nullable=False)

    def __repr__(self):
        """Alteração do __repr__ para representar os elementos da tabela."""
        return 'ItemOrder(id_order={}, id_service={}, \
                id_employee={}, amount={}, value={}, \
                status={})'.format(
                    self.id_order,
                    self.id_service,
                    self.id_employee,
                    self.amount,
                    self.value,
                    self.status
                )

engine = create_engine(db_url)
session = scoped_session(sessionmaker(bind=engine))
