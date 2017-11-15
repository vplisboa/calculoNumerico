from tkinter import *
import numpy as np

#caso de teste A = [[4.0, -2.0, 1.0], [1.0, -3.0, 2.0], [-1.0, 2.0, 6.0]]
# chute inical: [1,1,1]
# solução: [1.0,2.0,3.0]

class MenuMetodoGaussJacobi:
    def __init__(self, master):
        self.master = master
        master.title("Método de Gauss-Jacobi")

        #altera o tamanho do menu
        master.geometry("720x360")

        self.label = Label(master, text="Insira os parâmetros:", font=("Fixedsys",16))
        self.label.grid(row=0, column=1)

        #frame
        self.frame = Frame(master)

        #botao que fecha o menu
        self.close_button = Button(master, text="Fechar", command=master.quit)
        self.close_button.config(width = 2)
        self.close_button.grid(row=14, column=2)

        #cria menu no topo da janela, com a label Ajuda
        self.principal = Menu(master)
        self.master.config(menu=self.principal)
        self.principal.add_command(label="Ajuda", command=self.Ajuda)
        self.principal.add_command(label="Sobre", command=self.Sobre)

        #espaço para inserir a Matriz A
        self.labelMatrizA = Label(master, text="Insira a Matriz A:", font=("Fixedsys", 12))
        self.labelMatrizA.grid(row=1, column=1)
        self.matrizA = StringVar()
        self.campoMatrizA = Entry(master, textvar=self.matrizA)
        self.campoMatrizA.grid(row=2, column=1)

        #chute o vetor chute inicial
        self.labelChuteInicial = Label(master, text="Insira o chute inicial", font=("Fixedsys", 12))
        self.labelChuteInicial.grid(row=3, column=1)
        self.chuteInicial = StringVar()
        self.campoChuteInicial = Entry(master, textvar = self.chuteInicial)
        self.campoChuteInicial.grid(row=4, column=1)

        #Insira o vetor solução
        self.labelVetorSolucao = Label(master, text="Insira o vetor solução", font=("Fixedsys", 12))
        self.labelVetorSolucao.grid(row=5, column=1)
        self.vetorSolucao = StringVar()
        self.campoVetorSolucao = Entry(master, textvar=self.vetorSolucao)
        self.campoVetorSolucao.grid(row=6, column=1)

        #Insira o numero de interações
        self.labelNumeroInteracoes = Label(master, text="Insira o número de interações", font=("Fixedsys", 12))
        self.labelNumeroInteracoes.grid(row=7, column=1)
        self.numeroInteracoes = IntVar()
        self.campoNumeroInteracoes = Entry(master, textvar=self.numeroInteracoes)
        self.campoNumeroInteracoes.grid(row=8, column=1)

        #executa o método de Gauss-Seidel
        self.botaoExecutar = Button(master, text="Calcular", command=self.MetodoGaussJacobi)
        self.botaoExecutar.config(height=2, width=10)
        self.botaoExecutar.grid(row=13, column=2)

        #Campo que mostra o resultado Final
        self.labelResultado = Label(master, text="Resposta Final: ", font=("Fixedsys", 12))
        self.labelResultado.grid(row=11, column=1)

    def Ajuda(self):
        texto_ajuda = 'Para inserir a equação utilize os seguintes operadores          \n'\
                      '  - \'*\' : Multiplicação                                       \n'\
                      '  - \'**\' : Potenciação                                        \n' \
                      '  - \'+\' : Adição                                               \n' \
                      '  - \'-\' : Subtração                                            \n' \
                      '  - \'/\' : Divisão                                              \n' \
                      '  - exemplo de inputs:                                             \n'\
                      '  matriz A:[[4.0, -2.0, 1.0], [1.0, -3.0, 2.0], [-1.0, 2.0, 6.0]] \n' \
                      '  matriz b e solucao: [1,1,1] ou [1.0,2.0,3.0]                   '

        self.pop_up = Toplevel()
        self.label = Label(self.pop_up,text = texto_ajuda, height=18, width=72,font=("Fixedsys",12))
        self.label.pack(expand=True)

    def Sobre(self):
        texto_sobre = '   É um método iterativo para resolução de sistemas de equações lineares. \n'

        self.pop_upSobre = Toplevel()
        self.labelSobre = Label(self.pop_upSobre, text=texto_sobre, height=12, width=72, font=("Fixedsys", 12))
        self.labelSobre.pack(expand=True)

    def MetodoGaussJacobi(self):

        matrizA = np.array(eval(self.matrizA.get()))
        diagonal = np.diag(matrizA)
        matrizR = matrizA - np.diagflat(diagonal)

        vetorSolucao = eval(self.vetorSolucao.get())
        chuteInicial = eval(self.chuteInicial.get())
        numeroInteracoes = self.numeroInteracoes.get()

        for i in range(numeroInteracoes):
            chuteInicial = (vetorSolucao - np.dot(matrizR, chuteInicial)) / diagonal

        self.labelResultado.config(text='Resultado Final '+ str(chuteInicial))

principal = Tk()
menu = MenuMetodoGaussJacobi(principal)
principal.mainloop()
