print('{:^40}'.format('Exercício 015'))
print('{:=^40}'.format('ALUGUEL DE CARROS'))
print('Escreva um programa que pergunte a quantidade de km percorridos por um carro\n'
      'alugado e a quantidade de dias pelos quais ele foi alugado.\n'
      'Calcule o preço a pagar, sabendo que o carro custa R$60por dia e R$0,15 por km\n'
      'rodado.')
d = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
valor_d = d*60.00
valor_km = km*0.15
total = valor_d + valor_km
print('Total a pagar é de R${:.2f}.'.format(total))