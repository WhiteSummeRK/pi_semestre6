"""Modulo para as rotas de login."""
from flask import (
    Blueprint,
    jsonify,
)
from sistema_hotel.models.db_functions import query_services_names

app = Blueprint('service', __name__)

@app.route('/api_service', methods=['GET'])
def services():
    result = {}
    service = query_services_names()
    for item in service:
        result.update(
            {item.id_service: {'id_employee': item.id_employee, 'name': item.name, 'description': item.description}})
    return jsonify(result)

