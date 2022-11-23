#    para a exportação para Microsof Excel estou usando o modulo pandas 
#    para instalar abra o prompt de comando do windows e digite: pip install pandas

import pandas as pd

# criação do DataFrame
dados = pd.DataFrame({'Codigo': [1, 2, 3, 4, 5, 6], 
    'Nome': ['Daniel', 'Vilma', 'Isabella', 'Denis', 'Edna', 'Maria'], 
    'Instagram': ['daniel.xds93', 'vilmanunes104', 'xaviier_13', 'aprendendo.doinicio', 
    'edna.apmacedo', 'aprendendo.doinicio']})

# a linha abaixo crio o nome do arquivo .xlsx
nome_xlsx = 'export_excel/usuarios_dados.xlsx'

# a linha abaixo seta a exportação para excel, passando o nome do arquivo, indexação e cabeçalho
dados.to_excel(nome_xlsx, index=False, header=True)
