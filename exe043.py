"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule o seu IMC e mostre seu status, de acordo com a tabela abaixo:

-Abaixo de 18.5: abaixo do peso
-Entre 18.5 e 25: peso ideal
-25 até 30: sobrepeso
-30 até 40: obesidade
-Acima de 40: obesidade mórbida"""

peso = float(input('Digite seu peso: (KG) '))
altura = float(input('Digite sua altura: (M) '))
imc = peso / altura ** 2

if imc < 18.5:
    status = 'ABAIXO DO PESO!'
elif 25 > imc >= 18.5:
    status = 'com PESO IDEAL!'
elif 30 > imc >= 25:
    status = 'com SOBREPESO'
elif 40 > imc >= 30:
    status = 'com OBESIDADE!'
else:
    status = 'com OBESIDADE MÓRBIDA!'

print('Seu IMC é de {:.1f} e você está {} '.format(imc, status))



