import numpy as np
import random
#import PySimpleGUI as sg
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation

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


def popGeneration(popSize):
    generation = []
    for i in range(popSize):
        newIndividual = Individual(np.random.uniform(-2, 2), np.random.uniform(-2, 2))
        generation.append(newIndividual)
    return generation

tampop = 10
#for i in range(10):
gen = [popGeneration(tampop) for i in range(10)]


def animate(gen, tampop):
        fig = plt.figure(1)
        ax = plt.axes(xlim=[-2,2], ylim=[-2,2])
        for i in range(tampop):
            x = [gen[0][i].get_x() for tampop in gen[0]]
            y = [gen[0][i].get_y() for tampop in gen[0]]
            print(x)
            
            scatter = ax.scatter(x,y)


        def update(i):
            for i in gen[i]:
                for j in range(tampop):
                    x = gen[i][j]
            for i in gen[i]:
                for j in range(tampop):
                    y = gen[i][j]
            # xy = [[x[i][j], y[i][j] for j in range tampop]]
            scatter.set_offsets(x,y)
            #fig.suptitle("Generation: "+str(i))

            return scatter,
        
        anim = FuncAnimation(fig, update, frames=len(gen)-1, interval=500)


        plt.show()

animate(gen, tampop)