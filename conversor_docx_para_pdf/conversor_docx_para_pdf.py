from os import path, listdir

# instalar a biblioteca docx2pdf: pip install docx2pdf
from docx2pdf import convert

# instalar a biblioteca tKinter: pip install tk
from tkinter import filedialog

pasta = filedialog.askdirectory()
caminho_pasta = path.join(pasta)
lista_arquivos = listdir()

if lista_arquivos and caminho_pasta:
    for item in range(len(lista_arquivos)):
        arquivo = lista_arquivos[item]
        cam_arquivo = caminho_pasta + '/' + arquivo
        convert(arquivo)
