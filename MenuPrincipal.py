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

        # botao que seleciona o método do Ponto Fixo
        self.executaPontoFixo = Button(master, text="Método do Ponto Fixo", command=self.MetodoPontoFixo)
        self.executaPontoFixo.config(height=2, width=15)
        self.executaPontoFixo.grid(row=3, column=1)

        #botão que seleciona o método de Gauss-Seidel
        self.executaGaussSeidel = Button(master, text="Método de Gauss-Seidel", command=self.MetodoGaussSeidel)
        self.executaGaussSeidel.config(height=2, width=15)
        self.executaGaussSeidel.grid(row=4,column=1)

        # botão que seleciona o método de Gauss-Jacobi
        self.executaGaussJacobi = Button(master, text="Método de Gauss-Seidel", command=self.MetodoGaussJacobi)
        self.executaGaussJacobi.config(height=2, width=15)
        self.executaGaussJacobi.grid(row=5, column=1)

    def Ajuda(self):
        texto_ajuda = 'Os métodos disponíveis são:                              \n' \
                      ' - Método de Newton                                       \n'\
                      ' - Método da Bisseção                                     \n'\
                      ' - Método do Ponto Fixo                                   \n' \
                      ' - Método de Gauss-Seidel                                  \n' \
                      ' - Método de Gauss-Jacobi                                   \n' \

        self.pop_up = Toplevel()
        self.label = Label(self.pop_up, text = texto_ajuda, height=12, width=60,font=("Fixedsys",12))
        self.label.pack(expand=True)

    def MetodoDeNewton(self):
        os.system('python3 MetodoDeNewton.py')

    def MetodoBissecao(self):
        os.system('python3 MetodoBissecao.py')

    def MetodoPontoFixo(self):
        os.system('python3 MetodoPontoFixo.py')

    def MetodoGaussSeidel(self):
        os.system('python3 MetodoGauss-Seidel.py')

    def MetodoGaussJacobi(self):
        os.system('python3 MetodoGauss-Jacobi.py')

principal = Tk()
menu = menuTrabalhoCG(principal)
principal.mainloop()