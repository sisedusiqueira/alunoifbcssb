'''
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido
'''

dia = int(input("Digite um número de 1 a 7: "))

if dia == 1:
  print("1 - DOMINGO")
elif dia == 2:
  print("2 - SEGUNDA")
elif dia == 3:
  print("3 - TERÇA")
elif dia == 4:
  print("4 - QUARTA")
elif dia == 5:
  print("5 - QUINTA")
elif dia == 6:
  print("6 - SEXTA")
elif dia == 7:
  print("7 - SÁBADO")
else:
  print("VALOR INVÁLIDO")