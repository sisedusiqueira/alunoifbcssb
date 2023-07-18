'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o
programa que calculará os reajustes.
a) Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

b) salários até R$ 280,00 (incluindo) : aumento de 20%

c) salários entre R 280,00eR  700,00 : aumento de 15%

d) salários entre R 700,00eR  1500,00 : aumento de 10%

e) salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:

f) o salário antes do reajuste;

g) o percentual de aumento aplicado;

h) o valor do aumento;

i) o novo salário, após o aumento.
'''
salario = float(input("Salário: "))
if salario <= 280:
    porcentagem = 20
elif salario > 280 and salario <= 700:
    porcentagem = 15
elif salario > 700 and salario <= 1500:
    porcentagem = 10
else:
    porcentagem = 5

    valor_aumento = salario * (porcentagem / 100)
    novo_salario = salario + valor_aumento

    print("O antigo salario: ", salario)
    print("Porcentagem: ", porcentagem)
    print("O aumento: ", valor_aumento)
    print("O novo salário: ", novo_salario)