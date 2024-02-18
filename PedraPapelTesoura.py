import random

class PedraPapelTesoura():
    def __init__(self):
        self.opcoes = ['pedra, papel, tesoura']
        print('Bem-vindo ao Game Pedra, papel e Tesoura!')
    
    def escolha_usuario(self):
        escolha = str(input("Escolha uma opção: ")).lower()
        while escolha not in self.opcoes:
            print('ERRO! Escolha PEDRA, PAPEL ou TESOURA.')
            escolha = str(input("Escolha uma opção: ")).lower()
        return escolha

jogo = PedraPapelTesoura()

jogo.escolha_usuario()