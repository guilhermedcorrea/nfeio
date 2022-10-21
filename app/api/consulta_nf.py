from typing import Any
from flask import Blueprint, request, jsonify, make_response, Response, abort, current_app
from functools import wraps
import os
from dotenv import load_dotenv
import requests
from typing import Dict, Tuple, List
from ..extensions import db
from ..models.pedidos_hausz_mapa import PedidoFlexy
from ..models.cliente_hausz_mapa import EnderecoPedidos
from sqlalchemy import text
from datetime import datetime
from itertools import chain
from ..controllers.controllers_hausz_mapa import executa_select
from itertools import groupby


def register_handlers(app):
    if current_app.config.get('DEBUG') is True:
        current_app.logger.debug('Errors')
        return

    @current_app.errorhandler(404)
    def not_found_error(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

    @current_app.errorhandler(500)
    def internal_error(error):
        return make_response(jsonify({"Error":"internal error"}), 500)
    

    @current_app.errorhandler(500)
    def ModuleNotFoundError(*args, **kwargs):
        return make_response(jsonify({"Error":"internal error"}), 500)

    @current_app.errorhandler(404)
    def page_not_found(*args, **kwargs):
        return make_response(jsonify({"Error":"Endpoint NotFound"}), 404)
   
    @current_app.errorhandler(405)
    def method_not_allowed_page(*args, **kwargs):
        return make_response(jsonify({"Error":"Endpoint NotFound"}), 405)

consulta_bp = Blueprint('consultanf', __name__)
register_handlers(current_app)

from ..controllers.controllers_notas import get_metodo, list_all_empresas

"""
NOTA FISCAL CONSUMIDOR
"""
load_dotenv()



API_KEY_EMISSAO = os.getenv('API_KEY_EMISSAO')
COMPANY_ID_EMISSAO = os.getenv('COMPANY_ID_EMISSAO')


@get_metodo
def get_parametros(*args: tuple, **kwargs: Dict[str, Any]) -> None:
    """Docstring"""
    print('Called function')


@list_all_empresas
def get_list_empresas(*args: tuple, **kwargs: Dict[str, Any]) -> None:
    print("teste")


"""
Lista notas
https://nfe.io/docs/desenvolvedores/rest-api/nota-fiscal-de-consumidor-v2/#/
"""

@consulta_bp.route('/api/v2/companies/list/empresas/all', methods=['GET','POST'])
def listas_all_empresas() -> Response:
    try:
        jsons = get_list_empresas(api_key= API_KEY_EMISSAO)
        return make_response(jsonify(jsons)), 201
    except:
        abort(400)

@consulta_bp.route('/api/v2/companies/list/nfe/all', methods=['GET','POST'])
def consulta_nf():
    try:
        jsons = get_parametros(compani_id=COMPANY_ID_EMISSAO, api_key=API_KEY_EMISSAO)
        return make_response(jsonify(jsons))
    except:
        abort(400)
  

@consulta_bp.route('/api/v1/companies/consumerinvoices/<consumer_invoice_id>', methods=['GET','POST'])
def consultar_nf_id(consumer_invoice_id: str) -> Response:
    consumer_invoice_id = request.get_json()
    values = consumer_invoice_id['consumer_invoice_id']
    print(values)
    return jsonify({"Notas":values})
@consulta_bp.route('/api/v1/companies/consumerinvoices/<consumer_invoice_id>/items', methods=['GET','POST'])
def consultar_produtos_id_nf(consumer_invoice_id: str) -> Response:
    consumer_invoice_id = request.get_json()
    values = consumer_invoice_id['consumer_invoice_id']
    return jsonify({"Notas":values})
@consulta_bp.route('/api/v1/companies/consumerinvoices/<consumer_invoice_id>/events', methods=['GET','POST'])
def consultar_eventos_nf_id(consumer_invoice_id: str) -> Response:
    consumer_invoice_id = request.get_json()
    values = consumer_invoice_id['consumer_invoice_id']
    return jsonify({"Notas":values})
@consulta_bp.route('/api/v1/companies/consumerinvoices/<consumer_invoice_id>/xml', methods=['GET','POST'])
def consultar_xml_nf(consumer_invoice_id: str) -> Response:
    consumer_invoice_id = request.get_json()
    values = consumer_invoice_id['consumer_invoice_id']
    print(consumer_invoice_id)
    return jsonify({"Notas":values})
@consulta_bp.route('/api/v1/companies/consumerinvoices/<consumer_invoice_id>/rejeicao/xml', methods=['GET','POST'])
def consultar_xml_rejeicao_id(consumer_invoice_id: str) -> Response:
    consumer_invoice_id = request.get_json()
    values = consumer_invoice_id['consumer_invoice_id']
    print(values)
    return jsonify({"Notas":values})

