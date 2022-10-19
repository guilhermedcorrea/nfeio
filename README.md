

##cadastra_nf
```
Emissao notas ficais
https://nfe.io/docs/desenvolvedores/rest-api/nota-fiscal-de-produto-v2/#/
```

##consulta_nf
```
NOTA FISCAL CONSUMIDOR
```

##consulta_nf
```
Recebe nome da tabela como parametro pela função wraps


```
```python
exemplo

def get_metodo_nf(f):
    @wraps(f)
    def get_jestor_notafiscal(*args: tuple, **kwargs: Dict[str, Any]) -> Any:
        print(args, kwargs)
        print('Envia requisicao JESTOR CONSULTA | METODO GET')
        url = "https://supply.api.jestor.com/object/list"
        payload = {
        "object_type": f"{kwargs.get('tabela')}", #Nome da tabela
        "sort": "number_field desc",
        "page": 1,
        "size": "10"
        }
      
        response = requests.post(url, json=payload, headers=headers)
        return response.json()
```


##controllers_hausz
```
classe PedidosVendaHausz e HauszMapa Faz inserção de registros e logs
```

```python

class HauszMapa(ABC):
    def call_func_hausz_mapa(self): pass

class PedidosVendaHausz(HauszMapa):
    def __init__(self, dataatual):
        self.dataatual = dataatual

class NotasHausz:
    def __init__(self, pedido, data, unidade):
        self.pedido = pedido
        self.data = data
        self.unidade = unidade

```

##Wraper recebe e retorna jsons api jestor
```Python
API_KEY_JESTOR = os.getenv('API_KEY_JESTOR')

"""Ira substituir a função colocada no jestor.py"""
def api_get_jestor(f):
    @wraps(f)
    def get_jestor_notafiscal(*args: tuple, **kwargs: Dict[str, Any]) -> Any:
        print(args, kwargs)
        print('GET JESTOR | METODO GET')
        url = "https://supply.api.jestor.com/object/list"
        payload = {
        "object_type": f"{kwargs.get('tabela')}",
        "sort": "number_field desc",
        "page": 1,
        "size": "10"
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": f"{API_KEY_JESTOR}"
        }
    
        response = requests.post(url, json=payload, headers=headers)
        strs = response.json()
        try:
            for items in strs:
                dicts = strs[items]
                if isinstance(dicts, dict):
                    dict_items = dicts.get('items')
                    for values in dict_items:
                        if next(filter(lambda k: len(k) > 0, values), None):
                            dict_pedidos = {}
                            if type(values) == dict:
                                dict_pedidos.update(values)
                                yield dict_pedidos
                            else:
                                return "Error"
        except Exception as e:
            print("error", e)
```


```
Classe JestorHausz - Recebe parametros data, pedido, cliente, nf, estatus e tabela que são passados para o endpoint e fazem o filtro para retornar o json com as informações
```
## JestorHausz
```Python
class JestorHausz(Jestor):
    def __init__(self, data = None, pedido = None, cliente = None, nf = None
                 , status = None, tabela = None):
        self.data: datetime = data
        self.pedido: str = pedido
        self.cliente: str = cliente
        self.nf:int = nf
        self.status: str = status
        self.tabela: str = tabela
        self.cont: int = 0

```
