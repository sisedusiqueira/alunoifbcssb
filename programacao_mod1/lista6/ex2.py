# 2. Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

#função
def verificar_sinal(n):
    if n >= 0:
        return 'Positivo'
    else:
        return 'Negativo'

#programa principal
n = int(input('Digite um numero: '))
total = verificar_sinal(n)
print("O sinal do argumento é:", total)