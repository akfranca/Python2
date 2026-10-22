"""Crie um programa que leia dois valores e mostre um MENU na tela:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA
Seu programa deverá realizar a operação solicitada em cada caso."""

from time import sleep
num1 = int(input('Digite o 1º primeiro valor: '))
num2 = int(input('Digite o 2º segundo valor: '))
opcao = 0
while opcao != 5:
    sleep(1)
    print('========= MENU ======='.center(50))
    print("""
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA""")
    print('')
    sleep(2)
    opcao = int(input('Qual opção desejada? '))
    if opcao == 1:
        print('SOMAR...')
        soma = num1 + num2
        sleep(1)
        print('A soma entre {} e {} é {}.'.format(num1, num2, soma))
    elif opcao == 2:
        print('MULTIPLICAR...')
        mult = num1 * num2
        sleep(1)
        print('{} x {} = {}'.format(num1, num2, mult))
    elif opcao == 3:
        print('MAIOR...')
        sleep(1)
        if num1 > num2:
            print('O numero {} é maior que o numero {}.'.format(num1, num2))
        elif num1 == num2:
            print('Os dois números são iguais')
        else:
            print('O numero {} é maior que o numero {}.'.format(num2, num1))
    elif opcao == 4:
        print('NOVOS NUMEROS...')
        sleep(1)
        novo_num1 = int(input('Digite o 1º primeiro valor: '))
        novo_num2 = int(input('Digite o 2º segundo valor: '))
        num1 = novo_num1
        num2 = novo_num2
    elif opcao == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção inválida, tente novamente...')

print('Obrigada por usar o programa, até a próxima...')






