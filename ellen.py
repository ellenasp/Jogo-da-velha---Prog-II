import tkinter as tk
from tkinter import messagebox
from random import choice  # escolha aleatória da IA

# Classe que representa cada botão do tabuleiro
class BotaoJogo:
    def __init__(self, letra, linha, coluna, janela, callback):
        self.letra = letra
        self.botao = tk.Button(
            janela,
            width=15,
            height=10,
            background="black",
            command=lambda: callback(self.letra, self)  # chama a função da jogada ao clicar
        )
        self.botao.grid(row=linha, column=coluna, padx=2, pady=2)

    def marcar(self, texto, cor):
        # marca o botão com o símbolo do jogador e desativa
        self.botao.config(text=texto, bg=cor, font=("Arial", 9, "bold"), state="disabled")

    def resetar(self):
        # reseta o botão para o estado inicial do jogo
        self.botao.config(text="", bg="black", state="normal")


# Classe que representa um jogador
class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = 0  # pontuação inicial do jogador
        self.ListaJogadas = [0] * 8  # lista que contem as 8 combinações que garantem vitória nas linhas, colunas ou diagonais


# Classe principal do jogo, gerencia o jogo da velha
class JogoDaVelha:
    def __init__(self, janela):
        self.janela = janela
        self.jogoAtivo = False  # indica se o jogo está em andamento
        self.temVencedor = False  # indica se já houve um vencedor
        self.letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]  # identificadores únicos para cada botão do tabuleiro
        self.posVencedoras = ["ABC", "DEF", "GHI", "ADG", "BEH", "CFI", "AEI", "CEG"]  # combinações da vitória
        self.jogadasPossiveis = self.letras[:]  # lista de jogadas disponíveis
        self.botoes_dict = {}  # Dicionário para acessar os botões por letra
        self.botoes = []  # lista de todos os botões
        self.jogador1 = Jogador("Você")  # jogador1 você
        self.jogador2 = Jogador("IA")  # computador joga
        self.criar_interface()  # cria a interface do jogo

    # criação do tabuleiro do jogo
    def criar_interface(self):
        for index, letra in enumerate(self.letras):
            linha = index // 3
            coluna = index % 3
            botao = BotaoJogo(letra, linha, coluna, self.janela, self.jogada)
            self.botoes_dict[letra] = botao
            self.botoes.append(botao)

        # criação do botão de ‘iniciar’
        botaoIniciar = tk.Button(
            self.janela,
            text="Iniciar Jogo",
            font=("Arial", 14, "bold"),
            bg="green",
            fg="white",
            width=20,
            height=2,
            command=self.iniciar_jogo
        )
        botaoIniciar.grid(row=3, column=0, columnspan=3, pady=20)

    # reinicia o estado do jogo para uma nova partida
    def iniciar_jogo(self):
        self.jogadasPossiveis = self.letras[:]
        self.temVencedor = False
        self.jogoAtivo = True
        self.jogador1 = Jogador("Você")
        self.jogador2 = Jogador("IA")

        # reseta todos os botões do tabuleiro
        for botao in self.botoes:
            botao.resetar()
        self.janela.attributes('-disabled', False)

    # função chamada quando o jogador faz uma jogada
    def jogada(self, escolha, botao_obj):
        if not self.jogoAtivo:
            messagebox.showinfo("Atenção", "Clique em 'Iniciar Jogo' para começar!")
            return

        if self.temVencedor or escolha not in self.jogadasPossiveis:
            return

        botao_obj.marcar("X", "red")  # marca a jogada do jogador
        self.jogadasPossiveis.remove(escolha)

        for i, pos in enumerate(self.posVencedoras):
            if escolha in pos:
                if self.jogador1.ListaJogadas[i] + 1 == 3:
                    messagebox.showinfo("Vitória!", f"O jogador {self.jogador1.nome} venceu!")
                    self.temVencedor = True
                    return
                else:
                    self.jogador1.ListaJogadas[i] += 1

        # Verifica se houve empate após a jogada do jogador
        if not self.jogadasPossiveis and not self.temVencedor:
            messagebox.showinfo("Empate!", "O jogo terminou em empate!")
            self.temVencedor = True
            return

        # caso não tenha vencedor, a IA faz a sua jogada
        self.jogada_ia()

    # função que executa a jogada da IA
    def jogada_ia(self):
        if not self.jogadasPossiveis or self.temVencedor:
            return

        escolha = choice(self.jogadasPossiveis)
        self.jogadasPossiveis.remove(escolha)
        botao = self.botoes_dict[escolha]
        botao.marcar("O", "blue")

        for i, pos in enumerate(self.posVencedoras):
            if escolha in pos:
                if self.jogador2.ListaJogadas[i] + 1 == 3:
                    messagebox.showinfo("Vitória!", f"A IA ({self.jogador2.nome}) venceu!")
                    self.temVencedor = True
                    return
                else:
                    self.jogador2.ListaJogadas[i] += 1

        # Verifica se houve empate após a jogada da IA
        if not self.jogadasPossiveis and not self.temVencedor:
            messagebox.showinfo("Empate!", "O jogo terminou em empate!")
            self.temVencedor = True


# Execução principal
# if __name__ == "__main__":
janela = tk.Tk()
janela.geometry("357x600")  # tamanho da janela
janela.title("Jogo da Velha")  # título da janela
janela.config(background="black")  # cor de fundo
janela.resizable(False, False)  # desabilita redimensionamento da janela
jogo = JogoDaVelha(janela)  # cria a instância do jogo
janela.mainloop()  # inicia o loop principal da interface
