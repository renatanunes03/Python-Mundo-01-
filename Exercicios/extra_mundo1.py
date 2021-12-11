print('\033[1;43mOlá, Mundo!\033[m')
a = 3
b = 5
print(f'Os valores são \033[31m{a}\033[m e \033[35m{b}\033[m')
cores = {
    'limpa':'\033[m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'pretoebranco': '\033[7m'
}
nome = 'Renatinha'
print('Olá, mundo! Meu nome é {}{}{}'.format(cores['pretoebranco'], nome, cores['limpa']))

#\033[aqui eu incluo o c´pdigo de formatação e separo com ;m
#\033[0;33;44m
# código para style 0(none) , 1(bold/negrito) , 4(underline/sublinhado) , 7(negative/inverte a cor da letra com o fundo)
# código para cor do text, 30(black), 31(red), 32(green), 33(yellow), 34(blue), 35(magenta), 36(cyan), 37(grey), 97(white)
# código para back/fundo 40(black), 41(red), 42(green), 43(yellow), 44(blue), 45(magenta), 46(cyan), 47(grey), 107(white)