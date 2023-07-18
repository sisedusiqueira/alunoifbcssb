import math

def calcular_atenuacao(comprimento, atenuacao_por_metro):
    atenuacao_total = comprimento * atenuacao_por_metro
    return atenuacao_total

def calcular_potencia_saida(potencia_entrada, ganho, eficiencia):
    potencia_saida = potencia_entrada * ganho * eficiencia
    return potencia_saida

def calcular_snr(potencia_sinal, potencia_ruido):
    snr = 10 * math.log10(potencia_sinal / potencia_ruido)
    return snr

# Função principal da calculadora
def calculadora_telecomunicacoes():
    print("Bem-vindo à Calculadora de Engenharia de Telecomunicações!")
    print("Selecione a operação:")
    print("1. Cálculo de Atenuação")
    print("2. Cálculo de Potência de Saída")
    print("3. Cálculo de SNR")
    escolha = int(input("Digite o número da operação desejada: "))

    if escolha == 1:
        comprimento = float(input("Digite o comprimento do meio de transmissão (em metros): "))
        atenuacao_por_metro = float(input("Digite a atenuação por metro (em dB/m): "))
        resultado = calcular_atenuacao(comprimento, atenuacao_por_metro)
        print("Resultado da atenuação:", resultado, "dB")
    elif escolha == 2:
        potencia_entrada = float(input("Digite a potência de entrada: "))
        ganho = float(input("Digite o ganho: "))
        eficiencia = float(input("Digite a eficiência: "))
        resultado = calcular_potencia_saida(potencia_entrada, ganho, eficiencia)
        print("Potência de saída:", resultado, "W")
    elif escolha == 3:
        potencia_sinal = float(input("Digite a potência do sinal: "))
        potencia_ruido = float(input("Digite a potência do ruído: "))
        resultado = calcular_snr(potencia_sinal, potencia_ruido)
        print("Relação Sinal-Ruído (SNR):", resultado, "dB")
    else:
        print("Escolha inválida. Por favor, tente novamente.")

calculadora_telecomunicacoes()
