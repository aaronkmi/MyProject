import PySimpleGUI as sg
from re import match

sg.theme('dark')
layout=[
    [
        sg.Input(key='-INPUT-'),
        sg.Spin(['Km to mile','Kg to pound', 'sec to min'], key='-UNITS-'),
        sg.Button('Convert', key = '-CONVERT-')
    ],
    [sg.Text('Output', key = '-OUTPUT-')]
]

window = sg.Window('Convert', layout)

while True :
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        input_value02 = values['-UNITS-']
        if input_value.isnumeric():
            #'''match values['-UNITS-']:'''
            if input_value02 == 'Km to mile':
            #''' case 'Km to mile':   '''
                output =round(float(input_value) * 0.6214,2)
                output_string = f'{input_value} Km are {output} miles.'
            
            elif input_value02 == 'Kg to pound':
                output =round(float(input_value) * 2.20462,2)
                output_string = f'{input_value} Kg are {output} pound.'
                           
            elif input_value02 == 'sec to min':
                output =round(float(input_value) / 60,2)
                output_string = f'{input_value} sec are {output} min.'
            window['-OUTPUT-'].update(output_string)
        else:
            window['-OUTPUT-'].update('Please enter a number')              
window.close()