def calcular_atenuacao(comprimento, atenuacao_por_metro):
    atenuacao_total = comprimento * atenuacao_por_metro
    return atenuacao_total

comprimento = float(input("Digite o comprimento do meio de transmissão (em metros): "))
atenuacao_por_metro = float(input("Digite a atenuação por metro (em dB/m): "))

resultado = calcular_atenuacao(comprimento, atenuacao_por_metro)

print("Tipo de cálculo: Cálculo de atenuação")
print("Comprimento do meio de transmissão:", comprimento, "metros")
print("Atenuação por metro:", atenuacao_por_metro, "dB/m")
print("Resultado da atenuação:", resultado, "dB")
