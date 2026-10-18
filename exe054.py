"""Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores. (CONSIDERE 21 ANOS)"""

from datetime import date
hoje = date.today().year
maiores = 0
menores = 0
for cont in range (1, 8):
    nasc = int(input('Digite o ano de nascimento: '))
    idade = hoje - nasc
    if idade >= 21:
        maiores +=1
    else:
        menores +=1
print('MAIORES TOTAL: {}'.format(maiores))
print('MENORES TOTAL: {}'.format(menores))



