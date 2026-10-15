
import time
import random
print("""===============
\033[32mJO KEN PO!!!\033[m
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

print('-=-'* 10)
print('\033[32mJOGADOR\033[m ESCOLHEU \033[32m{}\033[m'.format (opcoes[jogada]))
print('\033[33mCOMPUTADOR\033[m ESCOLHEU \033[33m{}\033[m'.format (cpu))
print('-=-'* 10)

if cpu == opcoes[jogada]:
    print('\033[31mEMPATE\033[m')
elif cpu == 'PEDRA' and opcoes[jogada] == 'PAPEL':
    print('\033[32mJOGADOR VENCEU\033[m')
elif cpu == 'TESOURA' and opcoes[jogada] == 'PEDRA':
    print('\033[32mJOGADOR VENCEU\033[m')
elif cpu == 'PAPEL' and opcoes[jogada] == 'TESOURA':
    print('\033[32mJOGADOR VENCEU\033[m')
else:
    print('\033[33mCOMPUTADOR VENCEU\033[m')
