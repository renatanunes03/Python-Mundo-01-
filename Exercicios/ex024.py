print('Crie um programa que leia o nome de uma '
      'cidade e diga se ela começa ou não com o nome SANTO. ')
cid = str(input('Digite o nome de uma cidade: ')).strip().split()

print(cid[0].upper() == "SANTO")

print('Crie um programa que leia o nome de uma pessoa \n'
      'e diga se ela se tem SILVA no nome.')
nome = str(input('Digite seu nome completo: ')).strip().split()
#print('Seu nome tem Silva? {}'.format("SILVA" in nome.upper()))

print('SANTO' in nome.upper())

# retornar true or false