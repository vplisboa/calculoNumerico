from tkinter import *
import sys
import os

from pyanaconda.iutil import get_active_console
from sympy import *
from decimal import *

class menuTrabalhoCG:
    def __init__(self, master):
        self.master = master
        master.title("Método de Newton")

        #altera o tamanho do menu
        master.geometry("720x360")

        self.label = Label(master, text="Insira os parâmetros:", font=("Fixedsys",16))
        self.label.grid(row=0, column=1)

        #frame para os poligonos
        self.poligonos = Frame(master)

        #botao que fecha o menu
        self.close_button = Button(master, text="Fechar", command=master.quit)
        self.close_button.config(width = 2)
        self.close_button.grid(row=14, column=2)

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
        self.chuteInicial = StringVar()
        self.campoChuteInicial = Entry(master, textvar = self.chuteInicial)
        self.campoChuteInicial.grid(row=4, column=1)

        #Insira o numero de casas decimais de erro
        self.labelErro = Label(master, text="Insira o erro desejado", font=("Fixedsys", 12))
        self.labelErro.grid(row=5, column=1)
        self.erroDesejado = IntVar()
        self.campoErroDesejado = Entry(master, textvar=self.erroDesejado)
        self.campoErroDesejado.grid(row=6, column=1)

        #Campo que mostra os passos até a resposta ser encontrada
        self.labelPassos = Label(master,text="Quantidade de Passos: ",font=("Fixedsys", 12))
        self.labelPassos.grid(row=10, column=1)

        #Campo que mostra o resultado final
        self.labelResultado = Label(master,text="Resposta Final: ",font=("Fixedsys", 12))
        self.labelResultado.grid(row=11, column=1)

        #executa o método de newton
        self.botao_cubo = Button(master, text="Calcular", command=self.MétodoDeNewton)
        self.botao_cubo.config(height=2, width=10)
        self.botao_cubo.grid(row=13, column=2)

        self.observacao = Label(master, text="A derivada é calcula em função de x", fg="red",font=("Fixedsys", 12))
        self.observacao.grid(row=0, column=2)

    def Ajuda(self):
        texto_ajuda = 'Para inserir a equação utilize os seguintes operadores     \n'\
                      '  - \'*\' : Multiplicação                                  \n'\
                      '  - \'**\' : Potenciação                                   \n' \
                      '  - \'+\' : Adição                                         \n' \
                      '  - \'-\' : Subtração                                      \n' \
                      '  - \'/\' : Divisão                                         \n' \

        self.pop_up = Toplevel()
        self.label = Label(self.pop_up, text = texto_ajuda, height=12, width=60,font=("Fixedsys",12))
        self.label.pack(expand=True)

    def MétodoDeNewton(self):
        valorAnterior = eval(self.chuteInicial.get())
        proximoValor = valorAnterior - self.f(valorAnterior)/self.fDerivada(valorAnterior);

        a= self.erroDesejado.get()
        b = '%.'+ str(a) +'f'
        passos = 1

        while(b % proximoValor != b % valorAnterior):
            valorAnterior = proximoValor
            proximoValor = valorAnterior - self.f(valorAnterior) / self.fDerivada(valorAnterior);
            passos += 1

        self.labelResultado.config(text = 'Resultado Final: '+str(proximoValor))
        self.labelPassos.config(text='Quantidade de Passos: '+ str(passos))

    def f(self,valor):
        x = valor
        equacao = eval('\'' + self.equacaoInicial.get() + '\'')
        return eval(equacao)

    def fDerivada(self,valor):
        equacao = eval('\'' + self.equacaoInicial.get() + '\'')
        x = valor
        derivada = str(diff(equacao, 'x'))
        return eval(derivada)

principal = Tk()
menu = menuTrabalhoCG(principal)
principal.mainloop()