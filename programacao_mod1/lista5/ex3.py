'''
3. Faça um programa que leia 5 números e informe o maior número.
'''

numeros = []
for i in range(4):
  numero = float(input("Digite outro número: "))
  numeros.append(numero)

maior_numero = max(numeros)
print("Dos números digitados o maior é: ", maior_numero)