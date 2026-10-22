"""Escreva um programa que leia um numero n inteiro quaquer e
mostre na tela os n primeiros elementos de uma sequência
Fibonacci.
EX: 0 → 1 → 1 → 2 → 3 → 5 → 8"""

print('SEQUÊNCIA FIBONACCI'.center(50))
num_int = int(input('Digite um numero: '))
n1 = 0
n2 = 1
soma = 0
for cont in range(1, num_int + 1):
    print(n1, end=' -> ')
    soma = n1 + n2
    n1 = n2
    n2 = soma
print('FIM')
