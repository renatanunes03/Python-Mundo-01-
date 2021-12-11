print('Escreva um programa que leia a velocidade de um carro.\n'
      'Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.\n'
      'A multa vai custar R$7,00 por cada km acima do limite.')
v = float(input('Qual a velocidade do veículo: '))
if v > 80:
      m = v - 80
      valor = m * 7
      print('Você será multado em R${:.2f}.'.format(valor))
else:
      print('Tenha um ótimo dia! Dirija com segurança!')

