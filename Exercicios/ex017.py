from math import hypot
print('{:^40}'.format('Exercício 017'))
print('{:=^40}'.format('CATETOS E HIPOTENUSA'))
print('Faça um programa que leia o comprimento do cateto oposto e do\n'
      'cateto adjacente de um triangulo retângulo, calcule e mostre o \n'
      'comprimento da hipotenusa.')
co = float(input('Qual o comprimento do cateto oposto: '))
ca = float(input('Qual o comprimento do cateto adjacente: '))
print('O comprimento da hipotenusa é {:.2f}.'.format(hypot(co,ca)))
''' Sem utilizar a lib math:
hipotenusa = (co ** 2 + ca ** 2) ** (1/2)
 
'''