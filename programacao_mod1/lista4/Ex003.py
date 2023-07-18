'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir
os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

a) Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir
os demais valores, sendo encerrado;

b) Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;

c) Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;

d) Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''
a = int(input("Digite A: "))
if a == 0:
  print("Não é possível resolver equação de 2 grau")
  print("Programa finalizado")
else:
  b = int(input("Digite B: "))
  c = int(input("Digite C: "))
  delta = b**2-(4*a*c)
  if delta < 0:
    print("As raízes não são reais")
  elif delta == 0:
    print("1 raiz: ", x1 = (-b+(delta**0.5)) / (2*a))
  else:
    x1 = (- b + (delta**0.5)) / (2*a)
    x2 = (- b - (delta**0.5)) / (2*a)
    print("1 raiz: ", x1, '\n', "2 raiz",x2)