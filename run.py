import PySimpleGUI as sg
import encode
import decode

sg.theme('Dark')
sg.SetOptions(element_padding=(0, 0), margins=(10, 0), font=('Tahoma', 18))


nostrings = [[sg.Text('This program only accepts numbers.')]]

inputcol = [[sg.Text('Input:', font=('Tahoma', 20), pad=(0, 10))],
            [sg.Multiline(size=(20, 3), key='input')]]

outputcol = [[sg.Text('Output:', font=('Tahoma', 20), pad=(0, 10))],
             [sg.Output(size=(20, 3), key='output')]]

layout = [[sg.Column(inputcol), sg.Column(outputcol)],
          [sg.Radio('Encode', "RADIO1", default=True, size=(15, 1), font=('Tahoma', 10), key='encode'),
           sg.Radio('Decode', "RADIO1", font=('Tahoma', 10), key='decode')],
          [sg.Button('Cancel', button_color=('white', 'red'), pad=(10, 20)),
           sg.Button('Go', button_color=('white', 'green'), pad=(0, 20))]]


window = sg.Window('Keyboard Reverse', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break

    if window.FindElement('encode'):
        window.FindElement('output').update(encode.Encode(values['input']).encode_input())

    if window.FindElement('decode'):
        window.FindElement('output').update(decode.Decode(values['input']).decode_input())


window.close()
