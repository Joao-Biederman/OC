import PySimpleGUI as sg


def startWindow():
    sg.theme('DarkBlack')

    mainColumn = [
        [sg.Text('Set the population size:')],
        [sg.Input(key='INPUT_popSize'), ],
        [sg.Text('Set the number of generetions:')],
        [sg.Input(key='INPUT_genAmount')],
        [sg.Button('Ok', size=(5,1)), sg.Button('Cancel', size=(5,1)), ]
    ]

    layoutDefinitions = [
        [sg.VPush()],
        [sg.Push(), sg.Column(mainColumn, element_justification='c'), sg.Push()],
        [sg.VPush()]
    ]

    return sg.Window('Genetic Algorithm', size=(500,500), finalize=True, layout=layoutDefinitions)

def resetWindow():
    sg.theme('DarkBlack')

    mainColumn = [
        [sg.Button('New Generation', size=(15, 3)), sg.Button('Close', size=(15, 3))]
    ]

    layoutReset = [
        [sg.VPush()],
        [sg.Push(), sg.Column(mainColumn, element_justification='c'), sg.Push()],
        [sg.VPush()]
    ]

    return sg.Window('Genetic Algorithm', size=(500,500), finalize=True, layout=layoutReset)