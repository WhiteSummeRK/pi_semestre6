"""Modulo para as rotas de login."""
from flask import (
    Blueprint,
    jsonify,
    request
)
from sistema_hotel.models.db_functions import query_services_names,query_outstanding

app = Blueprint('service', __name__)

@app.route('/api_service', methods=['PosT'])
def services():
    result = {}
    service = query_services_names()
    for item in service:
        result.update(
            {item.id_service: {'id_employee': item.id_employee,
                               'name': item.name, 'description':
                                   item.description,'value':item.value}})
    return jsonify(result)


@app.route('/outstanding_balance', methods=['POST'])
def outstanding():
    result = {}
    request.form.get('id_resident')
    service = query_outstanding()
    for item in service:
        result.update(
            {item.id_service: {'id_employee': item.id_employee,
                               'name': item.name, 'description':
                                   item.description,'value':item.value}})
    return jsonify(result)
