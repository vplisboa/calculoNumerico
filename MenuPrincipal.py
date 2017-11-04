from tkinter import *
import os
class menuTrabalhoCG:
    def __init__(self, master):
        self.master = master
        master.title("Trabalho de Cálculo Numérico 2017.2")

        #altera o tamanho do menu
        master.geometry("512x512")

        self.label = Label(master, text="Selecione o método numérico", font=("Fixedsys",16))
        self.label.grid(row=0, column=1)

        #frame para os poligonos
        self.frame = Frame(master)

        #botao que fecha o menu
        self.close_button = Button(master, text="Fechar", command=master.quit)
        self.close_button.config(width = 5)
        self.close_button.grid(row=5, column=3)

        #cria menu no topo da janela, com a label Ajuda
        self.principal = Menu(master)
        self.master.config(menu=self.principal)
        self.principal.add_command(label="Ajuda", command=self.Ajuda)

        #botao que seleciona o método de newton
        self.executaMetodoDeNewton = Button(master, text="Método de Newton", command=self.MetodoDeNewton)
        self.executaMetodoDeNewton.config(height=2, width=15)
        self.executaMetodoDeNewton.grid(row=1, column=1)

        # botao que seleciona o método da bisseção
        self.executaBissecao = Button(master, text="Método da Bisseção", command=self.MetodoBissecao)
        self.executaBissecao.config(height=2, width=15)
        self.executaBissecao.grid(row=2, column=1)

    def Ajuda(self):
        texto_ajuda = 'Os métodos disponíveis são:                              \n' \
                      ' - Método de Newton                                       \n'\
                      ' - Método da Bisseção                                     \n'\
                      '  - \'+\' : Adição                                         \n' \
                      '  - \'-\' : Subtração                                      \n' \
                      '  - \'/\' : Divisão                                         \n' \

        self.pop_up = Toplevel()
        self.label = Label(self.pop_up, text = texto_ajuda, height=12, width=60,font=("Fixedsys",12))
        self.label.pack(expand=True)

    def MetodoDeNewton(self):
        os.system('python3 MetodoDeNewton.py')

    def MetodoBissecao(self):
        os.system('python3 MetodoBissecao.py')

principal = Tk()
menu = menuTrabalhoCG(principal)
principal.mainloop()