'''
1. Faça um programa que leia e valide as seguintes informações:
-Nome: maior que 3 caracteres;
-Idade: entre 0 e 150;
-Salário: maior que zero;
-Sexo: 'f' ou 'm';
-Estado Civil: 's', 'c', 'v', 'd';
'''

nome = str(input("Digite um nome maior que 3 caracteres: "))

while len(nome) <= 3:
  nome = input("Informe mais de 3 caracteres! ")


idade = int(input("Digite sua idade: "))

while(idade < 0) or (idade > 150):
  idade = int(input("Informe entre 0 e 150 anos! "))


salario = float(input("Digite seu salário: "))

while(salario < 0):
  salario = float(input("Informe o seu salário! "))


sexo = input("Digite a letra do seu sexo: ")

while(sexo == 'f') and (sexo == 'F') and (sexo == 'm') and (sexo == 'M'):
  sexo = input("Informe novamente!")

civil = input("Qual seu estado civil? ")

while(civil != 's') and (civil != 'c') and (civil != 'v') and (civil != 'd'):
  civil = input("Informe novamente!")