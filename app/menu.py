""" 
Este módulo utiliza funções do módulo 'menu' para exibir o menu ao usuário. 
"""
import inquirer

from app.consulta import consultar_arquivo
from app.editar import editar_arquivo
from app.limpar import limpar_menu
def mostrar_menu():
    """
    Função para exibir o menu e lidar com a escolha do usuário
    """
    while True:
        perguntas = [
        inquirer.List('opcao',
                    message="O que você gostaria de fazer?",
                    choices=['Editar', 'Consultar', 'Sair'],
                    ),
        ]
        respostas = inquirer.prompt(perguntas)
        if respostas['opcao'] == 'Consultar':
            limpar_menu()
            consultar_arquivo()
        elif respostas['opcao'] == 'Editar':
            limpar_menu()
            editar_arquivo()
        elif respostas['opcao'] == 'Sair':
            limpar_menu()
            print("==================================================")
            print('')
            print('Até mais.....')
            print('')
            print("==================================================")
        break
