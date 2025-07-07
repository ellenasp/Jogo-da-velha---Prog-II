###################### IMPORTS ##################
from tkinter import *
from random import *

###################### TKINTER CONFIG ############################

janela = Tk()

janela.geometry("600x800")
janela.title("Jogo da Velha")

buttonA = Button(janela, width = 8, height = 8, background="black", command=lambda: jogada("A", buttonA))
buttonB = Button(janela, width = 8, height = 8, background="black", command=lambda: jogada("B", buttonB))
buttonC = Button(janela, width = 8, height = 8, background="black", command=lambda: jogada("C", buttonC))
buttonD = Button(janela, width = 8, height = 8, background="black", command=lambda: jogada("D", buttonD))
buttonE = Button(janela, width = 8, height = 8, background="black", command=lambda: jogada("E", buttonE))
buttonF = Button(janela, width = 8, height = 8, background="black", command=lambda: jogada("F", buttonF))
buttonG = Button(janela, width = 8, height = 8, background="black", command=lambda: jogada("G", buttonG))
buttonH = Button(janela, width = 8, height = 8, background="black", command=lambda: jogada("H", buttonH))
buttonI = Button(janela, width = 8, height = 8, background="black", command=lambda: jogada("I", buttonI))

buttonA.grid(row = 0, column = 0, pady = 2, padx = 2)
buttonB.grid(row = 0, column = 1, pady = 2, padx = 2)
buttonC.grid(row = 0, column = 2, pady = 2, padx = 2)
buttonD.grid(row = 1, column = 0, pady = 2, padx = 2)
buttonE.grid(row = 1, column = 1, pady = 2, padx = 2)
buttonF.grid(row = 1, column = 2, pady = 2, padx = 2)
buttonG.grid(row = 2, column = 0, pady = 2, padx = 2)
buttonH.grid(row = 2, column = 1, pady = 2, padx = 2)
buttonI.grid(row = 2, column = 2, pady = 2, padx = 2)

# Metodo que habilita/desabilita o redimensionamento da largura e altura da janela
janela.resizable(True, True)
janela.config(background="black")


##################### VARIAVEIS GLOBAIS ########################

posVencedoras = ["ABC", "DEF", "GHI", "ADG", "BEH", "CFI", "AEI", "CEG"]
jogadasPossiveis = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
jogadas = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
botoes = [buttonA, buttonB, buttonC, buttonD, buttonE, buttonF, buttonG, buttonH, buttonI]
temVencedor = False


###################### CLASSES ##################################

class Jogador:

    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = 0
        self.ListaJogadas = [0, 0, 0, 0, 0, 0, 0, 0]
                #"ABC", "DEF", "GHI", "ADG", "BEH", "CFI", "AEI", "CEG"
                #  0,     1,     2,     3,     4,     5,     6,     7

################### FUNCOES ###############################

def jogada(escolha, botao):

    global temVencedor

    botao.config(bg="red")

    # remove a jogada escolhida das jogadas possiveis
    jogadasPossiveis.remove(escolha)

    # Passar pela lista posVencedoras e se a posicao fizer parte de uma posicoes
    # vencedoras, incrementamos 1 ao elemento da lista ListaJogadas no indice
    # correspondente
    for i, posVenc in enumerate(posVencedoras):

        if escolha in posVenc:
            if jogador1.ListaJogadas[i] + 1 == 3:
                print(f"Jogador {jogador1.nome} Venceu")
                temVencedor = True
            else:
                jogador1.ListaJogadas[i] += 1
            #print(jogador1.ListaJogadas)

    if temVencedor == False:
        jogadaIA()


def jogadaIA():

    global temVencedor

    # gerar a escolha da IA
    print(jogadasPossiveis)
    indEscolha = randint(0, len(jogadasPossiveis) - 1)
    escolha = jogadasPossiveis[indEscolha]
    jogadasPossiveis.remove(escolha)

    indLetra = jogadas.index(escolha)
    botao = botoes[indLetra]
    botao.config(bg="blue")

    print(f"A IA jogou na casa {escolha}")

    # Passar pela lista posVencedoras e se a posicao fizer parte de uma posicoes
    # vencedoras, incrementamos 1 ao elemento da lista ListaJogadas no indice
    # correspondente
    for i, posVenc in enumerate(posVencedoras):

        if escolha in posVenc:
            if jogador2.ListaJogadas[i] + 1 == 3:
                print(f"Jogador {jogador2.nome} Venceu")
                temVencedor = True
            else:
                jogador2.ListaJogadas[i] += 1

    if temVencedor == True:
        janela.attributes('-disabled', True)



###################### MAIN #####################################

#def main():
#    while True:
#        jogador1 = jogador()
#        jogador2 = jogador()
#main()

jogador1 = Jogador("Gui")
jogador2 = Jogador("IA")

janela.mainloop()