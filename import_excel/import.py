#    para a importar arquivo do Microsof Excel estou usando o modulo pandas 
#    para instalar abra o prompt de comando do windows e digite: pip install pandas

#   para ler arquivo .xlsx é implementado o modulo openpyxl
#   para instalar abra o prompt de comando do windows e digite: pip install openpyxl

import pandas as pd

# a linha abaixo é a variavel que recebe o caminho e nome do arquivo a ser importado
nomeXlsx = "import_excel/arquivo.xlsx"

# a linha abaixo é a variavel que recebe as linhas e colunas do arquivo excel
# pd.read_excel() -> faz a leitura do arquivo 
dados = pd.read_excel(nomeXlsx, engine="openpyxl")

# aqui eu apenas mostro em tela os dados do arquivo
print(dados)
