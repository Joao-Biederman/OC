import numpy as np
import random
import PySimpleGUI as sg #pip install pysimplegui


class Individual(object): 
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __repr__(self):
        return " [x:%s y:%s] " % (self.__x, self.__y)

    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y

    def calcFitness(self):
        z = -(100*(((self.__x**2)-self.__y)**2) + ((1-self.__x)**2))
        if z==0:
            z=0.0000001
        return 1/-z

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
        prop = round((fitness[i]*10000)/np.sum(fitness)) #calcula a porcentagem/quantidade de posisoes de cada individuo  
        for j in range(0, prop): 
            rouleta.append(i) #pra incrementar os individuos segundo a porcentagem
    P1 = random.choice(rouleta)
    P2 = random.choice(rouleta)
    while P1 == P2:
        P2 = random.choice(rouleta)
    pais = [P1, P2]
    return pais

def blx(p1, p2):
    alpha = random.uniform(0, 0.5) #esse calculo retirei dos slides, do meu entendimento foi isso

    beta = random.uniform(-alpha,1+alpha)
    gene = p1+beta*(p1-p2)
    gene = acerto(gene)
    
    return gene

def crossbreed(gen, popSize):
    
    fitness = []
    newgen = []

    for j in range(0, popSize):
        fitness.append(gen[j].calcFitness())
    print('melhor fitness = %s\n' % max(fitness))
    newgen.append(gen[fitness.index(max(fitness))])

    for k in range(popSize-1):
        pai = roleta(fitness)
        if random.uniform(0, 1) < 0.9:
            newX = blx(gen[pai[0]].get_x(), gen[pai[1]].get_x())
            newX = creep(newX)
            newY = blx(gen[pai[0]].get_y(), gen[pai[1]].get_y())
            newY = creep(newY)
            newgen.append(Individual(newX, newY))
        else:
            newgen.append(random.choice([gen[pai[0]], gen[pai[1]]]))

    return newgen

def creep(gene):
    if np.random.rand() < 0.05: #define se vai ser feita a mutação no gene
        if np.random.rand() < 0.5: #define se a mutação sera a adição ou subtração da distribuição normal
            gene += np.random.normal(0,0.5)
        else:
            gene -= np.random.normal(0,0.5)
        gene = acerto(gene) #corrige caso o novo valor do gene tenha saido do intervalo da função
    return gene

def acerto(gene):
    if gene > 10:
        gene = 10
    if gene < -10:
        gene = -10
    return gene

sg.theme('DarkBlack') # styling the window

column = [
    [sg.Text('Set the population size:')],
    [sg.Input(key='INPUT_popsize')],
    [sg.Button('Ok'), sg.Button('Cancel'), ]
]

layout = [
    [sg.VPush()],
    [sg.Push(), sg.Column(column,element_justification='c'), sg.Push()],
    [sg.VPush()]
]

window = sg.Window('Genetic Algorithm', layout, size=(500,500))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'Ok':
        if int(values['INPUT_popsize']) < 1:
            sg.popup('Insert a valid number')
        else:
            popSize = int(values['INPUT_popsize'])
            sg.popup('Simulating population.')
            break

    if event == 'Cancel':
        break

quantGen = 20
gen = popGeneration(popSize)
# print(gen)
# print()

for i in range(0, quantGen):
    print('generation %s = %s' % (i, gen))
    gen = crossbreed(gen, popSize)
print(gen)