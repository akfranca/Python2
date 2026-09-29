"""Escreva um programa que leia um numero inteiro qualquer e
peça para o usuário escolher qual será a base de conversão:

-1 para binário
-2 para octal
-3 para hexadecimal"""

num = int(input("Digite um numero? "))

binario = bin(num)
octal = oct(num)
hexa = hex(num)

print("ESCOLHA A BASE")
print("[1] BINÁRIO")
print("[2] OCTAL")
print("[3] HEXADECIMAL")

base = int(input("Digite sua base? "))

if base == 1:
    print(binario)
elif base == 2:
    print(octal)
elif base == 3:
    print(hexa)
else:
    print("Escolha inválida")


