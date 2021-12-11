print('{:40}'.format('Exercício 012'))
print('{:=^40}.'format('CALCULANDO DESCONTO'))
print('Faça um algoritmo que leia o preço de um \nproduto e mostre seu'
      'novo preço, com 5% de desconto.')
preco = float(input('Preço do produto: '))
desc = preco * 0.05
novo_preco = preco - desc
print('Você terá um desconto de R${}. Total da compra, com desconto, será R${}'.format(desc, novo_preco))