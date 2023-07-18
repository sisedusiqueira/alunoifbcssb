'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
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

salario = float(input("Digite o seu salário: "))

salario_baixo = salario * 0.20
baixo = salario * 1.20

salario_medio = salario * 0.15
medio = salario * 1.15

salario_alto = salario * 0.10
alto = salario * 1.10

salario_altissimo = salario * 0.05
altissimo = salario * 1.05

print("\nAntes Reajuste: ", salario)

if salario <= 280: print("Aumento: 20%\nValor: ", salario_baixo, "\nFinal: ", baixo)
elif salario > 200 and salario <= 700: print("Aumento: 15%\nValor: ", salario_medio, "\nFinal: ", medio)
elif salario > 700 and salario <= 1500: print("Aumento: 10%\nValor: ", salario_alto, "\nFinal: ", alto)
else: print("Aumento: 5%\nValor: ", salario_altissimo, "\nFinal: ", altissimo)