import tkinter as tk

def executar_codigo():
    codigo = texto.get("1.0", tk.END)
    try:
        exec(codigo)
        resultado.configure(text="")
    except Exception as e:
        resultado.configure(text=str(e))

janela = tk.Tk()

# Área de texto para o código
texto = tk.Text(janela)
texto.pack()

# Botão para executar o código
botao_executar = tk.Button(janela, text="Executar", command=executar_codigo)
botao_executar.pack()

# Resultado da execução
resultado = tk.Label(janela, text="")
resultado.pack()

janela.mainloop()
