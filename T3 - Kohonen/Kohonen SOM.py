from random import uniform
"""
    Mapa auto organizável de Kohonen

    AUTOR:  WILLIAN SAYMON DA SILVA
    MATRICULA: 33962
    DATA: 26/10/2017

    DESCRIÇÃO: O programa em questão consite de um mapa auto-organizavel de kohonen. O mesmo foi 
    desenvolvido para o Trabalho 3 da disciplina de Inteligência Artificial do Curso de Ciências
    da Computação na UNIFEI

    Como usar: Ao executar o programa ele irá calcular o mapa baseado no exemplo do livro "Fundamentals
    of neural networks: architectures, algorithms, and applications" de Laurene Fausett. Ao instanciar
    o objeto do mapa, é necessário passar como parâmetro a matriz de pesos e a matriz de entrada. Cada
    linha da matriz de entrada corresponde a uma entrada do problema. Cada coluna da matriz de pesos
    equivale a um cluster da resposta. Vale ressaltar que é necessário que a matriz de pesos possua um
    número de linhas igual ao número de colunas da matriz de entrada.
    Para treinar a rede basta executar o método treinar().
"""

class KohonenSOM:
    def __init__(self, entradas, pesos):
        self.entradas = entradas
        self.num_maximo_grupos = 2
        self.fator_aprendizado = 0.6
        self.fator_aprendizado_minimo = 0.00001
        self.pesos = pesos
        self.num_pesos = len(self.pesos)

    def inicia_matriz_pesos(self):
        pesos = []
        for peso in range(0, self.num_pesos):
            linha = []
            for grupo in range(0,self.num_maximo_grupos):
                linha.append(uniform(0, 1))
            pesos.append(linha)
        self.pesos = pesos

    def treinar(self):
        interacoes = 0
        while True:
            if self.fator_aprendizado <= self.fator_aprendizado_minimo:
                break
            print("Época {}".format(interacoes))
            for entrada in range(0, len(self.entradas)):
                menor_distancia = [0, 99999999]
                for grupo in range(0, self.num_maximo_grupos):
                    distancia = self.calcula_distancia(grupo, entrada)
                    if distancia < menor_distancia[1]:
                        menor_distancia = [grupo, distancia]

                print("Entrada {} assemelha-se mais do grupo {}".format(entrada, menor_distancia[0]))
                self.atualiza_peso_grupo(menor_distancia[0], entrada)
            self.imprime_pesos()
            self.atualiza_fator_aprendizado()
            interacoes += 1

    def calcula_distancia(self, grupo, entrada):
        distancia = 0
        for peso in range(0, self.num_pesos):
            distancia += pow(self.pesos[peso][grupo] - self.entradas[entrada][peso], 2)
        return distancia

    def atualiza_peso_grupo(self, grupo, entrada):
        for peso in range(0, self.num_pesos):
            self.pesos[peso][grupo] += self.fator_aprendizado * (self.entradas[entrada][peso] - self.pesos[peso][grupo])
            self.pesos[peso][grupo] = round(self.pesos[peso][grupo], 3)

    def atualiza_fator_aprendizado(self):
        self.fator_aprendizado = self.fator_aprendizado * 0.5

    def imprime_pesos(self):
        print("{} | {}".format(self.pesos[0][0], self.pesos[0][1]))
        print("{} | {}".format(self.pesos[1][0], self.pesos[1][1]))
        print("{} | {}".format(self.pesos[2][0], self.pesos[2][1]))
        print("{} | {}\n".format(self.pesos[3][0], self.pesos[3][1]))

    def imprimir_resultado(self):
        print("Resultado:")
        for entrada in range(0, len(self.entradas)):
            menor_distancia = [0, 99999999]
            for grupo in range(0, self.num_maximo_grupos):
                distancia = self.calcula_distancia(grupo, entrada)
                if distancia < menor_distancia[1]:
                    menor_distancia = [grupo, distancia]
            print("Entrada {} pertence ao grupo {}".format(entrada,menor_distancia[0]))


entradas = [[1, 1, 0, 0],
            [0, 0, 0, 1],
            [1, 0, 0, 0],
            [0, 0, 1, 1]]

pesos = [[.2, .8],
         [.6, .4],
         [.5, .7],
         [.9, .3]]

ksom = KohonenSOM(entradas, pesos)

ksom.treinar()

ksom.imprimir_resultado()