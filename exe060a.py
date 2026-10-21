"""Crie um programa que leia um número qualquer e nostre seu fatorial.
ex: 5! = 5 x 4 x 3 x 2 x 1 = 120"""

n = int(input('Digite um numero para saber seu fatorial: '))
cont = 1
num = n
for c in range(n, 0, -1):
    print('{}x...'.format(c), end=' ')
    cont *= c
print('\nO fatorial de {} é: {}...'.format(num, cont))




