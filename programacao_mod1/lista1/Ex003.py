'''
3 Qual a quantidade de caracteres nas seguintes frases, faça cada uma ser
  armazenada em uma variável diferente.
Brasil Hexa 2006
Você nasceu em 29 de Outubro de 19731
Campus Party 2023
'''
nome = str(input('Digite uma das 3 frase acima: ')).strip()
separa = nome.split()

print('A frase digitada tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))