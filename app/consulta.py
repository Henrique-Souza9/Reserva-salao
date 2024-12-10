"""
Modulo consulta
"""
import pyexcel_ods3
import pandas as pd


# Função para consultar a planilha
def consultar_arquivo():
    """
    Função que consulta no arquivo libre office
    
    """
    data = pyexcel_ods3.get_data('base-de-dados.ods')

    sheet_names = data.keys()
    #print(sheet_names)  # Isso irá te ajudar a encontrar o nome correto da planilha

    df = pd.DataFrame(data[list(sheet_names)[0]])
    print(df.to_string())
