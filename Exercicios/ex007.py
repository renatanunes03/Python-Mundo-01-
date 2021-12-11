print(f'{"Exercício 007":^40}')
print(f'{"MÉDIA ARITMÉTICA":=^40}')
print('Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.')
nota1 = float(input('Primeira nota do aluno? '))
nota2 = float(input('Segunda nota do aluno? '))
media = (nota1 + nota2) / 2
print(f'A média entre {nota1:.1f} e {nota2:.1f} é {media:.1f}.')