"""Escreva um programa que leia dois numeros inteiros e compare-os,
mostrando na tela uma mensagem:

-O primeiro valor é maior
-O segundo valor é maior
-Não existe valor maior, os dois são iguais"""

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

print("\033[1;7;40m------COMPARADOR DE NUMEROS------\033[m")

if num1 > num2 :
    print("Entre o numero {} e {} o numero {} é MAIOR".format(num1, num2, num1))
elif num1 == num2 :
    print("Não existe valor maior, os dois numeros são iguais")
else:
    print("Entre o numero {} e {} o numero {} é MAIOR".format(num1, num2, num2))

