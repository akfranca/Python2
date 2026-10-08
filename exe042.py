"""Refaça o desafio 035 dos triangulos, acrescentando o recurso de mostrar
que tipo de triangulo será formado:

EQUILATERO: todos os lados iguais
ISÓSCELES: dois lados iguais
ESCALENO: todos os lados diferentes"""

r1 = float(input("Digite a primeira reta: "))
r2 = float(input("Digite a segunda reta: "))
r3 = float(input("Digite a terceira reta: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas PODEM FORMAR um triângulo', end=' ')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('As retas NÃO PODEM formar um triângulo')