"""Modulo para as migrações do banco."""

from sistema_hotel.models.tables import manager


if __name__ == '__main__':
    manager.run()
