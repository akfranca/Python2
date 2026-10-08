"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule o seu IMC e mostre seu status, de acordo com a tabela abaixo:

-Abaixo de 18.5: abaixo do peso
-Entre 18.5 e 25: peso ideal
-25 até 30: sobrepeso
-30 até 40: obesidade
-Acima de 40: obesidade mórbida"""

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura ** 2

if imc < 18.5:
    status = 'ABAIXO DO PESO!'
elif imc >= 18.5 and imc <= 25:
    status = 'com PESO IDEAL!'
elif imc >= 25 and imc <= 30:
    status = 'com SOBREPESO'
elif imc >= 30 and imc <= 40:
    status = 'com OBESIDADE!'
else:
    status = 'com OBESIDADE MÓRBIDA!'

print('Seu IMC é de {:.1f} e você está {} '.format(imc, status))



