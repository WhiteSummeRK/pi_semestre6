"""Modulo para as rotas de login."""
from flask import (
    Blueprint,
    jsonify,
    request
)
from sistema_hotel.models.db_functions import (query_services_names,
                                               query_outstanding,
                                               service_status,
                                               query_insert_order,
                                               update_account_value,
                                               query_resident_account_by_room_id)

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
                               'qtde':item.amount,'id_service':item.id_service}})
    return jsonify(result)


@app.route('/service_status', methods=['POST'])
def status():
    result = {}
    id_resident = request.form.get('id_resident')
    id_room = request.form.get('id_room')

    service = service_status(id_resident,id_room)
    for item in service:
        result.update(
            {item.id_order: {'total_value': item.total_value,
                               'name': item.name,'value':item.value,
                               'date':item.date,'status':item.status,
                               'qtde':item.amount,'id_service':item.id_service}})
    return jsonify(result)


@app.route('/insert_order', methods=['POST'])
def insert_order():
    result = {}
    account = query_resident_account_by_room_id(request.json['id_room'])
    try:
        content_order = request.json
        order_cost = content_order['orderCost']
        update_account_value(account.id_account, order_cost)

        query_insert_order(content_order)
        return jsonify({'status':True})
    except:
        return jsonify({'status':False})
