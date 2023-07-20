# Criação de arquivos e Pastas usando script Python

**Criação de arquivos e pastas usando script Python**

A criação de arquivos e pastas usando script Python é um processo que permite criar um arquivo ou pasta usando um programa de computador escrito em Python. Isso pode ser feito usando uma variedade de funções da biblioteca padrão do Python, como `open()`, `os.mkdir()` e `os.path.join()`.

A função `open()` é usada para abrir um arquivo para leitura, escrita ou adição. O parâmetro `mode` especifica o modo de abertura do arquivo. Os modos possíveis são `"r"` para leitura, `"w"` para escrita e `"a"` para adição.

A função `os.mkdir()` é usada para criar uma nova pasta. O parâmetro `name` especifica o nome da pasta a ser criada.

A função `os.path.join()` é usada para concatenar dois ou mais caminhos. O retorno é um novo caminho que é a concatenação dos caminhos especificados.

Aqui está um exemplo de código que cria um arquivo chamado `meu_arquivo.txt` e escreve o texto "Olá, mundo!" no arquivo:

```
import os

file = open("meu_arquivo.txt", "w")
file.write("Olá, mundo!")
file.close()
```

Aqui está um exemplo de código que cria uma pasta chamada `minha_pasta`:

```
import os

os.mkdir("minha_pasta")
```

Aqui está um exemplo de código que usa a função `os.path.join()` para concatenar dois caminhos:

```
import os

path1 = "/home/user1/"
path2 = "/home/user2/"

new_path = os.path.join(path1, path2)

print(new_path)
```

A saída do código acima é:

```
/home/user1/user2/
```


# Estrutura de Dados - Árvores Binárias

**Estrutura de Dados - Árvores Binárias**

Uma árvore binária é uma estrutura de dados que consiste em nós e nós filhos. Cada nó tem dois nós filhos, um à esquerda e um à direita. O nó no topo da árvore é chamado de nó raiz.

As árvores binárias são usadas para armazenar e acessar dados de forma rápida. Elas são particularmente úteis para armazenar dados que estão organizados em uma estrutura hierárquica, como uma lista de pessoas, onde cada pessoa tem pais, filhos e irmãos.

As árvores binárias são uma estrutura de dados complexa, mas também são muito eficientes. Elas podem ser usadas para realizar uma variedade de tarefas, como:

* Buscar dados
* Inserir dados
* Remover dados
* Ordenar dados

Aqui está um exemplo de árvore binária:

```
    A
   / \
  B   C
 / \ / \
D   E   F
```

Neste exemplo, o nó `A` é o nó raiz. O nó `B` é o filho esquerdo do nó `A`. O nó `C` é o filho direito do nó `A`. O nó `D` é o filho esquerdo do nó `B`. O nó `E` é o filho direito do nó `B`. O nó `F` é o filho esquerdo do nó `C`.






# Threads

**Threads**

Um thread é uma linha de execução de um programa de computador. Cada thread pode executar uma tarefa diferente ao mesmo tempo.

Os threads são úteis para melhorar o desempenho de um programa de computador. Eles permitem que o programa execute várias tarefas ao mesmo tempo, o que pode acelerar o tempo de execução do programa.

Os threads também são úteis para tornar um programa de computador mais responsivo. Se um programa de computador tiver apenas uma linha de execução, ele só poderá executar uma tarefa de cada vez. Isso pode fazer com que o programa pareça lento ou bloqueado se uma tarefa for demorada.

Os threads podem ser usados para executar várias tarefas ao mesmo tempo, o que pode tornar o programa de computador mais responsivo.

Aqui está um exemplo de código que usa threads para executar duas tarefas ao mesmo tempo:

```
import threading

def task1():
    print("Executando tarefa 1")

def task2():
    print("Executando tarefa 2")

if __name__ == "__main__":
    # Cria duas threads
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)

    # Inicia as duas threads
    t1.start()
    t2.start()
```

# Adminstração de Sistemas Operacionais - Profº Luiz

# Lista de Exercícios - Criação de arquivos


1. Crie um código em Python que crie 10 arquivos vazios na pasta C:/Users/alunocssb/Desktop

for a in range(10):
	arq = open('C:\\Users\\alunocssb\\Desktop\\Arquivo' + str(a) + '.txt','w')



2. Crie um código em Python que crie 10 pastas na pasta C:/Users/alunocssb/Desktop

import os

for p in range(10):
	os.system ('mkdir C:\\Users\\Alunocssb\\Desktop\\pasta +str(p))



3. Crie um código em Python que crie 15 pastas com 35 arquivos vazios dentro delas

for p in range(15):
	os.system('mkdir p+str(p))
	for a in range(35):
		arq = open('pasta+str(p)+'/arquivo+str(a)+'.txt','w')


  
4. Crie um código em Python que crie 15 arquivos com 500 Bytes cada

for a in range(15):
	with open('Arquivo',+str(a+1)+'.txt','w') as arq:
		for b in range(500):
			arq.write('V')



5. Crie um código em Python que imprima na tela o conteúdo dos 15 arquivos criados no exercício anterior

for a in range(15):
	with open('Arquivo',+str(a+1)+'.txt','r') as arq:
		print(arq.read())



6. Crie um código em Python que exclua as 15 pastas do exercício 3. Pode utilizar o comando 'rm'.

import os
for p in range(15):
	os.system('rmdir pasta+str(p))



 
