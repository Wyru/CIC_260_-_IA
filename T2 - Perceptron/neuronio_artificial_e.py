"""
    Perceptron E

    AUTOR:  WILLIAN SAYMON DA SILVA
    MATRICULA: 33962
    DATA: 16/10/2017

    DESCRIÇÃO: O programa em questão consite de neuronio/perceptron que aprende a avaliar
    entradas para obter resultados da porta lógica E. O mesmo foi desenvolvido para o
    Trabalho 2 da disciplina de Inteligência Artificial do Curso de Ciências da Computação
    na UNIFEI

    Como usar: Basta executar.

"""


from random import uniform


class NeuronioE:

    def __init__(self):
        self.entrada_padrao = [[-1, -1, -1],
                               [-1, 1, -1],
                               [1, -1, -1],
                               [1, 1, 1]]
        self.padrao = 0
        self.limiar_t = 0
        self.fator_correcao = 0.2
        self.peso_1 = uniform(-1,1)
        self.peso_2 = uniform(-1,1)
        self.treino_completo = False
        self.bias = -1

    def treino(self):
        num_epoca = 0
        print("Pesos Iniciais:\nPeso 1: {}\nPeso 2: {}".format(self.peso_1, self.peso_2))
        while True:
            print("Época {}".format(num_epoca))
            self.treino_completo = True
            for self.padrao in range(0, 4):
                somatoria = self.calcula_somatoria()
                valor_obtido = self.ativacao(somatoria)

                if valor_obtido is not self.entrada_padrao[self.padrao][2]:
                    print("Erro encontrado :( Estudando causa...")
                    self.treino_completo = False
                    erro = self.calcula_erro(valor_obtido)
                    self.atualiza_pesos(erro)

            print("peso 1 = {}\npeso 2 = {}".format(self.peso_1, self.peso_2))
            if self.treino_completo:
                print("Treino Completo!")
                break
            num_epoca += 1
            if num_epoca > 1000:
                break;

    def calcula_somatoria(self):
        return (self.peso_1 * self.entrada_padrao[self.padrao][0]) + (self.peso_2 * self.entrada_padrao[self.padrao][1]) + self.bias

    def ativacao(self, somatoria):
        if somatoria > self.limiar_t:
            return 1
        else:
            return -1

    def calcula_erro(self, obtido):
        return self.entrada_padrao[self.padrao][2] - obtido

    def atualiza_pesos(self, erro):
        self.peso_1 = self.peso_1 + (self.entrada_padrao[self.padrao][0] * self.fator_correcao * erro)
        self.peso_2 = self.peso_2 + (self.entrada_padrao[self.padrao][1] * self.fator_correcao * erro)
        self.bias = self.bias + erro

n = NeuronioE()
n.treino()