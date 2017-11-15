from tkinter import *
from decimal import *

#caso de teste x**2 - 7, -1:3 , 0.0001

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

        #Inicio Intervalo
        self.labelInicioIntervalo = Label(master, text="Insira o Início do intervalo", font=("Fixedsys", 12))
        self.labelInicioIntervalo.grid(row=3, column=1)
        self.inicioIntervalo = StringVar()
        self.campoInicioIntervalo = Entry(master, textvar = self.inicioIntervalo)
        self.campoInicioIntervalo.grid(row=4, column=1)

        # Fim Intervalo
        self.labelFimIntervalo = Label(master, text="Insira o Fim do intervalo", font=("Fixedsys", 12))
        self.labelFimIntervalo.grid(row=3, column=2)
        self.fimIntervalo = StringVar()
        self.campoFimIntervalo = Entry(master, textvar=self.fimIntervalo)
        self.campoFimIntervalo.grid(row=4, column=2)

        #Insira a tolerancia
        self.labelTolerancia = Label(master, text="Insira a Tolerância(exemplo:0.001)", font=("Fixedsys", 12))
        self.labelTolerancia.grid(row=5, column=1)
        self.tolerancia = StringVar()
        self.campoTolerancia = Entry(master, textvar=self.tolerancia)
        self.campoTolerancia.grid(row=6, column=1)

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

        if(self.inicioIntervalo.get() == '' or self.fimIntervalo.get() == ''
           or self.tolerancia.get() == '' or self.equacaoInicial.get() == ''):
            self.labelErrosInput.config(text="Todos os campos são obrigatórios")

        else:
            self.labelErrosInput.config(text="")

            inicioIntervalo = Decimal(self.inicioIntervalo.get())
            fimIntervalo = Decimal(self.fimIntervalo.get())
            tolerancia= Decimal(self.tolerancia.get())
            passos = 0
            dois = Decimal('2.0')
            pontoMedio = 0

            if self.f(inicioIntervalo) * self.f(fimIntervalo) > 0:
                resultado = 'Não tem raíz'

            else:
                while (fimIntervalo - inicioIntervalo) / dois > tolerancia:

                    pontoMedio = (inicioIntervalo + fimIntervalo) / dois
                    passos += 1

                    if self.f(pontoMedio) == 0:
                        break

                    elif self.f(inicioIntervalo) * self.f(pontoMedio) < 0:
                        fimIntervalo = pontoMedio

                    else:
                        inicioIntervalo = pontoMedio

                resultado = str(pontoMedio)

            self.labelResultado.config(text = 'Resultado Final: '+resultado)
            self.labelPassos.config(text='Quantidade de Passos: '+ str(passos))

    def f(self,valor):
        x = valor
        equacao = eval('\'' + self.equacaoInicial.get() + '\'')
        return eval(equacao)

principal = Tk()
menu = MenuMetodoBissecao(principal)
principal.mainloop()