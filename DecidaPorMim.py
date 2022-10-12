# Decida por mim
# Objetivo: responder as perguntas do usuário.
import random
class DecidaPorMim:
    def __init__(self):
        self.respostas= [
            'Com certeza, você deve fazer isso!',
            'Não sei, você que sabe!',
            'Não faz isso Não!',
            'Acho que está na hora certa.'
        ]

    def iniciar(self):
        input('Faça uma pergunta:')
        print(random.choice(self.respostas))

decida = DecidaPorMim()
decida.iniciar()
