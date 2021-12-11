print('{:^40}'.format('Exercício 010'))
print('{:=^40}'.format('CONVERSOR DE DÓLAR'))
print('Crie um programa que leia quanto dinheiro uma pessoa tem'
      'na carteira e mostre quantos dólares ela pode comprar.\n'
      'Considere US$=R$3,27')
din = float(input('Quanto você tem hoje na carteira? R$ '))
print('Você possui R${.:2f}, hoje é possível comprar US${:.2f} dólares'. format(din, din / 5.35))