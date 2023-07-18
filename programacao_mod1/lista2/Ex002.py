'''
2. Escreva um programa que receba o salário de um funcionário
 (float), e retorne o resultado do
 novo salário com reajuste de 35%.
'''
salario = float (input('Qual o salario do funcionario?  '))
print ('O salario do funcionario é:  ',salario)
print ('O aumento de 35% é no valor de:  ',(35/100 * salario))
print ('Salario total é: ', (35/100 * salario) + salario )