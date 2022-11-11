import numpy as np
import random

class Individual(object): 
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __repr__(self):
        return " [x:%s y:%s] " %(self.__x, self.__y)

    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y

    def calcFitness(self):
        z = -(100*(((self.__x**2)-self.__y)**2) + ((1-self.__x)**2))
        return z

def popGeneration(popSize):
    generation = []
    for i in range(popSize):
        newIndividual = Individual(np.random.uniform(-2, 2), np.random.uniform(-2, 2))
        generation.append(newIndividual)
    return generation

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
    return [P1, P2]

def blx(parent):
    alpha = random.uniform(0,1) #esse calculo retirei dos slides, do meu entendimento foi isso
    taxa_cruz = 0.9 #estou aderindo este valor devido ao fato de maior variabilidade 

    if alpha<=taxa_cruz: 
        beta = random.uniform(-alpha,1+alpha)
        return (parent[0]+beta*(parent[1]-parent[0]))
    else:
        return random.choice(parent)

def crossbreed(gen, popSize, fitness):
    for i in range(popSize-1):
        pai = roleta(fitness)
        newIndividual = Individual(blx([gen[pai[0]].get_x(), gen[pai[1]].get_x()]), blx([gen[pai[0]].get_y(), gen[pai[1]].get_y()]))

def creep(gene):
    if np.random.rand() < 0.05: #define se vai ser feita a mutação no gene
        if np.random.rand() < 0.5: #define se a mutação sera a adição ou subtração da distribuição normal
            gene += np.random.normal(0,0.0625)
            print(gene)
        else:
            gene -= np.random.normal(0,0.0625)
            print(gene)
        gene = acerto(gene) #corrige caso o novo valor do gene tenha saido do intervalo da função
    return gene

def acerto(gene): #Nome temporario #Faz a correção de valores fora do intervalo
    if gene > 2:  #verifica se o valor do gene está maior que o teto do intervalo
        gene = 2
    if gene < -2: #verifica se o valor do gene está menor que o piso do intervalo
        gene = -2
    return gene

quantGen = 5
popSize = 10
gen = popGeneration(10)

for i in range(0, quantGen):
    print('generation %s = %s' % (i, gen))
    newgen = []
    fitness = []
    
    for j in range(popSize):
        fitness.append(gen[j].calcFitness())
    print('melhor fitness = %s' % max(fitness))
    newgen.append(gen[fitness.index(max(fitness))])

    for j in range(popSize-1):
        pai = roleta(fitness)
        newgen.append(Individual(blx([gen[pai[0]].get_x(), gen[pai[1]].get_x()]), blx([gen[pai[0]].get_y()(), gen[pai[1]].get_y()])))

    print('New gen = %s' % newgen)