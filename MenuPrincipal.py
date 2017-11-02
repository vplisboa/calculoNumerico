from tkinter import *
import sys
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
        self.poligonos = Frame(master)

        #botao que fecha o menu
        self.close_button = Button(master, text="Fechar", command=master.quit)
        self.close_button.config(width = 5)
        self.close_button.grid(row=5, column=3)

        #cria menu no topo da janela, com a label Ajuda
        self.principal = Menu(master)
        self.master.config(menu=self.principal)
        self.principal.add_command(label="Ajuda", command=self.Ajuda)

        #variavel que salva a textura escolhida
        self.textura = StringVar(master)

        #botao que seleciona o cubo
        self.botao_cubo = Button(master, text="Método de Newton", command=self.Cubo)
        self.botao_cubo.config(height=2, width=15)
        self.botao_cubo.grid(row=1, column=1)

    def Ajuda(self):
        texto_ajuda = 'Para usar o programa, primeiro escolha um método numérico\n' \
                      ' Os operadores são:                                       \n'\
                      '  - \'*\' : Multiplicação                                  \n'\
                      '  - \'**\' : Potenciação                                   \n' \
                      '  - \'+\' : Adição                                         \n' \
                      '  - \'-\' : Subtração                                      \n' \
                      '  - \'/\' : Divisão                                         \n' \

        self.pop_up = Toplevel()
        self.label = Label(self.pop_up, text = texto_ajuda, height=12, width=60,font=("Fixedsys",12))
        self.label.pack(expand=True)

    def Cubo(self):
        os.system('python3 MetodoDeNewton.py')

principal = Tk()
menu = menuTrabalhoCG(principal)
principal.mainloop()