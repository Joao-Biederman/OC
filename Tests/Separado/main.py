import PySimpleGUI as sg
from genAlgorithm import *
import view

janela1, janela2 = view.startWindow(), None

while True:
    window, event, values = sg.read_all_windows()

    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == sg.WIN_CLOSED:
        break
    
    if window == janela1 and event == 'Ok':
        if int(values['INPUT_popSize']) < 1 or int(values['INPUT_genAmount']) < 1:
            sg.popup('Insert a valid number')
        else:
            popSize = int(values['INPUT_popSize'])
            genAmount = int(values['INPUT_genAmount'])
            sg.popup('Simulating population.')
            runGen(popSize, genAmount)
            janela2 = view.resetWindow()
            janela1.hide()

    if window == janela2 and event == 'New Generation':
        janela2.hide()
        janela1.un_hide()

    if window == janela1 and event == 'Cancel':
        break
    if window == janela2 and event == 'Close':
        break