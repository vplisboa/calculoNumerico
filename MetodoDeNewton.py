from tkinter import *
import sys
import os
from sympy import *

class menuTrabalhoCG:
    def __init__(self, master):
        self.master = master
        master.title("Método de Newton")

        #altera o tamanho do menu
        master.geometry("780x512")

        self.label = Label(master, text="Insira os parâmetros:", font=("Fixedsys",16))
        self.label.grid(row=0, column=1)

        #frame para os poligonos
        self.poligonos = Frame(master)

        #botao que fecha o menu
        self.close_button = Button(master, text="Fechar", command=master.quit)
        self.close_button.config(width = 5)
        self.close_button.grid(row=5, column=2)

        #cria menu no topo da janela, com a label Ajuda
        self.principal = Menu(master)
        self.master.config(menu=self.principal)
        self.principal.add_command(label="Ajuda", command=self.Ajuda)

        self.labelEquacao = Label(master, text="Insira a equação:", font=("Fixedsys", 12))
        self.labelEquacao.grid(row=1, column=1)
        self.equacaoInicial = StringVar()
        self.campoEquacaoInicial = Entry(master, textvar=self.equacaoInicial)
        self.campoEquacaoInicial.grid(row=2, column=1)

        #chute inicial
        self.labelChuteInicial = Label(master, text="Insira o chute inicial", font=("Fixedsys", 12))
        self.labelChuteInicial.grid(row=3, column=1)
        self.chuteInicial = IntVar()
        self.campoChuteInicial = Entry(master, textvar = self.chuteInicial)
        self.campoChuteInicial.grid(row=4, column=1)

        #erro desejado
        self.labelErro = Label(master, text="Insira o erro desejado", font=("Fixedsys", 12))
        self.labelErro.grid(row=5, column=1)
        self.erroDesejado = StringVar()
        self.campoErroDesejado = Entry(master, textvar=self.erroDesejado)
        self.campoErroDesejado.grid(row=6, column=1)

        #executa o método de newton
        self.botao_cubo = Button(master, text="Calcular", command=self.MétodoDeNewton)
        self.botao_cubo.config(height=2, width=15)
        self.botao_cubo.grid(row=5, column=3)

        self.observacao = Label(master, text="A derivada é calcula em função de x", fg="red",font=("Fixedsys", 12))
        self.observacao.grid(row=6, column=3)

    def Ajuda(self):
        texto_ajuda = 'Ajuda do método de newton'
        self.pop_up = Toplevel()
        self.label = Label(self.pop_up, text = texto_ajuda, height=12, width=60,font=("Fixedsys",12))
        self.label.pack(expand=True)

    def MétodoDeNewton(self):
        valorAnterior = self.chuteInicial.get()

        proximoValor = valorAnterior - self.f(valorAnterior)/self.fDerivada(valorAnterior)
        print(proximoValor)

    def f(self,valor):
        x = valor
        equacao = eval('\'' + self.equacaoInicial.get() + '\'')
        return eval(equacao)

    def fDerivada(self,valor):
        equacao = eval('\'' + self.equacaoInicial.get() + '\'')
        derivada = str(diff(equacao, 'x'))
        x = valor
        return eval(derivada)

principal = Tk()
menu = menuTrabalhoCG(principal)
principal.mainloop()