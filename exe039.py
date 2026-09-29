"""Faça um programa que leia o ano nascimento de um jovem e informe,
de acordo com sua idade:

-Se ainda vai se alistar ao serviço militar.
-Se é a hora de se alistar.
-Se já passou do tempo de alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date
alistam = date.today()

nasc = int(input("Digite sua data de nascimento: "))
idade = alistam.year - nasc
print("Ano de nascimento: {} e você tem {} anos.".format(nasc, idade))

ano_alistam = alistam.year
alistado = idade - 18
novo = 18 - idade

if idade > 18:
    print("Era para você ter se alistado a {} anos atrás".format(alistado))
    print("Seu alistamento foi em {}!".format(ano_alistam - alistado))
elif idade < 18:
    print("Ainda faltam {} anos para o alistamento".format(novo))
    print("Seu alistamento será em {}!".format(ano_alistam + novo))
elif idade == 18:
    print("Você deve se alistar IMEDIATAMENTE!")











