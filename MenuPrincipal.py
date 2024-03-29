from tkinter import *
import os

class menuTrabalhoCG:
    def __init__(self, master):
        self.master = master
        master.title("Trabalho de Cálculo Numérico 2017.2")

        #altera o tamanho do menu
        master.geometry("550x550")

        self.label = Label(master, text="Selecione o método numérico", font=("Fixedsys",16))
        self.label.grid(row=0, column=1)

        #frame para os poligonos
        self.frame = Frame(master)

        #botao que fecha o menu
        self.close_button = Button(master, text="Fechar", command=master.quit)
        self.close_button.config(height=2,width = 8)
        self.close_button.grid(row=5, column=3)

        #cria menu no topo da janela, com a label Ajuda
        self.principal = Menu(master)
        self.master.config(menu=self.principal)
        self.principal.add_command(label="Sobre", command=self.Sobre)

        #botao que seleciona o método de newton
        self.executaMetodoDeNewton = Button(master, text="Método de Newton", command=self.MetodoDeNewton)
        self.executaMetodoDeNewton.config(height=3, width=27)
        self.executaMetodoDeNewton.grid(row=1, column=1)

        # botao que seleciona o método da bisseção
        self.executaBissecao = Button(master, text="Método da Bisseção", command=self.MetodoBissecao)
        self.executaBissecao.config(height=3, width=27)
        self.executaBissecao.grid(row=2, column=1)

        # botao que seleciona o método do Ponto Fixo
        self.executaPontoFixo = Button(master, text="Método do Ponto Fixo", command=self.MetodoPontoFixo)
        self.executaPontoFixo.config(height=3, width=27)
        self.executaPontoFixo.grid(row=3, column=1)

        #botão que seleciona o método de Gauss-Seidel
        self.executaGaussSeidel = Button(master, text="Método de Gauss-Seidel", command=self.MetodoGaussSeidel)
        self.executaGaussSeidel.config(height=3, width=27)
        self.executaGaussSeidel.grid(row=4,column=1)

        # botão que seleciona o método de Gauss-Jacobi
        self.executaGaussJacobi = Button(master, text="Método de Gauss-Jacobi", command=self.MetodoGaussJacobi)
        self.executaGaussJacobi.config(height=3, width=27)
        self.executaGaussJacobi.grid(row=5, column=1)

        # botão que seleciona o método da Integração Numérica
        self.executaIntegracaoNumerica = Button(master, text="Método da Integração Numérica", command=self.MetodoIntegracaoNumerica)
        self.executaIntegracaoNumerica.config(height=3, width=27)
        self.executaIntegracaoNumerica.grid(row=6, column=1)

        # botão que seleciona o método da Integração Numérica
        self.executaGradienteDescendente = Button(master, text="Método do Gradiente Descendente",
                                                command=self.MetodoGradienteDescendente)
        self.executaGradienteDescendente.config(height=3, width=27)
        self.executaGradienteDescendente.grid(row=7, column=1)

        # botão que seleciona o método de Euler
        self.executaEuler = Button(master, text="Método de Euler",
                                                  command=self.MetodoEuler)
        self.executaEuler.config(height=3, width=27)
        self.executaEuler.grid(row=8, column=1)

    def Sobre(self):
        texto_ajuda = 'Trabalho da disciplina de Cálculo Numérico           \n' \
                      'Author: Victor Pedro Rodrigues Lisboa                \n' \
                      'Objetivo: criar um programa que permitisse a execução\n' \
                      '          de diversos métodos numéricos e mostrasse os\n' \
                      '          resultados obtidos' \

        self.pop_up = Toplevel()
        self.label = Label(self.pop_up, text = texto_ajuda, height=12, width=60,font=("Fixedsys",12))
        self.label.pack(expand=True)

    def MetodoDeNewton(self):
        os.system('python3 Metodos/MetodoDeNewton.py')

    def MetodoBissecao(self):
        os.system('python3 Metodos/MetodoBissecao.py')

    def MetodoPontoFixo(self):
        os.system('python3 Metodos/MetodoPontoFixo.py')

    def MetodoGaussSeidel(self):
        os.system('python3 Metodos/MetodoGauss-Seidel.py')

    def MetodoGaussJacobi(self):
        os.system('python3 Metodos/MetodoGauss-Jacobi.py')

    def MetodoIntegracaoNumerica(self):
        os.system('python3 Metodos/MetodoIntegracaoNumerica.py')

    def MetodoGradienteDescendente(self):
        os.system('python3 Metodos/MetodoGradienteDescendente.py')

    def MetodoEuler(self):
        os.system('python3 Metodos/MetodoEuler.py')

principal = Tk()
menu = menuTrabalhoCG(principal)
principal.mainloop()