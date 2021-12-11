from random import choice
print('{:^40}'.format('Exercício 019'))
print('{:=^40}'.format('SORTEANDO UM ITEM NA LISTA'))
print('Um professor quer sortear um dos seus quatro alunos para apagar o quadro.\n'
      'Faça um programa que ajuda ele, lendo o nome deles e escrevendo o nome do escolhido.')
alu1 = str((input('Primeiro aluno? ')))
alu2 = str((input('Segundo aluno? ')))
alu3 = str((input('Terceiro aluno? ')))
alu4 = str((input('Quarto aluno? ')))
lista = [alu1, alu2, alu3, alu4]
print(f'O aluno escolhido foi: {choi(lista)}')
