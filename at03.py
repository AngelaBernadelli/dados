# 3- Faça
# um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a
# temperatura em graus Celsius. C = 5 * ((F-32) / 9).

fah = float(input("Digite a temperatura em Fahrenheit: "))
conversao = (5 * ((fah - 32) / 9))
print(f"A Temperatura {fah} ºF em graus Celsius é {conversao}")