import csv

def criar_usuario(usuario):
    with open('usuarios.csv', 'a', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(usuario)

def listar_usuarios():
    with open('usuarios.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(linha)

def buscar_usuario(email):
    with open('usuarios.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            if linha[2] == email:
                return linha
        return None

def atualizar_usuario(email, novos_dados):
    usuarios = []
    with open('usuarios.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            if linha[2] == email:
                usuarios.append(novos_dados)
            else:
                usuarios.append(linha)
    
    with open('usuarios.csv', 'w', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(usuarios)

def deletar_usuario(email):
    usuarios = []
    with open('usuarios.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            if linha[2] != email:
                usuarios.append(linha)
    
    with open('usuarios.csv', 'w', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(usuarios)

# Exemplo de uso
usuario1 = ['João', 'Silva', 'joao@example.com']
usuario2 = ['Maria', 'Santos', 'maria@example.com']

# Criar usuários
criar_usuario(usuario1)
criar_usuario(usuario2)

# Listar todos os usuários
listar_usuarios()

# Buscar um usuário pelo e-mail
usuario_encontrado = buscar_usuario('joao@example.com')
if usuario_encontrado:
    print('Usuário encontrado:', usuario_encontrado)
else:
    print('Usuário não encontrado.')

# Atualizar um usuário
novo_nome = 'João Pedro'
atualizar_usuario('joao@example.com', [novo_nome, usuario1[1], usuario1[2]])

# Deletar um usuário
deletar_usuario('maria@example.com')

# Listar usuários após as modificações
listar_usuarios()
