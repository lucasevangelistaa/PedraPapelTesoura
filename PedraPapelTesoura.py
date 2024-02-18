import random

class PedraPapelTesoura():
    def __init__(self):
        self.opcoes = ['pedra', 'papel', 'tesoura']
        print('=====Bem-vindo ao Game Pedra, papel e Tesoura!=====')
    
    def escolha_usuario(self):
        escolha = input("--Escolha uma opção: ").lower()
        while escolha not in self.opcoes:
            print('ERRO! Opção Inválida.')
            escolha = str(input("--Escolha uma opção: ")).lower()
        return escolha
    
    def escolha_maquina(self):
        return random.choice(self.opcoes)

    def vencedor(self, escolha_usuario, escolha_maquina):
        if escolha_usuario == escolha_maquina:
            return '-----EMPATE!-----'
        elif escolha_usuario == 'pedra' and escolha_maquina == 'papel':
            return '-----Máquina Venceu!-----'
        elif escolha_usuario == 'papel' and escolha_maquina == 'tesoura':
            return '-----Máquina Venceu!-----'
        elif escolha_usuario == 'tesoura' and escolha_maquina == 'pedra':
            return '-----Máquina Venceu!-----'
        elif escolha_maquina == 'pedra' and escolha_usuario == 'papel':
            return '-----Você Venceu!-----'
        elif escolha_maquina == 'papel' and escolha_usuario == 'tesoura':
            return '-----Você Venceu!-----'
        elif escolha_maquina == 'tesoura' and escolha_usuario == 'pedra':
            return '-----Você Venceu!-----'
        else:
            return 'ERRO!'
        
    def placar(self):
        pass
    
    def game(self):
        escolha_usuario = self.escolha_usuario()
        escolha_maquina = self.escolha_maquina()
        
        print(f'-----Você escolheu {escolha_usuario.upper()}')
        print(f'-----Máquina escolheu {escolha_maquina.upper()}')
            
        resultado = self.vencedor(escolha_usuario, escolha_maquina)
        print(resultado)

jogo = PedraPapelTesoura()

jogo.game()