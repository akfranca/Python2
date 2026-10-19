"""Crie um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos."""


for c in range(1, 6):
    peso = float(input('Digite o peso em KG: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O MAIOR peso entre os cinco é {:.1f}.'.format(maior))
print('O MENOR peso entre os cinco é {:.1f}.'.format(menor))


