'''
Calculadora cientifica Pyhton with interface

by Felipe Ales.
'''
import PySimpleGUI as sg

dados = 'f'

def janelaicial():

    sg.theme('DarkAmber')

    layoutinicio = [  
        [sg.Text('Inciando Calculadora')],
        [sg.Text('Informe seu nome: '), sg.InputText(key='Name')],
        [sg.Button('OK'),sg.Button('Cancelar')]]

    windowstart = sg.Window('Tela Incial',layoutinicio,finalize=True)
    return windowstart


def janelaCalculadora():
    sg.theme('DarkAmber')


    layoutCalc = [  
        [sg.Text('Bem Vindo '),sg.Text(size=(4,1),key='name'),sg.Text(' a calculadora Cientifica em Python')],
        [sg.Text(key='telinhavalores')],
        [sg.Button('C'),sg.Button('^'),sg.Button('%'),sg.Button('/')],
        [sg.Button('7'),sg.Button('8'),sg.Button('9'),sg.Button('X')],
        [sg.Button('4'),sg.Button('5'),sg.Button('6'),sg.Button('-')],
        [sg.Button('1'),sg.Button('2'),sg.Button('3'),sg.Button('+')],
        [sg.Button('SAIR'),sg.Button('0'),sg.Button(','),sg.Button('=')]]

    windowCalc = sg.Window('Tela Calculadora',layoutCalc,finalize=True)
    return windowCalc


janela1,janela2 = janelaicial(), None

while True:
    window,event,value = sg.read_all_windows()
    print(window,event,value)

    if window == janela1 and event == sg.WIN_CLOSED or event == 'Cancelar': #fechar janela oa clicar no "X"
        break
    
    if window == janela1 and event == 'OK':
        janela2 = janelaCalculadora()
        janela2['name'].update(value['Name'])
        janela1.hide()

    if window == janela2 and event == 'Sair':
        break
    
    if window == janela2 and event >= '0' or event <='9' or event == ',' and event != 'SAIR':
        dados + event
       janela2['telinhavalores'].update()

    if window == janela2 and event == 'SAIR' and event == sg.WIN_CLOSED:
        janela1.close()
        break
