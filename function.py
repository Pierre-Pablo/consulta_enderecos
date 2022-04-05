import requests
import json

def busca_Cep(Cep):
    Cep = ''
    if len(Cep) != 8:
        print('Cep invalido!!')
        exit()

    else:
        dados = requests.get('https://viacep.com.br/ws/{}/json/'.format(Cep))
        num = input('Informe o numero: ')
        opc = input('Possui complemento: S/N ').lower()
        if opc == 's':
            cep_tratado = dados.json()
            complemento = input('Qual o complemento: ')
            Rua = cep_tratado["logradouro"]
            bairro = cep_tratado["bairro"]
            cidade = cep_tratado["localidade"]
            estado = cep_tratado["uf"]
            print(Rua, num, complemento, bairro, cidade, estado)
        
        elif opc == 'n':
            cep_tratado = dados.json()
            Rua = cep_tratado["logradouro"]
            bairro = cep_tratado["bairro"]
            cidade = cep_tratado["localidade"]
            estado = cep_tratado["uf"]
            print(Rua, num, bairro, cidade, estado)
        
        else:
            print('Opção invalida!')