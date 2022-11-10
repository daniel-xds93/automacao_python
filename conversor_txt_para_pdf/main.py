# instalar o pacote fpdf: pip install fpdf
from os import path, listdir
from fpdf import FPDF
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


class Tela:
    def __init__(self):
        
        self.layout = Tk()
        
        self.parteCima = Frame(self.layout)
        self.parteBaixo = Frame(self.layout)

        self.txtInformativo = Label(self.parteCima, text="Conversor de .txt para .pdf:")

        self.btnSelPasta = Button(self.parteBaixo, text="Selecionar pasta", command=self.executar)

        self.parteCima.pack()
        self.parteBaixo.pack()
        self.txtInformativo.pack(anchor = "w")
        self.btnSelPasta.pack(anchor = "w")

        mainloop()

        # janela = self.Window("Conversor", layout)
    def executar(self):
        
        try:
            pasta = filedialog.askdirectory()
            caminho_pasta = path.join(pasta)
            lista_arquivos = listdir(pasta)

            def converter_para_pdf(file, nomePDF):

                pdf = FPDF()
                pdf.add_page()

                arquivo_res = file
                        
                for text in arquivo_res:
                    pdf.set_font("Arial",size=12) # For paragraph text
                    pdf.cell(w=0,h=10,txt=f'{text}', ln=1, align="L")
                    
                nomePDF = caminho_pasta + "/" + nomePDF + '.pdf'
                
                pdf.output(nomePDF)   

            if lista_arquivos and caminho_pasta:
                for item in range(len(lista_arquivos)):
                    arquivo = lista_arquivos[item]
                    caminho_nome = caminho_pasta + "/" + arquivo
                    nomePDF = arquivo.split('.')
                    if len(nomePDF) <= 1:
                        continue
                    nomePDF = nomePDF[0]
                    file = open(caminho_nome, "r")
                    converter_para_pdf(file, nomePDF)
            
                messagebox.showinfo('Concluído', "Conversão concluída")
            else:
                messagebox.showerror('Atenção','Pasta informada, não possuem arquivos que possam ser convertidos.')

        except FileNotFoundError:
            pass

tl = Tela()
