#função
def valorPagamento(valorPrest, diasAtraso):
  print('-'*35)
  if diasAtraso == 0:
    return valorPrest
  else:
    multa = valorPrest * 0.03
    juros = valorPrest * (0.001 * diasAtraso)
    return valorPrest + multa + juros
  print('-'*35)


#programa principal
prestacoesPagas = 0
valorTotalPag = 0

while True:
  valor = float(input("Digite o valor da prestação (ou 0 para sair): "))
  if valor == 0:
    break

  diasAtraso = int(input("Digite o número de dias em atraso: "))

  valorPagar = valorPagamento(valor, diasAtraso)

  print("Valor a ser pago: R$", valorPagar)
  prestacoesPagas += 1
  valorTotalPag += valorPagar

print("\nRelatório do dia: ")
print("Quantidade de prestações pagas:", prestacoesPagas)
print("Valor total de pretações pagas: R$", valorTotalPag)