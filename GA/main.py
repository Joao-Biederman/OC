import numpy as np
import random
import PySimpleGUI as sg

class Individual(object): 
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __repr__(self):
        return "[x:%s y:%s]" % (self.__x, self.__y)

    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y

    def calcFitness(self):
        z = -(100*(((self.__x**2)-self.__y)**2) + ((1-self.__x)**2))
        if z==0:
            z=0.00000001
        return 1/-z
    
    def fitnessRaw(self):
        z = -(100*(((self.__x**2)-self.__y)**2) + ((1-self.__x)**2))
        return z

def popGeneration(popSize):
    generation = []
    for i in range(popSize):
        newIndividual = Individual(np.random.uniform(-2, 2), np.random.uniform(-2, 2))
        generation.append(newIndividual)
    return generation

def rouletteCalc(fitness):
    roulette = [] # criar lista para receber os elementos
    for i in range(0, len(fitness)): #pra rodar até os o ultimo individuo da população 
        prop = round((fitness[i]*10000)/np.sum(fitness)) #calcula a porcentagem/quantidade de posisoes de cada individuo  
        for j in range(0, prop): 
            roulette.append(i) #pra incrementar os individuos segundo a porcentagem
    return roulette

def roulette(roulette):
    P1 = random.choice(roulette)
    P2 = random.choice(roulette)
    while P1 == P2:
        P2 = random.choice(roulette)
    parents = [P1, P2]
    return parents

def blx(p1, p2):
    alpha = random.uniform(0, 0.5) #esse calculo retirei dos slides, do meu entendimento foi isso

    beta = random.uniform(-alpha,1+alpha)
    gene = p1+beta*(p1-p2)
    gene = acerto(gene)
    
    return gene

def elitism(gen, fitness, popSize):

    elite = []

    for i in range(int(popSize*0.005)):
        maxIndex = fitness.index(max(fitness))
        
        elite.append(gen[maxIndex])
        
        gen.pop(maxIndex)
        fitness.pop(maxIndex)

    return elite

def crossbreed(gen, popSize):
    
    fitness = []
    newgen = []

    for j in range(0, popSize):
        fitness.append(gen[j].calcFitness())
    print('Melhor Individuo = %s\n' % gen[fitness.index(max(fitness))])
    print('Melhor fitness   = %s\n' % gen[fitness.index(max(fitness))].fitnessRaw())

    rouletteWheel = rouletteCalc(fitness)

    for k in range(popSize-int(popSize * 0.005)):
        parents = roulette(rouletteWheel)
        if random.uniform(0, 1) < 0.95:
            newX = blx(gen[parents[0]].get_x(), gen[parents[1]].get_x())
            newX = creep(newX)
            newY = blx(gen[parents[0]].get_y(), gen[parents[1]].get_y())
            newY = creep(newY)
            newgen.append(Individual(newX, newY))
        else:
            newgen.append(random.choice([gen[parents[0]], gen[parents[1]]]))

    newgen += elitism(gen, fitness, popSize)

    return newgen

def creep(gene):
    if np.random.rand() < 0.05: #define se vai ser feita a mutação no gene
        if np.random.rand() < 0.5: #define se a mutação sera a adição ou subtração da distribuição normal
            gene += np.random.normal(0,0.5)*gene
        else:
            gene -= np.random.normal(0,0.5)*gene
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
    [sg.Input(key='INPUT_popSize')],
    [sg.Text('Set the number of generetions:')],
    [sg.Input(key='INPUT_genAmount')],
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
        if int(values['INPUT_popSize']) < 1 or int(values['INPUT_genAmount']) < 1:
            sg.popup('Insert a valid number')
        else:
            popSize = int(values['INPUT_popSize'])
            genAmount = int(values['INPUT_genAmount'])
            sg.popup('Simulating population.')
            break

    if event == 'Cancel':
        break

gen = popGeneration(popSize)

print('Gen 0 = %s\n' % gen)

for i in range(0, genAmount):
    # print('generation %s = %s' % (i, gen))
    gen = crossbreed(gen, popSize)

print('Gen %s = %s\n' % (genAmount, gen))