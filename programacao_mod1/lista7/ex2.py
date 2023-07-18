#função2
def Tabuada(n):
  print("Tabuada de", n, ":")
  for i in range(1,11):
    r = n * i
    print(n, "x", i, "=", r)


#programa principal
n = int(input("Digite um número entre 1 e 10 para gerar a tabuada: "))
if n < 1 or n > 10:
  print("Número inválido. Por favor, digite um número entre 1 e 10: ")
else:
  Tabuada(n)