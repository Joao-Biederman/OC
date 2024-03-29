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

def blx(Pai, Mae):
    alpha = random.uniform(0,1) #esse calculo retirei dos slides, do meu entendimento foi isso
    taxa_cruz = 0.9 #estou aderindo este valor devido ao fato de maior variabilidade 

    if alpha<=taxa_cruz: 
        beta = random.uniform(-alpha,1+alpha)
        return (Pai+beta*(Mae-Pai))
    else:
        return random.choice([Pai,Mae])
    

class individual:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y


########################################################
#Exemplos para analisar como esta se comportando o codigo#
fit = (20, 32, 8, 40)
pais = roleta(fit)
Pai, Mae = pais[0], pais[1]
filho1, filho2 = blx(fit[Pai],fit[Mae]), blx(fit[Pai],fit[Mae]) 
print(pais, fit[Pai], fit[Mae], filho1, filho2)
########################################################