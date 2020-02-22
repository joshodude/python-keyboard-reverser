import PySimpleGUI as sg
import reverser

sg.theme('Dark')
sg.SetOptions(element_padding=(0, 0), margins=(10, 0), font=('Tahoma', 18))

inputcol = [[sg.Text('Input:', font=('Tahoma', 20), pad=(0, 10))],
            [sg.Multiline(size=(20, 3), key='input')]]

outputcol = [[sg.Text('Output:', font=('Tahoma', 20), pad=(0, 10))],
             [sg.Output(size=(20, 3), key='output')]]

layout = [[sg.Column(inputcol), sg.Column(outputcol)],
          [sg.Button('Cancel', button_color=('white', 'red'), pad=(10, 20)),
           sg.Button('Reverse', button_color=('white', 'green'), pad=(0, 20), key='green_button')]]


window = sg.Window('Keyboard Reverser', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break

    window['output'](reverser.Reverse(values['input']).reverse_input())


window.close()
