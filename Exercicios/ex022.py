print('Crie um programa que leia o nome completo de uma pessoa e mostre:'
       'O nome com todas as letras maiúsculas.'
       'O nome com todas as letras minúsculas.'
       'Quantas letras ao todo(sem considerar espaços).'
       'Quantas letras tem o primeiro nome. ')

name = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em letras maiúscula fica: {name.upper()}.')
print(f'Seu nome em letras minúscula fica: {name.lower()}.')
espaco = name.count(' ')
carac = len(name) - espaco
print(f"Possui {carac} letras, sem contar os espaços.") # ou len(name) - nome.count(' ')
esplit = name.split()
print(f'Seu primeiro nome é {esplit[0]} e possui {len(esplit[0])} letras.') # ou posso usar o find
# name.find(' ') find encontra e me mostra a posição encontrada


