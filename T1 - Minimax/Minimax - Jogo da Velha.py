"""
    ALGORITMO MINIMAX APLICADO EM JOGO DA VELHA

    AUTOR:  WILLIAN SAYMON DA SILVA
    MATRICULA: 33962
    DATA: 04/09/2017

    DESCRIÇÃO: O programa em questão consite de um jogo da velha utilizando
    tecnicas de inteligência artificial. O mesmo foi desenvolvido para o Trabalho 1
    da disciplina de Inteligência Artificial do Curso de Ciências da Computação
    na UNIFEI

    Como usar: O jogo inicia sempre no turno do jogador que deve selecionar uma
    das posições do tabuleiro para colocar seu símbolo, que por padrão é X.

"""
import copy


class Tabuleiro:

    def __init__(self):
        self.jogador1 = 'X'
        self.jogador2 = 'O'
        self.vazio = ' '
        self.empate = 'EMPATE'
        self.tamanho_campo = 9
        self.campos = [self.vazio, self.vazio, self.vazio,
                       self.vazio, self.vazio, self.vazio,
                       self.vazio, self.vazio, self.vazio]

    # jogar
    def jogar(self, simbolo, posicao):
        tabuleiro = copy.deepcopy(self)
        tabuleiro.campos[posicao] = simbolo
        return tabuleiro

    #Formatação para impressão
    def __str__(self):
        return '{} | {} | {}\n' \
               '--+---+---\n' \
               '{} | {} | {}\n' \
               '--+---+---\n' \
               '{} | {} | {}'.format(self.campos[0], self.campos[1], self.campos[2],
                                     self.campos[3], self.campos[4], self.campos[5],
                                     self.campos[6], self.campos[7], self.campos[8])

    # Verificar Vitória
    def jogo_acabou(self):

        # horizontal
        if self.campos[0] == self.campos[1] == self.campos[2] and self.campos[0] is not self.vazio:
            return self.campos[0]
        elif self.campos[3] == self.campos[4] == self.campos[5] and self.campos[3] is not self.vazio:
            return self.campos[3]
        elif self.campos[6] == self.campos[7] == self.campos[8] and self.campos[6] is not self.vazio:
            return self.campos[6]

        # vertical
        elif self.campos[0] == self.campos[3] == self.campos[6] and self.campos[0] is not self.vazio:
            return self.campos[0]
        elif self.campos[1] == self.campos[4] == self.campos[7] and self.campos[1] is not self.vazio:
            return self.campos[1]
        elif self.campos[2] == self.campos[5] == self.campos[8] and self.campos[2] is not self.vazio:
            return self.campos[2]

        # diagonal
        elif self.campos[0] == self.campos[4] == self.campos[8] and self.campos[0] is not self.vazio:
            return self.campos[0]
        elif self.campos[2] == self.campos[4] == self.campos[6] and self.campos[2] is not self.vazio:
            return self.campos[2]
        #empate
        else:
            for i in range(self.tamanho_campo):
                if self.campos[i] is self.vazio:
                    break
                if i is 8:
                    return self.empate
        return None

    # Avalia a Melhor Jogada
    def melhor_jogada(self):
            jogada = self.__minimax(self, self.jogador2, True)
            return jogada

    #Minimax
    def __minimax(self, tabuleiro, turno, raiz):

        if tabuleiro.jogo_acabou() is self.jogador2:
            return 1
        if tabuleiro.jogo_acabou() is self.jogador1:
            return -1
        if tabuleiro.jogo_acabou() is self.empate:
            return 0

        if turno is self.jogador2:
            melhor_jogada = [None, -2]
            prox_turno = self.jogador1
        else:
            melhor_jogada = [None, 2]
            prox_turno = self.jogador2

        for opcao_jogada in range(self.tamanho_campo):
            if tabuleiro.campos[opcao_jogada] is self.vazio:
                jogada = [opcao_jogada, self.__minimax(tabuleiro.jogar(turno,opcao_jogada),prox_turno, False)]

                if turno is self.jogador2:
                    if melhor_jogada[1] < jogada[1]:
                        melhor_jogada = jogada
                else:
                    if melhor_jogada[1] > jogada[1]:
                        melhor_jogada = jogada
        if raiz:
            return melhor_jogada[0]
        else:
            return melhor_jogada[1]


class JogoDaVelha:

    def __init__(self):
        self.tabuleiro = Tabuleiro()

    @staticmethod
    def clear():
        lines = 130
        print("\n" * lines)

    def jogar(self):
        print('JOGO DA VELHA')
        print(self.tabuleiro.__str__())
        print('\n================================================================================\n')
        while True:
            print('TURNO: JOGADOR')
            while True:
                jogada = input('Entre com a posicão[0...8] que você deseja jogar:')
                if jogada.isnumeric():
                    jogada = int(jogada)
                    if 0 <= jogada <=8:
                        if self.tabuleiro.campos[jogada] is not self.tabuleiro.vazio:
                            print('Jogada inválida, campo no tabuleiro ocupado!')
                        else:
                            break
                    else:
                        print('Jogada inválida, digite um valor entre 0 e 8!')
                else:
                    print('Jogada inválida, digite um valor entre 0 e 8!')
            self.tabuleiro = self.tabuleiro.jogar(self.tabuleiro.jogador1,jogada)
            print(self.tabuleiro.__str__())
            print('\n================================================================================\n')
            if self.tabuleiro.jogo_acabou() is not None:
                if self.tabuleiro.jogo_acabou() is self.tabuleiro.empate:
                    print('Deu Velha!')
                elif self.tabuleiro.jogo_acabou is self.tabuleiro.jogador1:
                    print('Parabéns, você venceu!')
                else:
                    print('DERROTA!')
                break
            print('TURNO: IA')
            jogada = self.tabuleiro.melhor_jogada()
            jogada = int(jogada)
            print('AI jogou O em {}'.format(jogada))
            self.tabuleiro = self.tabuleiro.jogar(self.tabuleiro.jogador2, jogada)
            print(self.tabuleiro.__str__())
            print('\n================================================================================\n')
            if self.tabuleiro.jogo_acabou() is not None:
                if self.tabuleiro.jogo_acabou() is self.tabuleiro.empate:
                    print('Deu Velha!')
                elif self.tabuleiro.jogo_acabou is self.tabuleiro.jogador1:
                    print('Parabéns, você venceu!')
                else:
                    print('DERROTA!')
                break

jdv = JogoDaVelha()
jdv.jogar()