import PySimpleGUI as sg

sg.theme('DarkBlack') # styling the window

layout = [
    [sg.Text('Set the population size:')],
    [sg.Input(key='INPUT_popsize')],
    [sg.Button('Ok'), sg.Button('Cancel'), ]
]

window = sg.Window('Genetic Algorithm', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'Ok':
        if int(values['INPUT_popsize']) < 1:
            sg.popup('Insert a valid number')
        else:
            sg.popup('Simulating population.')
            break

    if event == 'Cancel':
        print(popsizes)
        break