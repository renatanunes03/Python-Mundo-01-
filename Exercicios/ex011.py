print('{:^40}'.format('Exercício 011'))
print('{:=^40}'.format('PINTANDO PAREDE'))
print('Faça um programa que leia a largura e a altura de uma parede em metros,'
      'calcule a sua área e a \nquantidade de tinta necessária para pinta-la,'
      'sabendo que cada litro de tinta, pinta uma área de 2m².\n')
a = float(input('Quantos metros de altura possui a parede? '))
l = float(input('Quantos metros de  largura possui a parede?' ))
area = a * l
litro = area / 2
print('A parede possui {:.2f} m², sendo {} de altura e {} de largura, e precisamos de {:.2f} litros de tinta para pinta-la'.format(area,a,l, litro))