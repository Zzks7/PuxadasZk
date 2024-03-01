rom art import *
import requests
import json

def menu():
    print(logo)
    print('[1] Consultar informações por CPF')
    print('[2] Consultar informações por CEP')
    print('[3] Consultar informações por PLACA')

def get_cpf():
    cpf = input("Digite o CPF (somente números): ")
    url = f'https://apiconsultashk.azurewebsites.net/datasearch/api/cpf/{cpf}/pni'
    resposta = requests.get(url)
    resposta_json = resposta.json()
    print(json.dumps(resposta_json, indent=4, ensure_ascii=False))

def get_cep():
    cep = input("Digite o CEP (somente números): ")
    url = f'https://viacep.com.br/ws/{cep}/json/'
    resposta = requests.get(url)
    resposta_json = resposta.json()
    print(json.dumps(resposta_json, indent=4, ensure_ascii=False))

def get_placa():
    placa = input("Digite a PLACA: ")
    url = f'https://worldata.online/api?token=387a4560-4566-4f75-af1b-555c177a4fa3&type=placa&query={placa}'
    resposta = requests.get(url)
    resposta_json = resposta.json()
    print(json.dumps(resposta_json, indent=4, ensure_ascii=False))

# Imprime o texto "Zzks" em letras grandes
tprint("Zzks Consultas")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀@Zzks7")

# Executa o loop de evento para executar as funções
while True:
    menu_opcao = input("Escolha uma opção (1 CONSULTAR CPF, 2 CONSULTAR CEP, 3 CONSULTAR PLACA): ")

    if menu_opcao == '1':
        get_cpf()
    elif menu_opcao == '2':
        get_cep()
    elif menu_opcao == '3':
        get_placa()
    else:
        print("Opção inválida. Tente novamente.")
