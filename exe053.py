"""Crie um programa que leia uma frase qualquer e diaga se ela é
um palídromo, desconsiderando os espaços."""

frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.replace(' ', '')
inverso = ''

for letra in range(len(frase)-1, -1, -1):
    inverso += frase[letra]
if frase == inverso:
    print('Sua frase é: {} e ao contrário fica {} então ela é um PALÍNDROMO!'.format(frase, inverso))
else:
    print('Sua frase é: {} e ao contrário fica: {} então ela NÃO É UM PALÍNDROMO!'.format(frase, inverso))









