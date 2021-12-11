from random import randint
from time import sleep
print('{:^40}'.format('Exercício 28'))
print('{:=^40}'.format('Jogo de Adivinhação'))
print('Escreva um programa que faça o computador "pensar" em um número inteiro\n'
      'entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido\n'
      'pelo computador. \n'
      'O programa deverá escrever na tela se o usuário vencer ou perdeu')
# Se acertar de-lhe os parabéns

i = int(input('Tente descobrir qual número eu pensei de 0 a 5: '))
print('PROCESSANDO. . .  ')
sleep(2)
escolhido = randint(0, 5)
if i == escolhido:
    print(f'Você erro, o número escolhido foi {escolhido}')
else:
      print('Algo deu errado, apenas números de 0 a 5')

