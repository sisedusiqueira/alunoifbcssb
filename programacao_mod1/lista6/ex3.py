# 3. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

#função
def reverso_numero(numero):
    reverso = int(str(numero)[::-1])
    return reverso

#programa principal
n = int(input('Digite um numero inteiro: '))
resultado_reverso = reverso_numero(n)
print("O reverso do número é:", resultado_reverso)