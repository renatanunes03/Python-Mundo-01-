print('Faça um progrmaa que leia um  número de 0 a 9999 e mostre na tela cada um '
      'dos dígitos separados.')
n = int(input('Digite um número de 0 a 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'Sua unidade é {u}.')
print(f'Sua dezena é {d}.')
print(f'Sua dezena é {c}.')
print(f'Seu milhar é {m}.')
# ex número  1834
'''
usar o split e pedir por 0, 1 2 3
unidade: 4
dezena: 3
centena: 8
milhar: 1
'''