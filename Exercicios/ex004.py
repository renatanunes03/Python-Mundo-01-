print('{:20}'.format('Exercício 07'))
print('{:=^20}!'.format('DESAFIO 03'))
print('Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo '
      'primitivo e todas as informações possíveis sobre ele')

n = (input('Digite algo: '))
print('O tipo primitivo desse valor é {}'.format(type(n)))
print('É um número? {}'.format(n.isnumeric())) ## ou
print ('É alfabético? {}'.format(n.isalpha()))
print('É alfanumérico? {}'.format(n.isalnum()))
print('Está em maiuscúlo?{}'.format(n.isupper()))
print('Está em minuscúlo? {}'.format(n.islower()))
print('Possui espaço? {}'.format(n.isspace()))
