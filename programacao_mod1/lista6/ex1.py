# 1. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

#função
def soma(a, b, c):
    return a + b + c

#programa principal
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))
total = soma(n1, n2, n3)
print("A soma dos três números é:", total)