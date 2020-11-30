'''
Calculadora cientifica Pyhton

by Felipe Ales.
'''

print ('Inciando Calculadora')
name= input('Insira seu nome: ')

print(f'Olá {name}, Bem vinda a calculadora Cientifica em Python')

while True:
    print ('''Escolha uma operação:
    * Multiplicação
    / Divisão
    + Soma
    - Subtração 
    ^ Exponenciação (O segundo número que vai elevar o primeiro exemplo 2^3 = 8)
    ** Raiz (O segundo número que vai ser a raiz o primeiro exemplo 3**3 = 1)''')

    operacao = input('Qual operação deseja fazer? ')

    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))

    if operacao == '*':
        result = num1 * num2
        print (f'{num1} x {num2} = {result}')

    elif operacao == '/':
        result = num1 / num2
        print (f'{num1} / {num2} = {result}')

    elif operacao == '+':
        result = num1 + num2
        print (f'{num1} + {num2} = {result}')

    elif operacao == '-':
        result = num1 - num2
        print (f'{num1} - {num2} = {result}')

    elif operacao == '^':
        result = num1 ** num2
        print (f'{num1} ^ {num2} = {result}')

    elif operacao == '**':
        if num2 == 0:
            result = num1 ** 1/2
            print (f'{num1} ^ 1/2 = {result}')
        else:
            result = num1 ** 1/num2
            print (f'{num1} ^ 1/{num2} = {result}')

    if result == 31100:
        print ('''Olá meu nome é Felipe Ales, Criei esta calculadora para usar alguns conhecimento em Python, uma linguagem inovadora e muito fácil de se usar espero que esteje gostando.
        Adios''')
    
    retorno = input('Deseja Continuar: y/n ')
    if retorno == 'n':
        break
