#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Editor PT-Lógica SIMPLES - Janela Real e Funcional"""

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os
import subprocess

class EditorSimples:
    def __init__(self, root):
        self.root = root
        self.root.title("PT-LÓGICA - EDITOR DE CÓDIGO")
        self.root.geometry("1000x600")
        self.arquivo = None
        
        # Barra de Menu
        menu = tk.Menu(root)
        root.config(menu=menu)
        
        arquivo_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Arquivo", menu=arquivo_menu)
        arquivo_menu.add_command(label="Novo", command=self.novo)
        arquivo_menu.add_command(label="Abrir", command=self.abrir)
        arquivo_menu.add_command(label="Salvar", command=self.salvar)
        arquivo_menu.add_separator()
        arquivo_menu.add_command(label="Sair", command=root.quit)
        
        editar_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Editar", menu=editar_menu)
        editar_menu.add_command(label="Limpar", command=lambda: self.texto.delete("1.0", "end"))
        
        compilar_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Executar", menu=compilar_menu)
        compilar_menu.add_command(label="Compilar e Executar", command=self.compilar)
        compilar_menu.add_command(label="Ver Exemplos", command=self.exemplos)
        
        # Área de Texto
        self.texto = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier", 11), bg="#1e1e1e", fg="#d4d4d4")
        self.texto.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Status bar
        self.status = tk.Label(root, text="Pronto | PT-Lógica v1.0", bg="#333", fg="#0f0", anchor="w")
        self.status.pack(fill=tk.X, side=tk.BOTTOM)
        
    def novo(self):
        self.texto.delete("1.0", "end")
        self.arquivo = None
        self.root.title("PT-LÓGICA - NOVO ARQUIVO")
        
    def abrir(self):
        arquivo = filedialog.askopenfilename(
            filetypes=[("PT-Lógica", "*.ptlogica"), ("Todos", "*.*")],
            initialdir="exemplos"
        )
        if arquivo:
            try:
                with open(arquivo, 'r', encoding='utf-8') as f:
                    conteudo = f.read()
                self.texto.delete("1.0", "end")
                self.texto.insert("1.0", conteudo)
                self.arquivo = arquivo
                self.root.title(f"PT-LÓGICA - {os.path.basename(arquivo)}")
                self.status.config(text=f"✓ Aberto: {arquivo}")
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível abrir: {e}")
    
    def salvar(self):
        if not self.arquivo:
            self.arquivo = filedialog.asksaveasfilename(
                defaultextension=".ptlogica",
                filetypes=[("PT-Lógica", "*.ptlogica")],
                initialdir="exemplos"
            )
        
        if self.arquivo:
            try:
                with open(self.arquivo, 'w', encoding='utf-8') as f:
                    f.write(self.texto.get("1.0", "end"))
                self.status.config(text=f"✓ Salvo: {self.arquivo}")
                messagebox.showinfo("Sucesso", "Arquivo salvo com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao salvar: {e}")
    
    def compilar(self):
        if not self.arquivo:
            messagebox.showwarning("Aviso", "Salve o arquivo primeiro!")
            return
        
        self.salvar()
        try:
            cmd = f'cmd /c "compilar.bat {self.arquivo}"'
            subprocess.run(cmd, shell=True)
            self.status.config(text="✓ Compilado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao compilar: {e}")
    
    def exemplos(self):
        exemplos_dir = "exemplos"
        if os.path.exists(exemplos_dir):
            os.startfile(exemplos_dir)
            self.status.config(text=f"Abrindo pasta de exemplos...")
        else:
            messagebox.showerror("Erro", "Pasta 'exemplos' não encontrada")

if __name__ == "__main__":
    root = tk.Tk()
    root.state('zoomed')  # Tela cheia
    app = EditorSimples(root)
    root.mainloop()
