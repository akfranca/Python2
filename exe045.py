
import time
import random
print("""===============
\033[1;7;30;42mJO KEN PO!!!\033[m
===============""")
time.sleep(1)
print("""OPÇÕES DE JOGADAS:
[0] PEDRA
[1] PAPEL
[2] TESOURA""")
time.sleep(1)
jogada = int(input('Qual sua jogada? '))

print('\033[31mJO\033[m')
time.sleep(1)
print('\033[33mKEN\033[m')
time.sleep(1)
print('\033[32mPO!!!\033[m')
time.sleep(1)

opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
cpu = random.choice(opcoes)

print('JOGADOR ESCOLHEU {}'.format (opcoes[jogada]))
print('COMPUTADOR ESCOLHEU {}'.format (cpu))

if cpu == opcoes[jogada]:
    print('EMPATE')
elif cpu == 'PEDRA' and opcoes[jogada] == 'PAPEL':
    print('JOGADOR VENCEU')
elif cpu == 'TESOURA' and opcoes[jogada] == 'PEDRA':
    print('JOGADOR VENCEU')
elif cpu == 'PAPEL' and opcoes[jogada] == 'TESOURA':
    print('JOGADOR VENCEU')
else:
    print('COMPUTADOR VENCEU')
