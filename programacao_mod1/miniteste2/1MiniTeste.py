'''
Miniteste 2

Desenvolver um algoritmo que leia a altura de 15 pessoas.
Este programa deverá calcular e mostrar.
A menor altura do grupo.
A maior altura do grupo.
'''

num_pessoas = 3
alturas = []
for i in range(num_pessoas):
  altura = input("Digite a altura da pessoa {}: ".format(i+1))
  alturas.append(altura)

menor_altura = min(alturas)
maior_altura = max(alturas)

print("Manor altura do numero de pessoas: ", menor_altura)
print("Maior altura do numero de pessoas: ", maior_altura)
