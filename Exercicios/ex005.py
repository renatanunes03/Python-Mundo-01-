print('{:^40}'.format('Exercício 005'))
print('{:=^40}'.format('ANTECESSOR E SUCESSOR'))
print('Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor')
num = int(input('Digite um número: '))
print('Você digitou {}, logo seu antecessor é {} e seu sucessor é {}.'.format(num, num - 1, num + 1))