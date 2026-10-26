"""Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo."""

from time import sleep
from random import randint
print('-'*30)
print('JOGO PAR OU ÍMPAR')
print('-'*30)
sleep(1)
print('Vamos jogar par ou ímpar?')
soma = 0
vezes = 0
while True:
    num = int(input('Digite um número de 0 a 10: '))
    resp = str(input('Você escolhe PAR ou ÍMPAR [P/I]: ')).strip().upper()
    print('-'*30)
    cpu = randint(0, 10)
    soma = num + cpu
    resul = ''
    if soma % 2 == 0:
        print(f'Você digitou {num} e eu {cpu}, total {soma}')
        print(f'{soma} é um numero PAR')
        if resp == 'P':
            vezes += 1
            print('Você VENCEU :)')
            print('Vamos jogar novamente...')
            print('-'*30)
            resul = 'VENCEU'
        else:
            print('Você PERDEU :(')
            print('-'*30)
            resul = 'PERDEU'
    if soma % 2 == 1:
        print(f'Você digitou {num} e eu {cpu}, total {soma}')
        print(f'{soma} é um numero ÍMPAR')
        if resp == 'I':
            vezes += 1
            print('Você VENCEU :)')
            print('Vamos jogar novamente...')
            print('-'*30)
            resul = 'VENCEU'
        else:
            print('Você PERDEU :(')
            print('-'*30)
            resul = 'PERDEU'
    if resul == 'PERDEU':
        break
print(f'GAME OVER! Você venceu {vezes} vezes.')



