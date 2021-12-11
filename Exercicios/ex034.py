print('{:^40}'.format('Exercício 34'))
print('{:=^40}'.format('Aumentos múltiplos'))
print('Escreva um programa que pergunte o salário de um \n'
      'funcionário e calcule o valor de seu aumento.'
      'Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.\n'
      'Para os inferiores ou iguais, o aumento é de 15%.')

# if a paritr de 1.2500,00 else para inferiores ou iguais.

s = float(input('Qual seu salário? '))
if s <= 1250:
      aumento = s + (s * 0.15)
      print(f'Seu salário era de {s:.2f} e agora você recebe R${aumento:.2f}, um aumento de 15%.')
else:
      aumento = s + (s * 0.10)
      print(f'Seu salário era de{s:.2f} e agora você recebe R${aumento:.2f}, um aumento de 15%.')