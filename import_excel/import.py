#    para a importar arquivo do Microsof Excel estou usando o modulo pandas 
#    para instalar abra o prompt de comando do windows e digite: pip install pandas

#   para ler arquivo .xlsx é implementado o modulo openpyxl
#   para instalar abra o prompt de comando do windows e digite: pip install openpyxl

import pandas as pd

nomeXlsx = ""

dados = pd.read_excel(nomeXlsx, engine="openpyxl")

print(dados)
