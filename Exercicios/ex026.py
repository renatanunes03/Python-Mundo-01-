print('Faça um programa que leia uma frase pelo teclado e mostre:'
      'Quantas vezes aparece a letra A.'
      'Em que posição ela aparece a primeira vez.'
      'Em que posição ela aparece na última vez.')
frase1 = str(input('Digite uma frase que irei contar quantos A possui: ')).strip().lower()
frase = frase1.replace('á','a').replace('á','a').replace('ã','a').replace('ã','a')
print(f'A frase acima possui {frase.count("a")} As.')
print(f'A letra A aparece pela primeira vez na posição {frase.find("a") + 1}.')
print(f'A última letra A aparece na posição {frase.rfind("a") + 1}.')
