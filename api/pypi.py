import requests

# Referências sobre o uso do requests:
#
# Fazendo requisições:
# https://docs.python-requests.org/en/master/user/quickstart/#make-a-request
# Usando JSON retornado:
# https://docs.python-requests.org/en/master/user/quickstart/#json-response-content

def version_exists(package_name, version):
    # TODO
    # Fazer requisição na API do PyPI para checar se a versão existe
    
    try:
        r = requests.get('https://pypi.org/pypi/'+ package_name + '/json')
        rjson = r.json()
        versions = rjson["releases"].keys()
        
        if version in versions: return True
        else: return False
    except Exception as e:
        return "Erro funcao version_exists"


def latest_version(package_name):
    # TODO
    # Fazer requisição na API do PyPI para descobrir a última versão
    # de um pacote. Retornar None se o pacote não existir.    
    try:
        r = requests.get('https://pypi.org/pypi/'+ package_name + '/json')
        rjson = r.json()
        latversion = rjson["info"]["version"]  
        return latversion 
    except Exception as e:
        return "None"