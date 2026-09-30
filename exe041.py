"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com sua idade:

-Até 09 anos: MIRIM
-Até 14 anos: INFANTIL
-Até 19 anos: JUNIOR
-Até 20 anos: SÊNIOR
-Acima: MASTER"""

from datetime import date
hoje = date.today()

print("\033[1;42m----CONFEDERAÇÃO NACIONAL DE NATAÇÃO----\033[m")

nasc = int(input("Digite o ano de nascimento: "))
idade = hoje.year - nasc

if idade <= 9:
    print("Você tem {} anos e está na categoria MIRIM".format(idade))
elif idade <= 14:
    print("Você tem {} anos e está na categoria INFANTIL".format(idade))
elif idade <= 19:
    print("Você tem {} anos e está na categoria JUNIOR".format(idade))
elif idade <= 20:
    print("Voê tem {} anos e está na categoria SÊNIOR".format(idade))
elif idade > 20:
    print("Você tem {} anos e está na categoria MASTER".format(idade))
