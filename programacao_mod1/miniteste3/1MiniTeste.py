pe_direito_chip_identificacao = 4.0
pe_esquero_tipo_alimento = 3.5

print('='*50)

qtd_frango = (float(input('Digite o número de frangos: ')))

total = (pe_direito_chip_identificacao + ( 2 * pe_esquero_tipo_alimento))
resultado = total * qtd_frango

print('Quantidade total de gastos é: ', resultado)