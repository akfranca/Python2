"""Faça um programa que calcule a soma entre todos os numeros ímpares que são
multiplos de três e que se encontram no intervalo de 1 até 500."""

soma = 0
cont = 0
for c in range(3, 501, 6):
    if c % 3 == 0:
        cont += 1
    soma += c
print('A somatória dos {} números ímpares divisíveis por três é: {}'.format(cont,soma))


