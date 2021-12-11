print('{:^40}'.format('Exercício 35'))
print('Analisando Triângulo')
print('Desenvolva um programa que leia o comprimento de três retas e diga ao\n'
      'usuário se elas podem ou não formar um triângulo.')
r0 = float(input('Digite o valor da primeira reta: '))
r1 = float(input('Digite o valor da segunda reta: '))
r2 = float(input('Digite o valor da terceira reta: '))

if (r0 + r1) < r2 and (r2 + r1) > r0:
      print('Não temos um triângulo')
else:
      print('Temos um triângulo')

# pesquisar sobre triângulo