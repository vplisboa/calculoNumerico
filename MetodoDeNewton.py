from tkinter import *
from sympy import *

#caso de teste 9-x*(x-10)

class MenuMetodoDeNewton:
    def __init__(self, master):
        self.master = master
        master.title("Método de Newton")

        #altera o tamanho do menu
        master.geometry("800x360")

        self.label = Label(master, text="Insira os parâmetros:", font=("Fixedsys",16))
        self.label.grid(row=0, column=1)

        #frame
        self.frame = Frame(master)

        #botao que fecha o menu
        self.close_button = Button(master, text="Fechar", command=master.quit)
        self.close_button.config(width = 6)
        self.close_button.grid(row=14, column=2)

        #cria menu no topo da janela, com a label Ajuda
        self.principal = Menu(master)
        self.master.config(menu=self.principal)
        self.principal.add_command(label="Ajuda", command=self.Ajuda)
        self.principal.add_command(label="Sobre", command=self.Sobre)

        #Cria menu no topo da janela com a label Exemplo Interessante
        self.principal.add_command(label="Exemplo", command=self.ExemploInteressante)

        #espaço para inserir a equação
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
        self.labelErro = Label(master, text="Insira o número de casas decimais do erro", font=("Fixedsys", 12))
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

        # Campo que mostra erros para o usuário
        self.labelErrosInput = Label(master, text="", font=("Fixedsys", 12))
        self.labelErrosInput.grid(row=12, column=1)

        #executa o método de newton
        self.botaoExecutar = Button(master, text="Calcular", command=self.MetodoDeNewton)
        self.botaoExecutar.config(height=2, width=10)
        self.botaoExecutar.grid(row=13, column=2)

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
        self.label = Label(self.pop_up,text = texto_ajuda, height=12, width=60,font=("Fixedsys",12))
        self.label.pack(expand=True)

    def Sobre(self):
        texto_sobre = '  Tem o objetivo de estimar as raízes de uma função.       \n' \
                      'Para isso, escolhe-se uma aproximação inicial para esta.'

        self.pop_upSobre = Toplevel()
        self.labelSobre = Label(self.pop_upSobre, text=texto_sobre, height=12, width=60, font=("Fixedsys", 12))
        self.labelSobre.pack(expand=True)

    def ExemploInteressante(self):
        textoExemplo = 'Um exemplo interessante é a função 9-x*(x-10) com valor inicial 10. \n' \
                       'O interessante desse exemplo é que utilizando erro 4 e erro 8, o    \n' \
                       '   valor obtido é o mesmo, porém em passos diferentes isso ocorre   \n' \
                       '   devido à incerteza que existe em se trabalhar com variáveis do   \n' \
                       '   tipo float.'

        self.pop_upExemplo = Toplevel()
        self.labelExemplo = Label(self.pop_upExemplo, text=textoExemplo, height=12, width=74, font=("Fixedsys", 12))
        self.labelExemplo.pack(expand=True)

    def MetodoDeNewton(self):

        if(self.chuteInicial.get() == '' or self.erroDesejado.get() == 0
           or self.equacaoInicial.get() == ''):
            self.labelErrosInput.config(text="Todos os campos são obrigatórios")

        else:
            self.labelErrosInput.config(text="")
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
menu = MenuMetodoDeNewton(principal)
principal.mainloop()