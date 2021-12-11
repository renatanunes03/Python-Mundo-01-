print('{:^40}'.format('Exercício 33'))
print('Maior e menor valores')
print('Faça um  programa que leia três números e mostre qual é o maior e qual é o menor.')
from time import sleep

print('Pense em três número')
sleep(2)
print('Pensou?...')
sleep(1)
n1 = int(input('Primero número...'))
n2 = int(input('Segundo número...'))
n3 = int(input('Terceiro número...'))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
    print('O menor valor digitado foi {}.'.format(menor))
    print('O maior valor digitado foi {}'.format(maior))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))

'''maior = max(n1, n2, n3)
menor = min(n1, n2, n3)
print('O menor número é {}.'.format(menor))
print('O maior número é {}.'.format(maior))'''

