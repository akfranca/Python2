"""Faça um programa que leia um numero inteiro
e diga se ele é ou não um numero primo."""

num = int(input('Digite um número: '))
contador = 0
for n in range(1, num + 1):
    resto = num % n
    if resto == 0:
        contador += 1
if contador == 2:
    print('O numero {} é um número PRIMO!'.format(num))
else:
    print('O numero {} NÃO É PRIMO!'.format(num))



