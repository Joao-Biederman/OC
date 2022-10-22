import numpy as np
import random

def roleta(fitness):
    rouleta = [] # criar lista para receber os elementos
    for i in range(0, len(fitness)): #pra rodar até os o ultimo individuo da população 
        prop = round((fitness[i]*100)/np.sum(fitness)) #calcula a porcentagem/quantidade de posisoes de cada individuo  
        for j in range(0, prop): 
            rouleta.append(i) #pra incrementar os individuos segundo a porcentagem
    return random.choice(rouleta)
