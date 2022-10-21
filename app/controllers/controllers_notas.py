from functools import wraps
import os
from dotenv import load_dotenv
import requests
import json
from typing import Dict, Tuple, List, Any

"""
NOTA FISCAL CONSUMIDOR

"""
load_dotenv()

API_KEY_EMISSAO = os.getenv('API_KEY_EMISSAO')
COMPANY_ID_EMISSAO = os.getenv('COMPANY_ID_EMISSAO')

def get_metodo(f) -> Any:
    @wraps(f)
    def obtem_endpoint(*args: tuple, **kwargs: Dict[str, Any]) -> Any:
        print('Envia requisicao NFE IO CONSULTA | METODO GET')

        '''
        url = """https://api.nfse.io/v2/companies/{}/productinvoices?environment=production&apikey={}""".format(kwargs.get('compani_id'), kwargs.get('api_key'))
        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.status_code)
        jsons = response.json()
        '''

        #return jsons
        return (kwargs.get('CodigoPedido'))
        
    return obtem_endpoint

def emissao_nfe(f) -> Any:
    @wraps(f)
    def emissao_notas_fiscais(*args: tuple, **kwargs: Dict[str, Any]) -> Any:

        print('emissao notas fiscais ')

        url = """https://api.nfse.io/v2/companies/{COMPANY_ID_EMISSAO}/productinvoices/""".format(COMPANY_ID_EMISSAO)

        payload = json.dumps({
        "buyer": {
            "name": "{}","tradeName": "{}","address": {"city": {"code": "{}","name": "{}"
            },"state": "SP","district": "distrito","street": "Alameda Madri","postalCode": "{}","number": "{}","country": "{}"},
            "federalTaxNumber": {}
        },
        "items": [{"code": "{}","unitAmount": {},"quantity": {},"cfop": {}, "ncm": "{}","codeGTIN": "{}",
            "codeTaxGTIN": "{}","tax": {"totalTax": {},"icms": {"csosn": "{}","origin": "{}"},"pis": { "amount": {},"rate": {},"baseTax": {}, "cst": "{}"
                },"cofins": {"amount": {},"rate": {},"baseTax": {},"cst": "{}"}},"cest": "","description": "{}"
            }]}).format()
        headers = {
        'Authorization': f'{API_KEY_EMISSAO}',
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.status_code)
 
        return response.json()
        
    return emissao_notas_fiscais


@get_metodo
def get_parametros(*args: tuple, **kwargs: Dict[str, Any]) -> None:
    """Docstring"""
    print('Called function')


def list_all_empresas(f) -> Any:
    @wraps(f)
    def obtem_endpoint(*args: tuple, **kwargs: Dict[str, Any]) -> Any:

        print('Envia requisicao NFE IO CONSULTA | METODO GET')
      

        url = "https://api.nfse.io/v2/companies?apikey={}".format(kwargs.get('api_key'))


        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.status_code)
        jsons = response.json()

        return jsons
        
    return obtem_endpoint


class NotasHausz:
    def __init__(self, pedido, data, unidade, nf):
        self.pedido = pedido
        self.data = data
        self.unidade = unidade
        self.lista_dicts = []

    def seleciona_fields(self, *args: tuple, **kwargs: dict[str, Any]) -> dict[str, Any]:pass

    def get_jsons_api(self): pass

    def emissao_nf(self) -> None: pass

       

        