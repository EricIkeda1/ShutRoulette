import tkinter as tk
import shutil
import os

def download_exe():
    # Caminho do executável gerado
    arquivo_exe = "dist\\shutroulette.exe"
    
    if os.path.exists(arquivo_exe):
        # Defina o local para salvar o arquivo
        destino = os.path.expanduser('~') + "\\Downloads\\shutroulette.exe"  # Baixar para a pasta Downloads
        
        # Copia o executável para a pasta de downloads
        shutil.copy(arquivo_exe, destino)
        label_var.set(f"Executável baixado com sucesso! Salvo em: {destino}")
    else:
        label_var.set("Arquivo não encontrado. Certifique-se de que o .exe foi gerado.")

# Criando a interface gráfica
root = tk.Tk()
root.title("Baixar Executável")
root.geometry("400x150")

label_var = tk.StringVar()
label_var.set("Clique para baixar o executável")

label = tk.Label(root, textvariable=label_var, font=("Arial", 12))
label.pack(pady=20)

botao = tk.Button(root, text="Baixar .exe", command=download_exe)
botao.pack()

root.mainloop()
