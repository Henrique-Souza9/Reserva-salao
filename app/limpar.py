""" 
Este módulo limpa a tela do usuario. 
"""

import os

def limpar_menu():
    """
    Função para limpar
    """
    os.system('cls' if os.name == 'nt' else 'clear')