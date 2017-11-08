from tkinter import *

#caso de teste

class MenuMetodoBissecao:
    def __init__(self, master):
        self.master = master
        master.title("Método da Bisseção")

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

        #espaço para inserir a equação
        self.labelEquacao = Label(master, text="Insira a equação:", font=("Fixedsys", 12))
        self.labelEquacao.grid(row=1, column=1)
        self.equacaoInicial = StringVar()
        self.campoEquacaoInicial = Entry(master, textvar=self.equacaoInicial)
        self.campoEquacaoInicial.grid(row=2, column=1)

        #Valor Inicial
        self.labelValorInicial = Label(master, text="Insira o Início do intervalo", font=("Fixedsys", 12))
        self.labelValorInicial.grid(row=3, column=1)
        self.valorInicial = StringVar()
        self.campoValorInicial = Entry(master, textvar = self.valorInicial)
        self.campoValorInicial.grid(row=4, column=1)

        # Insira o numero de casas decimais da tolerancia
        #self.labelTolerancia = Label(master, text="Insira a tolerância", font=("Fixedsys", 12))
        #self.labelTolerancia.grid(row=5, column=1)
        #self.tolerancia = StringVar()
        #self.campoTolerancia = Entry(master, textvar=self.tolerancia)
        #self.campoTolerancia.grid(row=6, column=1)

        #Insira a quantidade maxima de passos
        self.labelQuantidadePassos = Label(master, text="Insira a quantidade máxima de passos", font=("Fixedsys", 12))
        self.labelQuantidadePassos.grid(row=7, column=1)
        self.quantidadePassos = IntVar()
        self.campoQuantidadePassos = Entry(master, textvar=self.quantidadePassos)
        self.campoQuantidadePassos.grid(row=8,column=1)

        #Campo que mostra os passos até a resposta ser encontrada
        self.labelPassos = Label(master,text="Quantidade de Passos: ",font=("Fixedsys", 12))
        self.labelPassos.grid(row=10, column=1)

        #Campo que mostra o resultado final
        self.labelResultado = Label(master,text="Resposta Final: ",font=("Fixedsys", 12))
        self.labelResultado.grid(row=11, column=1)

        #Campo que mostra o erro no resultado final
#        self.labelErroFinal = Label(master,text="Erro Final: ",font=("Fixedsys", 12))
 #       self.labelErroFinal.grid(row=12,column=1)

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
        valorInicial = eval(self.valorInicial.get())

        #tolerancia = eval(self.tolerancia.get())
        passos = 0
        quantidadeMaximaPassos = self.quantidadePassos.get()
        #erro = 1
        resultado = 0.0

        while (passos < quantidadeMaximaPassos):
            resultado = self.f(valorInicial)
            #erro = norm(valorInicial - resultado)
            print(resultado)
            valorInicial = resultado
            passos += 1

        self.labelResultado.config(text = 'Resultado Final: '+str(resultado))
        self.labelPassos.config(text='Quantidade de Passos: '+ str(passos))
        #self.labelErroFinal.config(text='Erro Final: '+str(erro))

    def f(self,valor):
        x = valor
        equacao = eval('\'' + self.equacaoInicial.get() + '\'')
        return eval(equacao)

principal = Tk()
menu = MenuMetodoBissecao(principal)
principal.mainloop()