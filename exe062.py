"""Melhore o desafio 061, perguntando ao usuário
se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos."""


print(('='*20).center(50))
print('GERADOR DE PA'.center(50))
print(('='*20).center(50))
termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
c = 0
total = 10
c2 = 0
while c < total:
    c += 1
    print('{}'.format(termo1), end=' -> ')
    termo1 += razao
print('PAUSA')
res = int(input('\nQuantos termos deseja mostrar a mais? '))
while res != 0:
    c2 = 0
    while c2 < res:
        c2 += 1
        print('{}'.format(termo1), end=' -> ')
        termo1 += razao
    print('PAUSA')
    res = int(input('\nQuantos termos deseja mostrar a mais? '))
print('FIM')

