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

class individual:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y