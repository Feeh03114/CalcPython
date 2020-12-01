'''
Calculadora cientifica Pyhton with interface

by Felipe Ales.
'''
import PySimpleGUI as sg


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
        [sg.Text(size=(1,1),key='name')],
        [sg.Text(key='telinhavalores',size=(4,1))],
        [sg.Button('C'),sg.Button('^'),sg.Button('%'),sg.Button('/')],
        [sg.Button('7'),sg.Button('8'),sg.Button('9'),sg.Button('*')],
        [sg.Button('4'),sg.Button('5'),sg.Button('6'),sg.Button('-')],
        [sg.Button('1'),sg.Button('2'),sg.Button('3'),sg.Button('+')],
        [sg.Button('SAIR'),sg.Button('0'),sg.Button('.'),sg.Button('=')]]

    windowCalc = sg.Window('Tela Calculadora',layoutCalc,finalize=True)
    return windowCalc


janela1,janela2 = janelaicial(), None
dados = ''
while True:
    window,event,value = sg.read_all_windows()

    if window == janela1 and event == sg.WIN_CLOSED or event == 'Cancelar': #fechar janela oa clicar no "X"
        break
    
    if window == janela1 and event == 'OK':
        janela2 = janelaCalculadora()
        janela2['name'].set_size((len('Bem Vindo ' + value['Name'] + ' a calculadora Cientifica em Python')-2,1))
        janela2['name'].update('Bem Vindo ' + value['Name'] + ' a calculadora Cientifica em Python')
        janela1.hide()

    if window == janela2 and event == 'Sair':
        break
    
    if window == janela2 and event != 'SAIR' and event != '=' and event != 'C':
        dados +=  event
        janela2['telinhavalores'].set_size((len(dados),1))
        janela2['telinhavalores'].update(dados)

    if window == janela2 and event == '=' and dados != '':
        janela2['telinhavalores'].update(eval(dados))

    if window == janela2 and event != 'SAIR' and event != '=' and event == 'C':
        dados = ''
        janela2['telinhavalores'].update(dados)
    
    if window == janela2 and event == 'SAIR' and event != '=' and event != 'C' and event == sg.WIN_CLOSED:
        janela1.close()
        break
