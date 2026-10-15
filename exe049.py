"""Refaça o desafio 009, mostrando a tabuada de um número que
o usuário escolher, só que agora utilizando laço for."""

from time import sleep
print('TABUADA'.center(50))
num = int(input('Digite um número: '))
for c in range(1, 11):
    print(f'{num} x {c} = {num * c}')
    sleep(1)

