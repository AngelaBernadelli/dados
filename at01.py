#1 - Faça um programa para leitura de
#três notas parciais de um aluno. O programa deve calcular a média alcançada por
#aluno e apresentar:

nota1 = float(input('Digite a nota da primeira prova:',))
nota2 = float(input('Digite a nota da segunda prova:',))
nota3 = float(input('Digite a nota da terceira prova:',))

media =(nota1+nota2+nota3) / 3

if media >= 7 and media <10:
              print(f'Parabéns. Aluno aprovado com {media} de média.')

elif media ==0 or media <7:
    print(f'Aluno reprovado com {media} de média.')

elif media == 10:
    print(f'Parabens. Aluno aprovado com distinsão! {media} de média.')

else:
    print('Erro na entrada de dados.')


print(input('Precione "enter" para sair'))