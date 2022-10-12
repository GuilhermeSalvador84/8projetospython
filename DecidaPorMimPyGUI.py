# Decida por mim
# Objetivo: responder as perguntas do usuário.
import random

import PySimpleGUI as sg


class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso!',
            'Não sei, você que sabe!',
            'Não faz isso Não!',
            'Acho que está na hora certa.'
        ]

    def iniciar(self):
        # Layout
        layout = [
            [sg.Text('Faça sua pergunta:')],
            [sg.Input()],
            [sg.Output(size=(50, 10))],
            [sg.Button('Decida por mim')]
        ]
        # Criar a Janela
        self.janela = sg.Window('Decida por mim!', layout=layout)
        while True:
            # Ler os valores
            self.eventos, self.valores = self.janela.Read()
            # Fazer algo com os valores
            if self.eventos == 'Decida por mim':
                print(random.choice(self.respostas))


decida = DecidaPorMim()
decida.iniciar()
