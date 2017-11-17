from tkinter import *
from decimal import *
from sympy import *
#caso de teste x**4 − 3*x**3 + 2 ; gama = 0.01 ; precisao = 0.00001 ; v0 = 6

class MenuMetodoGradienteDescendente:
    def __init__(self, master):
        self.master = master
        master.title("Método do Gradiente Descendente")

        #altera o tamanho do menu
        master.geometry("720x360")

        self.label = Label(master, text="Insira os parâmetros:", font=("Fixedsys",16))
        self.label.grid(row=0, column=1)

        #frame
        self.frame = Frame(master)

        #botao que fecha o menu
        self.close_button = Button(master, text="Fechar", command=master.quit)
        self.close_button.config(width = 5)
        self.close_button.grid(row=14, column=2)

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

        #Valor Inicial
        self.labelValorInicial = Label(master, text="Insira o Valor Inicial", font=("Fixedsys", 12))
        self.labelValorInicial.grid(row=3, column=1)
        self.valorInicial = StringVar()
        self.campoValorInicial = Entry(master, textvar = self.valorInicial)
        self.campoValorInicial.grid(row=4, column=1)

        # Multiplicador dos passos
        self.labelMultiplicadorPassos = Label(master, text="Insira o mutilplicador para os passos(Gama)", font=("Fixedsys", 12))
        self.labelMultiplicadorPassos.grid(row=3, column=2)
        self.multiplicadorPassos = StringVar()
        self.campoMultiplicadorPassos = Entry(master, textvar=self.multiplicadorPassos)
        self.campoMultiplicadorPassos.grid(row=4, column=2)

        #Insira a precisão
        self.labelPrecisao = Label(master, text="Insira a Precisão(exemplo:0.001)", font=("Fixedsys", 12))
        self.labelPrecisao.grid(row=5, column=1)
        self.precisao = StringVar()
        self.campoPrecisao = Entry(master, textvar=self.precisao)
        self.campoPrecisao.grid(row=6, column=1)

        #Campo que mostra os passos até a resposta ser encontrada
        self.labelPassos = Label(master,text="Quantidade de Passos: ",font=("Fixedsys", 12))
        self.labelPassos.grid(row=10, column=1)

        #Campo que mostra o resultado final
        self.labelResultado = Label(master,text="Resposta Final: ",font=("Fixedsys", 12))
        self.labelResultado.grid(row=11, column=1)

        #Campo que mostra erros para o usuário
        self.labelErrosInput = Label(master, text="", font=("Fixedsys", 12))
        self.labelErrosInput.grid(row=12, column=1)

        #executa o método da bisseção
        self.botaoExecutar = Button(master, text="Calcular", command=self.MetodoBissecao)
        self.botaoExecutar.config(height=2, width=10)
        self.botaoExecutar.grid(row=13, column=2)

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

    def Sobre(self):
        texto_sobre = ' É um método de busca de raízes que bissecta repetidamente um   \n' \
                      'intervalo e então seleciona um subintervalo contendo a raiz    \n' \
                      'para processamento adicional. Trata-se de um método simples e   \n' \
                      'robusto, relativamente lento quando comparado a métodos como o  \n' \
                      'método de Newton ou o método das secantes.'

        self.pop_upSobre = Toplevel()
        self.labelSobre = Label(self.pop_upSobre, text=texto_sobre, height=12, width=70, font=("Fixedsys", 12))
        self.labelSobre.pack(expand=True)

    def MetodoBissecao(self):

        if(self.valorInicial.get() == '' or self.multiplicadorPassos.get() == ''
           or self.precisao.get() == '' or self.equacaoInicial.get() == ''):
            self.labelErrosInput.config(text="Todos os campos são obrigatórios")
            self.labelResultado.config(text='Resultado Final: ')
            self.labelPassos.config(text='Quantidade de Passos: ')

        else:
            self.labelErrosInput.config(text="")

            valorInicial = Decimal(self.valorInicial.get())
            multiplicadorPassos = Decimal(self.multiplicadorPassos.get())
            passoAnterior = valorInicial
            precisao = Decimal(self.precisao.get())
            passos = 0

            while passoAnterior > precisao:

                valorAnterior = valorInicial
                valorInicial += Decimal('-1') * multiplicadorPassos * Decimal(str(self.fDerivada(float(valorAnterior))))
                passoAnterior = abs(valorInicial - valorAnterior)
                passos += 1

            self.labelResultado.config(text = 'Resultado Final: '+str(valorInicial))
            self.labelPassos.config(text='Quantidade de Passos: '+ str(passos))

    def fDerivada(self,valor):
        equacao = eval('\'' + self.equacaoInicial.get() + '\'')
        x = valor
        derivada = str(diff(equacao, 'x'))
        return eval(derivada)

principal = Tk()
menu = MenuMetodoGradienteDescendente(principal)
principal.mainloop()