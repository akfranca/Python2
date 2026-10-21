"""Crie um programa que leia um numero qualquer e
mostre seu fatorial.
ex: 5! = 5x4x3x2x1 = 120"""

n = int(input('Digite um número para saber seu fatorial: '))
cont = 1
num = n
while n >= 1:
    cont = cont * n
    n -= 1
print('O fatorial de {} é: {}...'.format(num, cont))





