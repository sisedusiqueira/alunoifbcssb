print("Bem-vindo ao meu quiz de computador!")

jogar = input("Você quer jogar? ")

if jogar.lower() != "sim":
    quit()

print("Ok! Vamos jogar :)")
pontuacao = 0

resposta = input("O que significa CPU? ")
if resposta.lower() == "unidade central de processamento":
    print('Correto!')
    pontuacao += 1
else:
    print("Incorreto!")

resposta = input("O que significa GPU? ")
if resposta.lower() == "unidade de processamento gráfico":
    print('Correto!')
    pontuacao += 1
else:
    print("Incorreto!")

resposta = input("O que significa RAM? ")
if resposta.lower() == "memória de acesso aleatório"
    print('Correto!')
    pontuacao += 1
else:
    print("Incorreto!")

resposta = input("O que significa PSU? ")
if resposta.lower() == "fonte de alimentação":
    print('Correto!')
    pontuacao += 1
else:
    print("Incorreto!")

print("Você acertou " + str(pontuacao) + " perguntas!")
print("Você obteve " + str((pontuacao / 4) * 100) + "% de acerto.")