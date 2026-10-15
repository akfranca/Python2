"""Faça um programa que calcule a soma entre todos os numeros ímpares que são
multiplos de três e que se encontram no intervalo de 1 até 500."""

soma = 0
for c in range(3, 501, 6):
    soma += c
print('A somatória de todos os números ímpares divisíveis por três é: {}'.format(soma))


