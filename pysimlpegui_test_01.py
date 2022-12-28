import PySimpleGUI as sg

layout = [
    [sg.Text('Text'),sg.Spin(['item 1', 'item 2'])],
    [sg.Button('Button',key = '-BUTTON1-')],
    [sg.Input(key='-INPUT-')],
    [sg.Text('Test'), sg.Button('Button', key='-BUTTON2-')]      
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    if event == '-BUTTON1-':
        '''print('button1 pressed')'''
        window['-INPUT-'].update(values['-INPUT-'])
    if event =='-BUTTON2-':
        print('Button2 pressed')   
    
   
window.close()