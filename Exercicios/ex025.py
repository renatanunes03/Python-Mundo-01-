print('Crie um programa que leia o nome de uma pessoa \n'
      'e diga se ela se tem SILVA no nome.')
nome = str(input('Digite seu nome completo: ')).strip().upper().split()
print('SILVA' in nome)

# retornar true or false