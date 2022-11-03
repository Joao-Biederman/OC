import numpy as np
import random

def roleta(fitness):
    rouleta = [] # criar lista para receber os elementos
    P1 = None
    P2 = None
    for i in range(0, len(fitness)): #pra rodar até os o ultimo individuo da população 
        prop = round((fitness[i]*100)/np.sum(fitness)) #calcula a porcentagem/quantidade de posisoes de cada individuo  
        for j in range(0, prop): 
            rouleta.append(i) #pra incrementar os individuos segundo a porcentagem    
    P1 = random.choice(rouleta)
    P2 = random.choice(rouleta)
    while P1 == P2:
        P2 = random.choice(rouleta)
    pais = [P1, P2]
    return pais

def creep(gene):
    if np.random.rand() < 0.05: #define se vai ser feita a mutação no gene
        if np.random.rand() < 0.5: #define se a mutação sera a adição ou subtração da distribuição normal
            gene += np.random.normal(0,0.0625)
            print(gene)
        else:
            gene -= np.random.normal(0,0.0625)
            print(gene)
        acerto(gene) #corrige caso o novo valor do gene tenha saido do intervalo da função

def acerto(gene): #Nome temporario #Faz a correção de valores fora do intervalo
    if gene > 2:  #verifica se o valor do gene está maior que o teto do intervalo
        gene = 2
    if gene < -2: #verifica se o valor do gene está menor que o piso do intervalo
        gene = -2
    return gene

def calcFitness(self):
    z = -(100*(((self.x**2)-self.y)**2) + ((1-self.x)**2))

class Population:

    def __init__(self, popSize):
        self.popSize = popSize

class Individual:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
