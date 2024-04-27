from art import *
import requests
import json

def menu():
    print(logo)
    print('[1] Consultar informações por CPF')
    print('[2] Consultar informações por CEP')
    print('[3] Consultar informações por PLACA')
    print('[4] Consultar informações por TELEFONE')

def get_cpf():
    cpf = input("Digite o CPF (somente números): ")
    url = f'https://f5search.com.br/search/serasa?access-key=0f9e4a06-d2de-4a25-b196-e56750656b36&cpf={cpf}'
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
    url = f'https://f5search.com.br/search/detran?access-key=0f9e4a06-d2de-4a25-b196-e56750656b36&placa={placa}'
    resposta = requests.get(url)
    resposta_json = resposta.json()
    print(json.dumps(resposta_json, indent=4, ensure_ascii=False))

def get_tel():
    tel = input("Digite o Telefone (somente números): ")
    url = f'https://f5search.com.br/search/serasa?access-key=0f9e4a06-d2de-4a25-b196-e56750656b36&telefone={tel}'
    resposta = requests.get(url)
    resposta_json = resposta.json()
    print(json.dumps(resposta_json, indent=4, ensure_ascii=False))


# Imprime o texto "Zzks" em letras grandes
tprint("Zzks Consultas")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀@Zzks7")

# Executa o loop de evento para executar as funções
while True:
    menu_opcao = input("Escolha uma opção (1 CONSULTAR CPF, 2 CONSULTAR CEP, 3 CONSULTAR PLACA, 4 CONSULTAR TELEFONE): ")

    if menu_opcao == '1':
        get_cpf()
    elif menu_opcao == '2':
        get_cep()
    elif menu_opcao == '3':
        get_placa()
    elif menu_opcao == '4':
        get_tel()

    else:
        print("Opção inválida. Tente novamente.")
