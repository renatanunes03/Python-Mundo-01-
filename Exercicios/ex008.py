print(f'{"Exercício 008":^40}')
print(f'{"CONVERSOR DE MEDIDAS":=^40}')
print('Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros')
m = int(input('Quantos metros: '))
cen = m * 100
mil = m * 1000
print('Temos {} metro(s) e logo temos {} cm e {} mm'.format(m, cen, mil))
