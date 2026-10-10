
import time
import random
print("""OPÇÕES DE JOGADAS:
[0] PEDRA
[1] PAPEL
[2] TESOURA""")
jogada = int(input('Qual sua jogada? '))

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
time.sleep(1)

opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
cpu = random.randint(0, 2)

print('JOGADOR ESCOLHEU {}'.format (jogada))
print('COMPUTADOR ESCOLHEU {}'.format (cpu))






