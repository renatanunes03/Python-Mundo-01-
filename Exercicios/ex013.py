print('{:^40}'.format('Exercício 013'))
print('{:=^40}'.format('REAJUSTE DE SALÁRIO'))
print('Faça um algoritmo que leia o salário de um funcionário\n'
      'e mostre seu novo salário, com 15% de aumento.')
sal = float(input('Qual seu salário hoje? R$ '))
aumento = sal * 15 / 100
novo_sal = sal + aumento
print('Seu salário era de {:.2F}. Você recebeu um aumento de 15%, r${:.2F}.\nO SEU novo salário será de R${:.2F}.'.format(sal, aumento, novo_sal))