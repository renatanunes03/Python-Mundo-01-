from random import sample

print('{:^40}'.format('Exercício 020'))
print('{:=^40}'.format('SORTEANDO UMA ORDEM NA LISTA'))
print('O mesmo professor do desafio anterior quer sortear a ordem de apresentação\n'
      'de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.')
alu1 = str((input('Primeiro aluno? ')))
alu2 = str((input('Segundo aluno? ')))
alu3 = str((input('Terceiro aluno? ')))
alu4 = str((input('Quarto aluno? ')))
lista = [alu1, alu2, alu3, alu4]
s = sample(lista, 4, counts=None)
print(f'Os alunos escolhidos na sequência são {s}')


''' É possível também usar usando o import sufle e random.shufle(lista)
No sample é possível escolher a quantidade de vezes que quero sortear, no caso 15 vezes substituindo o numero 4 em sample(lista, 4, counts=None)'''
