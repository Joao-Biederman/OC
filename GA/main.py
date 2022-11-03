import numpy as np
import random

def roleta(fitness):
    rouleta = [] # criar lista para receber os elementos
    for i in range(0, len(fitness)): #pra rodar até os o ultimo individuo da população 
        prop = round((fitness[i]*100)/np.sum(fitness)) #calcula a porcentagem/quantidade de posisoes de cada individuo  
        for j in range(0, prop): 
            rouleta.append(i) #pra incrementar os individuos segundo a porcentagem
    return random.choice(rouleta)

def creep(gene):
    if np.random.rand() < 0.05:
        if np.random.rand() < 0.5:
            gene += np.random.normal(0,0.0625)
            print(gene)
        else:
            gene -= np.random.normal(0,0.0625)
            print(gene)
        acerto(gene)

def acerto(gene): # nome temporario
    if gene > 2:
        gene = 2
    if gene < -2:
        gene = -2
    return gene

def calcFitness(self):
    z = -(100*(((self.x**2)-self.y)**2) + ((1-self.x)**2))

class Population:

    def __init__(self, popSize):
        self.popSize = popSize

class Individual:
    
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

        return z