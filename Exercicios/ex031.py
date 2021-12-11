print('{:^40}'.format('Exercício 31'))
print('{:=^40}'.format('Cust0 da viagem'))
print('Desenvolva um programa que pergunte a distância de uma viagem em km.'
      'Calcule o preço da passagem, cobrando R$0,50 por km \n'
      'para viagens de até 200km e R$ 0,45 para viagens mais longas')

d = float(input('Qual o distância da sua viagem? '))
f = ('Você está prestes a embarcar em uma viagem de {:.2f}.'.format(d))
if d <= 200:
      p = d * 0.50
      print(f)
      print('O custo de sua viagem será de R${:.2f}.'.format(p))
else:
      print(f)
      p = d * 0.45
      print('O custo de sua viagem será de R${:.2f}'.format(p))


#p = d * 0.50 if distancia <= 200 else d * 0.45