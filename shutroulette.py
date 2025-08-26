import tkinter as tk
import random
import time
import platform
import os
from threading import Thread

def shutdown_real():
    sistema = platform.system()
    try:
        if sistema == "Windows":
            os.system("shutdown /s /t 0")
        elif sistema == "Linux":
            os.system("shutdown -h now")
        else:
            print("Sistema não suportado para shutdown real.")
    except Exception as e:
        print(f"Erro: {e}")

def roleta_russa_real():
    sorteio = random.choice([True, False])
    if sorteio:
        for i in range(10, 0, -1):
            label_var.set(f"Você foi sorteado! Desligando em {i} segundos...")
            time.sleep(1)
        shutdown_real()
    else:
        label_var.set("Você não foi sorteado! Nenhum PC será desligado.")

def iniciar():
    Thread(target=roleta_russa_real).start()

root = tk.Tk()
root.title("Roleta Russa Educativa")
root.geometry("400x150")

label_var = tk.StringVar()
label_var.set("Abrindo roleta russa...")

label = tk.Label(root, textvariable=label_var, font=("Arial", 12))
label.pack(pady=20)

root.after(100, iniciar)
root.mainloop()
