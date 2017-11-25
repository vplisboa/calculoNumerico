from decimal import Decimal
from tkinter import *
from sympy import *
from time import *

class MenuMetodoEuler:
    def __init__(self, master):
        self.master = master
        master.title("Método de Euler")

        #altera o tamanho do menu
        master.geometry("720x450")

        self.label = Label(master, text="Insira os parâmetros:", font=("Fixedsys",16))
        self.label.grid(row=0, column=1)

        #frame
        self.frame = Frame(master)

        #botao que fecha o menu
        self.close_button = Button(master, text="Fechar", command=master.quit)
        self.close_button.config(width = 6)
        self.close_button.grid(row=15, column=3)

        #cria menu no topo da janela, com a label Ajuda
        self.principal = Menu(master)
        self.master.config(menu=self.principal)
        self.principal.add_command(label="Ajuda", command=self.Ajuda)
        self.principal.add_command(label="Sobre", command=self.Sobre)

        #espaço para inserir a equação
        self.labelEquacao = Label(master, text="Insira a equação:", font=("Fixedsys", 12))
        self.labelEquacao.grid(row=1, column=1)
        self.equacaoInicial = StringVar()
        self.campoEquacaoInicial = Entry(master, textvar=self.equacaoInicial)
        self.campoEquacaoInicial.grid(row=2, column=1)

        #valor inical de x
        self.labelPrimeiroX = Label(master, text="Insira o valor de x inicial", font=("Fixedsys", 12))
        self.labelPrimeiroX.grid(row=3, column=1)
        self.primeiroX = StringVar()
        self.campoPrimeiroX = Entry(master, textvar = self.primeiroX)
        self.campoPrimeiroX.grid(row=4, column=1)

        #Segundo valor de x
        self.labelSegundoValorX = Label(master, text="Insira o x para o y desejado", font=("Fixedsys", 12))
        self.labelSegundoValorX.grid(row=5, column=1)
        self.segundoX = StringVar()
        self.campoSegundoX = Entry(master, textvar=self.segundoX)
        self.campoSegundoX.grid(row=6, column=1)

        # valor inical de y
        self.labelPrimeiroY = Label(master, text="Insira o valor de y inicial", font=("Fixedsys", 12))
        self.labelPrimeiroY.grid(row=7, column=1)
        self.primeiroY = StringVar()
        self.campoPrimeiroY = Entry(master, textvar=self.primeiroY)
        self.campoPrimeiroY.grid(row=8, column=1)

        # valor de h
        self.labelValorH = Label(master, text="Insira o valor de h(exemplo 0.01)", font=("Fixedsys", 12))
        self.labelValorH.grid(row=9, column=1)
        self.valorH = StringVar()
        self.campoValorH = Entry(master, textvar=self.valorH)
        self.campoValorH.grid(row=10, column=1)

        # Campo que mostra o resultado final
        self.labelResultado = Label(master, text="Resultado Final: ", font=("Fixedsys", 12))
        self.labelResultado.grid(row=11, column=1)

        #Campo que mostra os passos até a resposta ser encontrada
        self.labelPassos = Label(master,text="Quantidade de Passos: ",font=("Fixedsys", 12))
        self.labelPassos.grid(row=12, column=1)

        #Campo que mostra o tempo de execução do programa
        self.labelTempoExecucao = Label(master,text="Tempo de Execução: ",font=("Fixedsys", 12))
        self.labelTempoExecucao.grid(row=13, column=1)

        # Campo que mostra erros para o usuário
        self.labelErrosInput = Label(master, text="", font=("Fixedsys", 12))
        self.labelErrosInput.grid(row=14, column=1)

        #executa o método de euler
        self.botaoExecutar = Button(master, text="Calcular", command=self.MetodoEuler)
        self.botaoExecutar.config(height=2, width=10)
        self.botaoExecutar.grid(row=15, column=2)

    def Ajuda(self):
        texto_ajuda = 'Para inserir a equação utilize os seguintes operadores     \n'\
                      '  - \'*\' : Multiplicação                                  \n'\
                      '  - \'**\' : Potenciação                                   \n' \
                      '  - \'+\' : Adição                                         \n' \
                      '  - \'-\' : Subtração                                      \n' \
                      '  - \'/\' : Divisão                                         \n' \
                      '  - o h deve ser passado na forma decimal(0.0(...)1)        ' \

        self.pop_up = Toplevel()
        self.label = Label(self.pop_up,text = texto_ajuda, height=12, width=60,font=("Fixedsys",12))
        self.label.pack(expand=True)

    def Sobre(self):
        texto_sobre = ' É um método numérico de primeira ordem para solucionar \n' \
                      'equações diferenciais ordinárias com um valor inicial dado.\n' \
                      'É o tipo mais básico de método explícito para integração\n' \
                      'numérica para equações diferenciais ordinárias.'

        self.pop_upSobre = Toplevel()
        self.labelSobre = Label(self.pop_upSobre, text=texto_sobre, height=12, width=60, font=("Fixedsys", 12))
        self.labelSobre.pack(expand=True)

    def MetodoEuler(self):
        if(self.valorH.get() == '' or self.segundoX.get() == '' or self.primeiroY.get() == ''
           or self.primeiroX.get()   == '' or self.equacaoInicial.get() == ''):
            self.labelErrosInput.config(text="Todos os campos são obrigatórios", fg = "red")
            self.labelResultado.config(text='Resultado Final: ')
            self.labelPassos.config(text='Quantidade de Passos: ')
            self.labelTempoExecucao.config(text='Tempo de Execução: ')

        else:
            inicio = time()
            self.labelErrosInput.config(text="")

            segundoValorX = Decimal(self.segundoX.get())
            xInicial = Decimal(self.primeiroX.get())
            yInicial = Decimal(self.primeiroY.get())
            h = Decimal(self.valorH.get())
            passos = 0
            x = xInicial
            y = yInicial
            quantidadePassos = int((segundoValorX - xInicial) / h)

            for i in range(quantidadePassos):
                x += h * self.f(x,y)
                y += h
                passos += 1

            self.labelResultado.config(text='Resultado Final: ' + str(y))
            self.labelPassos.config(text='Quantidade de Passos: ' + str(passos))
            self.labelTempoExecucao.config(text='Tempo de Execução: ' + str(time() - inicio))

    def f(self, valorX,valorY):
        x = valorX
        y = valorY
        equacao = eval('\'' + self.equacaoInicial.get() + '\'')
        return eval(equacao)

principal = Tk()
menu = MenuMetodoEuler(principal)
principal.mainloop()