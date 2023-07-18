import subprocess

def exibir_codigo(codigo):
    print("Código digitado:")
    print(codigo)

# Chamar o processo do editor
editor_process = subprocess.Popen(["python", "editor.py"])
editor_process.wait()

# Ler o conteúdo do arquivo de saída gerado pelo editor
with open("output.txt", "r") as file:
    codigo = file.read()

# Exibir o código digitado na tela
exibir_codigo(codigo)

# Faça algo com o código lido
 