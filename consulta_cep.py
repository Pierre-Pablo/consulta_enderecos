from traceback import print_tb
import requests
import json


print('=============================')
print('========CONSULTA CEP=========')
print('=============================')

uf = input('Informe o estado: ')
cidade = input('Informe a cidade: ')
logradouro = input('Informe o logradouro:')
dados = requests.get('https://viacep.com.br/ws/{}/{}/{}/json/'.format(uf, cidade, logradouro))
Cep = json.loads(dados.content)

for x in Cep:
    for y in x:
        if y == 'ibge' or y == 'gia' or y == 'siafi' or y == 'ddd' or y == 'complemento':
            continue
        print(f'{y}:{x.get(y)}')
        if y == 'cep':
            print('===================================================================')
