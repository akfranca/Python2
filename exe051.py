"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final mostre os 10 primeiros termos dessa progressão."""


termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

for c in range(1, 11):
    print('{} -> {}'.format(termo, termo + razao))
    termo += razao
print('FIM')





