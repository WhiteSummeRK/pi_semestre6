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
            {item.id_service: {
                               'name': item.name, 'description':
                                   item.description,'value':item.value,'cover_img':item.image}})
    return jsonify(result)


@app.route('/outstanding_balance', methods=['POST'])
def outstanding():
    result = {}
    id_resident = request.form.get('id_resident')
    service = query_outstanding(id_resident)
    for item in service:
        result.update(
            {item.id_order: {'total_value': item.total_value,
                               'name': item.name, 'description':
                                   item.description,'value':item.value,
                               'date':item.date,'status':item.status,
                               'amount':item.amount,'id_service':item.id_service}})
    return jsonify(result)
