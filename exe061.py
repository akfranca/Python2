"""Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando
estrutura while."""

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
c = 0
while c < 10:
    c += 1
    print('{}'.format(termo + razao), end=' -> ')
    termo += razao


