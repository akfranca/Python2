"""Faça um programa que mostre a tabuada de vários números,
um de cada vez para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo."""


print('-' * 30)
print('PROGRAMA DE TABUADA')
print('-' * 30)
cont = 1
num = int(input('Digite um número para saber sua tabuada: '))
while True:
    while cont <= 10:
        print(f'{num} x {cont} = {num * cont}')
        cont += 1
    num = int(input('Digite um número para saber sua tabuada: '))
    if num < 0:
        break



