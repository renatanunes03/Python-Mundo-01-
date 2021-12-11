print('Faça um programa que leia o nome completo de uma pessoa,\n mostrando em seguida o primero'
      'e o último nome separadamente.')
nome = str(input('Digite seu nome completo: ')).strip().title().split()
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[-1]}.')
# Posso usar também o len na última resposta
# print(f'Seu último nome é {nome[len(nome)-1]}.')