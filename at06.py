#6 - Faça
#um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação
#no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem
#lida.

idade = []
altura = []

for n in range(1, 4):
    i = int(input('Digite a idade: '))
    a = float(input('Digite a altura: '))
    idade.append(i)
    altura.append(a)

idd = idade[::-1]
alt = altura[::-1]
print(f"Lista de entrada da idade, {idade}")
print(f"A lista da idade invertida, {idd}")
print(f"Lista de entrada da altura, {altura}")
print(f"A lista da altura invertida, {alt} ")
