# instalar o pacote fpdf: pip install fpdf
from os import path, listdir
from fpdf import FPDF
from tkinter import filedialog
import PySimpleGUI as sg

layout = [
    [sg.Text('Converter .txt para .pdf')],
    [sg.Button("Selecione a pasta")]
]

janela = sg.Window("Conversor", layout)
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    
    try:
        pasta = filedialog.askdirectory()
        caminho_pasta = path.join(pasta)
        lista_arquivos = listdir(pasta)

        def converter_para_pdf(file, nomePDF):

            pdf = FPDF()
            pdf.add_page()
                    
            for text in file:
                pdf.set_font("Arial",size=15) # For paragraph text
                pdf.cell(w=0,h=10,txt=f'{text}',align="L")
                nomePDF = caminho_pasta + "/" + nomePDF + '.pdf'
                pdf.output(nomePDF)   

        if lista_arquivos and caminho_pasta:
            for item in range(len(lista_arquivos)):
                arquivo = lista_arquivos[item]
                caminho_nome = caminho_pasta + "/" + arquivo
                nomePDF = arquivo.split('.')
                nomePDF = nomePDF[0]
                file = open(caminho_nome, "r")
                converter_para_pdf(file, nomePDF)
        
            sg.popup('Conversão concluída')
        else:
            sg.popup('Pasta informada, não possuem arquivos que possam ser convertidos.')

    except FileNotFoundError:
        pass