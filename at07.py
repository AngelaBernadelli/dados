#7- Reverso
#do número. Faça uma função que retorne o reverso de um número inteiro
#informado



numero = str(input('Digite um número: ')).strip()
reverso = str(numero[::-1])
print(f'Reverso: {reverso}')