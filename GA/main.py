# import numpy as np
import random

def roleta(fitness):
    rouleta = [] # criar lista para receber os elementos
    for i in range(0, len(fitness)): #pra rodar até os o ultimo individuo da população 
        prop = round((fitness[i]*100)/np.sum(fitness)) #calcula a porcentagem/quantidade de posisoes de cada individuo  
        for j in range(0, prop): 
            rouleta.append(i) #pra incrementar os individuos segundo a porcentagem
    return random.choice(rouleta)

class individual:
    
    def __init__(self, x, y):
        self.x = x;
        self.y = y;
    
    def calcFitness(self):
        z = -(100*(((self.x**2)-self.y)**2) + ((1-self.x)**2))

        return z