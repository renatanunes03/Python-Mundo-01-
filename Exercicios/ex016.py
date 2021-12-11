from math import floor
print('{:^40}'.format('Exercício 016'))
print('{:=^40}'.format('QUEBRANDO UM NÚMERO'))
print('Crie um programa que leia um número real qualqer \n'
      'e mostre na tela sua porção inteira.')
n = float(input('Digite um valor flutuante: '))
print('O valor digitado é {} e sua porção inteira é {}'.format(n, floor(n)))
''' Outras respostas:
Sem precisar importar a lib math receber um float no input e na resposta escrever com int(n)
Ou receber um float no input e no print usar no n {:.0f}
'''

#floor arredonda pra baixo