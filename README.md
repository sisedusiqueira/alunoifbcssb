# alunoifbcssb

# Introdução a Programação com Python

# Exercícios
* <a href="">Lista 1</a>
* <a href="">Lista 2</a>
* <a href="">Lista 3</a>
* <a href="">Lista 4</a>
* <a href="">Lista 5</a>
* <a href="">Lista 6</a>
* <a href="">Lista 7</a>
* <a href="">Lista 8</a>

## Material Slides
<a href="https://drive.google.com/file/d/1yXhQkOMpoEIzLoC22RkC1kEewgTs8JIw/view?hl=pt-BR">Aula 01 - Introdução à Programação - Apostila 1<br>
<a href="https://drive.google.com/file/d/1AnKJsquc_zhZS2M4_tmo1QZeq5L_uGBb/view?hl=pt-BR">Aula 02 - Introdução à Programação - Apostila 2<br>
<a href="https://drive.google.com/file/d/1YEfQ_P9RMUOAoYHcYt2XgVG62gs6Be4e/view?hl=pt-BR">Aula 03 - Introdução à Programação - Apostila 3<br>
<a href="https://www.youtube.com/watch?v=ii4tVqL49wY">Aula 04 - Introdução à Programação - Variáveis em Python 3<br>
<a href="https://drive.google.com/file/d/1Dp1fuueKJQHKrW8MoTnX_CNzZwVMdpqr/view?hl=pt-BR">Aula 05 - Introdução à Programação - Lista 02 Exercícios - Operadores Aritméticos, Relacionais e Lógico<br>
<a href="https://drive.google.com/file/d/13_jVhzIVFJs4CQ9AE71J1EnHFXZntIOv/view?hl=pt-BR">Aula 06 - Introdução à Programação - Lista 02 Exercícios - Respostas<br>
<a href="https://www.youtube.com/watch?v=w6M7eWFWZcc">Aula 07 - Introdução à Programação - Como usar IF em Python<br>
<a href="https://www.youtube.com/watch?v=EbrIvzu32Bg">Aula 08 - Introdução à Programação - Identação<br>
<a href="https://www.youtube.com/watch?v=Pi3cHCFWb60">Aula 09 - Introdução à Programação - If e a Indentação em Python<br>
<a href="https://www.devmedia.com.br/python-estrutura-de-repeticao-while/38546?authuser=0&hl=pt-BR">Aula 10 - Introdução à Programação - Python: Estrutura de repetição while<br>
<a href="http://curso.grupysanca.com.br/pt/latest/repeticao.html?authuser=0&hl=pt-BR">Aula 11 - Introdução à Programação - Estruturas de repetição<br>
<a href="https://drive.google.com/file/d/1s9GicWTV4DrhkmdJIqDEymsePkrd-nsv/view?hl=pt-BR">Aula 12 - Introdução à Programação - Estrutura de Repetição While<br>
<a href="https://www.loom.com/share/637e520dfd5b46348796da05caf822b3?authuser=0&hl=pt-BR">Aula 13 - Introdução à Programação - Listas e FOR<br>
<a href="https://www.loom.com/share/6b0078621b4a4846a4aaed6a341e9439?authuser=0&hl=pt-BR">Aula 14 - Introdução à Programação - Listas e FOR<br>
<a href="https://www.youtube.com/watch?v=ezfr9d7wd_k"><br>
<a href="https://www.youtube.com/watch?v=etjJ_4Eqrk8"><br>

#### Python Orientação a Objetos
class Carro:
    # Definicao dos atributos
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
   
    #Definicao dos metodos
    def imprimir(lista):
        for i in lista:
            print(f"Marca: {i.marca} Modelo: {i.modelo} Ano: {i.ano} ")
   
    def criar_carros2():
        carros2 = []
        while True:
            marca = input("Digite a marca do carro (ou digite 'sair' para encerrar): ")
            if marca.lower() == 'sair':
                break
   
            modelo = input("Digite o modelo do carro: ")
            ano = int(input("Digite o ano do carro: "))
   
            carros2.append(Carro(marca, modelo, ano))
   
        return carros2
       
   
#-----------------------------------------------------------------

carro = Carro.criar_carros2()

Carro.imprimir(carro)

## Explique quando utilizar a estrutura de repetição e diferencie as estruturas FOR e WHILE dando um exemplo de uso para cada.
</p>
Estruturas de repetição são utilizadas quando um bloco de código é executado em looping repetidas vezes.

Existem duas formas de criar uma estrutura de repetição:

FOR - usado quando se quer iterar sobre um bloco de código um número determinado de vezes.

# Aqui repetimos o print 3 vezes
for n in range(0, 3):
    print(n)

0
1
2

WHILE - usado quando queremos que o bloco de código seja repetido até que uma condição seja satisfeita. Ou seja, é necessário que uma expressão booliana dada seja verdadeira. Assim que ela se tornar falsa, o while para.

# Aqui iniciamos o n em 0, e repetimos o print até que seu valor seja maior ou igual a 3
n = 0
while n < 3:
    print(n)
    n += 1

0
1
2
</p>

## O que é a indentação no Python? Quando utilizar?
<p>
Indentação é uma forma de arrumar o código, fazendo com que algumas linhas fiquei mais à direita que as outras, à medida que adicionamos espaços em seu início. Para a maioria das linguagens a indentação não é obrigatória, mas no caso Python isso é diferente.

A indentação é uma característica importante no Python, pois além de promover a legibilidade é essencial para o bom funcionamento do código. Em outras palavras, se a indentação não estiver adequada o programa pode se comportar de forma inesperada ou até mesmo não compilar.

Por exemplo, no caso de um if, o que determina se um código está dentro da condicional é o fato dele ter sido indentado. O Código apresenta um exemplo onde o comando print só será executado se o valor da variável x for maior que 8.

x = 10

if x > 8:
   print("x é maior que 8")

Agora veja esse novo exemplo no qual o comando print será executado de qualquer forma por não estar indentado e, por isso, não estar contido no if.

x = 10

if x > 8:

print("x é maior que 8")

No Código temos dois erros. O primeiro tem a ver com a forma como o código foi escrito, porque se se espera que o comando print seja executado apenas se x for maior que 8, ele deveria estar indentado.

Um outro erro está relacionado a estrutura de controle de fluxo if, que será vista em detalhes em um outro momento. Uma vez que o comando print não está indentado, o mesmo também não está contido no if, deixando-o vazio e isso vai causar um erro de sintaxe.</p>

## Quantas e quais são as variáveis definidas no exemplo do vídeo.
velocidade_maxima = 240 #Numero
frase_de_boas_vindas = 'Olá, seja bem-vindo a Dev Aprender!'
posso_entrar_na_sua_casa = False #Boleanos
dollar = 5.25 #Decimal

## Comandos do GitHub
<a href="https://github.com/sisedusiqueira/alunoifbcssb/blob/main/github-git-cheat-sheet.pdf">Comandos GitHub</a>
