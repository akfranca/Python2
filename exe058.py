"""Melhore o jogo do desafio 028 onde o computador vai
"pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer."""

import random
from time import sleep
import emoji
print('VAMOS JOGAR ADIVINHA?')
sleep(2)
print(emoji.emojize('Vou pensar em um número de 0 a 10!:thinking_face:'))
sleep(2)
cpu = random.randint(0, 10)
num = -1
cont = 0
while cpu != num:
    num = int(input('Em qual número eu pensei? '))
    cont += 1
    if cpu == num:
        print('PROCESSANDO...')
        sleep(3)
        print(emoji.emojize('UAAL :exploding_head:! Você disse {} e eu pensei em {}. PARABÉNS!'.format(num, cpu)))
    if cpu != num:
        print('PROCESSANDO...')
        sleep(3)
        print(emoji.emojize('Que pena :disappointed_face: ! Mas você pode tentar novamente...'))
        sleep(1)

print(emoji.emojize('Você tentou {} vezes até acertar. :face_with_hand_over_mouth:'.format(cont)))






