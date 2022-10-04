#4- Faça um Programa que peça um número correspondente a um determinado ano e em seguida
#informe se este ano é ou não bissexto.

anobi = int(input("Digite um ano: "))
if anobi % 4 == 0:
    print("O ano digitado é bissexto")
else:
    print("O ano escolhido não é bissexto!")
