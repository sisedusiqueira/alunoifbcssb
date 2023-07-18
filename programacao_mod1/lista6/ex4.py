# 4. Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

#função
def quantidade_digitos(numero):
    return len(str(numero))

#programa principal
n = int(input("Digite um numero: "))
resultado_digitos = quantidade_digitos(n)
print("O número possui", resultado_digitos, "dígitos.")