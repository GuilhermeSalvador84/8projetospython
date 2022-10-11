# Projeto Chute o número
# O algoritimo gerar um valor aletório e o usuário tentará adivinhar, haverá dicas parao usuário.
import random
import PySimpleGUI as sg


class ChuteONumero:

    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def iniciar(self):
        # Layout
        layout = [
            [sg.Text('Seu Chute' ,size=(20,0))],
            [sg.Input(size=(18,0),key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(20,10))]
        ]
        # Criar uma janela
        self.janela = sg.Window('Chute o Numero!', layout=layout)
        self.GerarNumeroAleatorio()
        try:
            while True:
                # Receber os valores
                self.LerValoresdaTela()
                # Fazer alguma coisa com os valores
                if self.evento == 'Chutar!':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                         if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Chute um valor mais baixo!')
                            self.LerValoresdaTela()
                            break
                         elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('Chute um valor mais alto!')
                            self.LerValoresdaTela()
                            break
                         if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print('PARABÉNS VOCÊ ACERTOU!!')
        except:
            print('Favor digitar apenas números!')
            self.iniciar()

    def LerValoresdaTela(self):
        self.evento, self.valores = self.janela.Read()

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

chute = ChuteONumero()
chute.iniciar()