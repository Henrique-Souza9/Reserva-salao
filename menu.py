import inquirer
from consulta import consultar_arquivo
from editar import editar_arquivo
from limpar import limpar_menu

# Função para exibir o menu e lidar com a escolha do usuário
def mostrar_menu():
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

