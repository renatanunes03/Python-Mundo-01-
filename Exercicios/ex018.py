from math import cos,tan, sin, radians
print('{:^40}'.format('Exercício 018'))
print('{:=^40}'.format('SENO, COSSENO E TANGENTE'))
print('Faça um programa que leia um ângulo qualquer e mostre na tela \n'
      'o valor do seno, cosseno e tangente desse ângulo.')
a = float(input('Qual o ângulo? '))
rad = radians(a)
cosseno = cos(rad)  '''cos(radians(a))'''
tang = tan(rad)   '''tan(radians(a))'''
seno = sin(rad)    '''sin(radians(a)) '''
print(f'O valor do seu seno é {seno:.2f}, do seu cosseno {cosseno:.2f} e tangente {tang:.2f}')

'''Na documentação do python.org o cos, tan e sin me dá o resultado
em radianos e tenho que chamar o radians para converter o angulo do input em radianos.
porderia import math e seno = math.sin(math.radians(a)), tang = math.tan(math.radians(a))
cosseso = math.cos(math.radians(a))
'''