#5 - Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro
# informado pelo usuário.


numeral = int(input("Digite um número: "))
lista = []

for i in range(numeral + 1):
    if i % 2 == 1 and i != 2:
        lista.append(i)
else:
    print("Números primos: ", lista)