"""Faça um programa que mostre na tela uma contagem regressiva
para estou de fogos de artifício, indo de 10 até 0, com
pausa de 1 segundo entre eles"""

print('\033[32m' + 'CONTAGEM REGRESSIVA PARA ANO NOVO'.center(60, '=')+ '\033[m')

import emoji
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize(':fireworks: \033[32mFELIZ ANO NOVO\033[m :fireworks:'))








