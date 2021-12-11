print('{:^40}'.format('Exercício 32'))
print('{:=^40}'.format('ANO BISSEXTO'))
print('Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.')

from datetime import date

a = int(input("Digite um ano: "))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 400 == 0:
    print('O ano {} é BISSEXTO'.format(a))
else:
    print('O ano {} não é BISSEXTO'.format(a))
