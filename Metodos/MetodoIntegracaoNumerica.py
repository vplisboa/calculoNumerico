from tkinter import *
from sympy import *
import numpy as np
from decimal import Decimal

#caso de teste sin(x) , 0,np.pi/2, 100

class MetodoIntegracaoNumerica:
    def __init__(self, master):
        self.master = master
        master.title("Método da Integração Numérica")

        #altera o tamanho do menu
        master.geometry("720x360")

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

        #espaço para inserir a equação
        self.labelEquacao = Label(master, text="Insira a equação:", font=("Fixedsys", 12))
        self.labelEquacao.grid(row=1, column=1)
        self.equacaoInicial = StringVar()
        self.campoEquacaoInicial = Entry(master, textvar=self.equacaoInicial)
        self.campoEquacaoInicial.grid(row=2, column=1)

        # Inicio Intervalo
        self.labelInicioIntervalo = Label(master, text="Insira o Início do intervalo", font=("Fixedsys", 12))
        self.labelInicioIntervalo.grid(row=3, column=1)
        self.inicioIntervalo = StringVar()
        self.campoInicioIntervalo = Entry(master, textvar=self.inicioIntervalo)
        self.campoInicioIntervalo.grid(row=4, column=1)

        # Fim Intervalo
        self.labelFimIntervalo = Label(master, text="Insira o Fim do intervalo", font=("Fixedsys", 12))
        self.labelFimIntervalo.grid(row=3, column=2)
        self.fimIntervalo = StringVar()
        self.campoFimIntervalo = Entry(master, textvar=self.fimIntervalo)
        self.campoFimIntervalo.grid(row=4, column=2)

        # Quantidade de pontos
        self.labelTolerancia = Label(master, text="Insira a quantidade de pontos", font=("Fixedsys", 12))
        self.labelTolerancia.grid(row=5, column=1)
        self.tolerancia = StringVar()
        self.campoTolerancia = Entry(master, textvar=self.tolerancia)
        self.campoTolerancia.grid(row=6, column=1)

        #Campo que mostra o resultado final
        self.labelResultado = Label(master,text="Resposta Final: ",font=("Fixedsys", 12))
        self.labelResultado.grid(row=11, column=1)

        # Campo que mostra erros para o usuário
        self.labelErrosInput = Label(master, text="", font=("Fixedsys", 12))
        self.labelErrosInput.grid(row=12, column=1)

        #executa o método da Integração Numérica
        self.botaoExecutar = Button(master, text="Calcular", command=self.MetodoIntegracaoNumerica)
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
        self.label = Label(self.pop_up,text = texto_ajuda, height=12, width=60,font=("Fixedsys",12))
        self.label.pack(expand=True)

    def Sobre(self):
        texto_sobre = ' A idéia básica desse método de integração numérica \n' \
                      'é a substituição da função f(x) por um polinômio que \n' \
                      'a aproxime razoavelmente no intervalo [a,b]. Assim o \n' \
                      'problema fica resolvido pela integração de polinômios,\n' \
                      'o que é trivial de se fazer.'

        self.pop_upSobre = Toplevel()
        self.labelSobre = Label(self.pop_upSobre, text=texto_sobre, height=12, width=60, font=("Fixedsys", 12))
        self.labelSobre.pack(expand=True)

    def MetodoIntegracaoNumerica(self):

        if(self.inicioIntervalo.get() == '' or self.fimIntervalo.get() == ''
           or self.tolerancia.get() == '' or self.equacaoInicial.get() == ''):
            self.labelErrosInput.config(text="Todos os campos são obrigatórios")

        else:
            self.labelErrosInput.config(text="")
            
            inicioIntervalo = Decimal(self.inicioIntervalo.get())
            fimIntervalo = Decimal(str(eval(self.fimIntervalo.get())))
            tolerancia = Decimal(self.tolerancia.get())

            x = np.linspace(float(inicioIntervalo + (fimIntervalo - inicioIntervalo) / (2 * tolerancia)), float(fimIntervalo - (fimIntervalo - inicioIntervalo) / (2 * tolerancia)), int(tolerancia))
            area = Decimal('0.0')

            for valor in x:
                fx = self.f(valor)
                area += Decimal(str(fx)) * (fimIntervalo - inicioIntervalo) / tolerancia

            self.labelResultado.config(text = 'Resultado Final: '+str(area))

    def f(self,valor):
        x = valor
        equacao = eval('\'' + self.equacaoInicial.get() + '\'')
        return eval(equacao)

principal = Tk()
menu = MetodoIntegracaoNumerica(principal)
principal.mainloop()