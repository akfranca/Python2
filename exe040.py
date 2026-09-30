"""Crie um programa que leia duas notas de um aluno calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

-Média abaixo de 5.0: REPROVADO
-Média entre 5.0 e 6.9: RECUPERAÇÃO
-Média 7.0 ou superior: APROVADO"""

print("\033[1;44m------MÉDIA ESCOLAR------\033[m")

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1 + nota2) / 2

if media < 5.0:
    print("Sua média foi {} e você está \033[1;31mREPROVADO!\033[m".format(media))
elif media >= 5.0 and media <= 6.9:
    print("Sua média foi {} e você está em \033[1;33mRECUPERAÇÃO!\033[m".format(media))
elif media >= 7.0:
    print("Sua média foi {} e você está \033[1;32mAPROVADO!\033[m".format(media))
