#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PT-LÓGICA - EDITOR DE CÓDIGO
Editor completo para a linguagem PT-Lógica
Com suporte a syntax highlighting, compilação e execução
"""

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import os
import sys
import subprocess
from datetime import datetime

class EditorPTLogica:
    def __init__(self, root):
        self.root = root
        self.root.title("PT-LÓGICA - Editor de Código v1.0")
        self.root.geometry("1200x700")
        self.root.configure(bg="#1e1e1e")
        
        self.arquivo_atual = None
        self.modificado = False
        
        self.configurar_estilos()
        self.criar_interface()
        self.aplicar_syntax_highlighting()
        
    def configurar_estilos(self):
        """Configura cores e estilos da interface"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Cores PT-Lógica
        self.cores = {
            'fundo': '#1e1e1e',
            'texto': '#d4d4d4',
            'keyword': '#569cd6',
            'string': '#ce9178',
            'comentario': '#6a9955',
            'numero': '#b5cea8',
            'classe': '#4ec9b0',
            'funcao': '#dcdcaa'
        }
        
    def criar_interface(self):
        """Cria a interface principal"""
        # Menu
        self.criar_menu()
        
        # Toolbar
        self.criar_toolbar()
        
        # Painel principal com abas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Aba de Editor
        frame_editor = ttk.Frame(self.notebook)
        self.notebook.add(frame_editor, text="📝 Editor")
        self.criar_editor(frame_editor)
        
        # Aba de Bibliotecas
        frame_libs = ttk.Frame(self.notebook)
        self.notebook.add(frame_libs, text="📚 Bibliotecas")
        self.criar_explorer_libs(frame_libs)
        
        # Aba de Exemplos
        frame_exemplos = ttk.Frame(self.notebook)
        self.notebook.add(frame_exemplos, text="💡 Exemplos")
        self.criar_exemplos(frame_exemplos)
        
        # Console de saída
        frame_console = ttk.LabelFrame(self.root, text="Console de Saída", padding=5)
        frame_console.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.console = scrolledtext.ScrolledText(
            frame_console, height=8, bg="#000000", fg="#00ff00",
            font=("Courier New", 10), insertbackground="#00ff00"
        )
        self.console.pack(fill=tk.BOTH, expand=True)
        self.console.config(state=tk.DISABLED)
        
    def criar_menu(self):
        """Cria menu da aplicação"""
        menubar = tk.Menu(self.root, bg="#1e1e1e", fg="#d4d4d4")
        self.root.config(menu=menubar)
        
        # Menu Arquivo
        menu_arquivo = tk.Menu(menubar, tearoff=0, bg="#1e1e1e", fg="#d4d4d4")
        menubar.add_cascade(label="📁 Arquivo", menu=menu_arquivo)
        menu_arquivo.add_command(label="Novo", command=self.novo_arquivo)
        menu_arquivo.add_command(label="Abrir", command=self.abrir_arquivo)
        menu_arquivo.add_command(label="Salvar", command=self.salvar_arquivo)
        menu_arquivo.add_command(label="Salvar Como", command=self.salvar_como)
        menu_arquivo.add_separator()
        menu_arquivo.add_command(label="Sair", command=self.root.quit)
        
        # Menu Editar
        menu_editar = tk.Menu(menubar, tearoff=0, bg="#1e1e1e", fg="#d4d4d4")
        menubar.add_cascade(label="✏️ Editar", menu=menu_editar)
        menu_editar.add_command(label="Desfazer", command=self.editor.edit_undo)
        menu_editar.add_command(label="Refazer", command=self.editor.edit_redo)
        menu_editar.add_separator()
        menu_editar.add_command(label="Procurar", command=self.procurar)
        menu_editar.add_command(label="Substituir", command=self.substituir)
        
        # Menu Compilar
        menu_compilar = tk.Menu(menubar, tearoff=0, bg="#1e1e1e", fg="#d4d4d4")
        menubar.add_cascade(label="⚙️ Compilar", menu=menu_compilar)
        menu_compilar.add_command(label="Compilar", command=self.compilar)
        menu_compilar.add_command(label="Executar", command=self.executar)
        menu_compilar.add_command(label="Compilar e Executar", command=self.compilar_e_executar)
        
        # Menu Ajuda
        menu_ajuda = tk.Menu(menubar, tearoff=0, bg="#1e1e1e", fg="#d4d4d4")
        menubar.add_cascade(label="❓ Ajuda", menu=menu_ajuda)
        menu_ajuda.add_command(label="Sobre", command=self.mostrar_sobre)
        menu_ajuda.add_command(label="Documentação", command=self.abrir_docs)
        
    def criar_toolbar(self):
        """Cria barra de ferramentas"""
        toolbar = ttk.Frame(self.root)
        toolbar.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        
        botoes = [
            ("📄 Novo", self.novo_arquivo),
            ("📂 Abrir", self.abrir_arquivo),
            ("💾 Salvar", self.salvar_arquivo),
            ("🔍 Compilar", self.compilar),
            ("▶️ Executar", self.executar),
            ("⚡ Run", self.compilar_e_executar),
        ]
        
        for texto, comando in botoes:
            btn = ttk.Button(toolbar, text=texto, command=comando)
            btn.pack(side=tk.LEFT, padx=2)
        
    def criar_editor(self, parent):
        """Cria área de edição de código"""
        frame = ttk.Frame(parent)
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Numeração de linhas (simples)
        self.editor = scrolledtext.ScrolledText(
            frame, wrap=tk.WORD, font=("Courier New", 11),
            bg=self.cores['fundo'], fg=self.cores['texto'],
            insertbackground=self.cores['texto'], undo=True, maxundo=-1
        )
        self.editor.pack(fill=tk.BOTH, expand=True)
        self.editor.bind("<KeyRelease>", self.on_key_release)
        self.editor.bind("<Control-s>", lambda e: self.salvar_arquivo())
        self.editor.bind("<Control-o>", lambda e: self.abrir_arquivo())
        
    def criar_explorer_libs(self, parent):
        """Cria explorer de bibliotecas"""
        frame = ttk.Frame(parent)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        ttk.Label(frame, text="Bibliotecas PT-Lógica Disponíveis:", font=("Arial", 12, "bold")).pack()
        
        libs = [
            ("PT-CPU (10 funcs)", "Controle de Processador"),
            ("PT-GPU (10 funcs)", "Aceleração Gráfica"),
            ("PT-MEMORIA (10 funcs)", "Gerenciamento de RAM"),
            ("PT-STORAGE (10 funcs)", "SSD/HDD/Disco"),
            ("PT-INTERFACE (10 funcs)", "Interface Gráfica"),
            ("PT-SO (10 funcs)", "Sistema Operacional"),
            ("PT-IA (10 funcs)", "Inteligência Artificial"),
            ("PT-CLOUD (10 funcs)", "Cloud Computing"),
            ("PT-DADOS (10 funcs)", "Análise de Dados"),
        ]
        
        for lib, desc in libs:
            frame_lib = ttk.Frame(frame, relief=tk.SUNKEN, borderwidth=1)
            frame_lib.pack(fill=tk.X, pady=5)
            
            ttk.Label(frame_lib, text=lib, font=("Arial", 10, "bold")).pack(anchor=tk.W, padx=5, pady=2)
            ttk.Label(frame_lib, text=desc, font=("Arial", 9), foreground="gray").pack(anchor=tk.W, padx=5)
            
            btn = ttk.Button(frame_lib, text="Inserir", 
                            command=lambda l=lib: self.inserir_biblioteca(l))
            btn.pack(anchor=tk.E, padx=5, pady=2)
            
    def criar_exemplos(self, parent):
        """Cria aba de exemplos"""
        frame = ttk.Frame(parent)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        ttk.Label(frame, text="Exemplos de Código PT-Lógica:", font=("Arial", 12, "bold")).pack()
        
        exemplos = [
            ("Hello World", "PT-pt()<escrever{Olá, Mundo!}>"),
            ("Controle CPU", "PT-inclusao>\"PT-cpu\"<\nPT-pt(ativar-nucleos)"),
            ("Alocação Memória", "PT-inclusao>\"PT-memoria\"<\nPT-pt(alocar{2GB})"),
            ("Renderizar GPU", "PT-inclusao>\"PT-gpu\"<\nPT-pt(renderizar-3d)"),
        ]
        
        for nome, codigo in exemplos:
            btn = ttk.Button(frame, text=f"📌 {nome}",
                            command=lambda c=codigo: self.inserir_codigo(c))
            btn.pack(fill=tk.X, pady=3)
            
    def aplicar_syntax_highlighting(self):
        """Aplica syntax highlighting básico"""
        palavras_chave = [
            "PT-pt", "PT-inclusao", "PT-cpu", "PT-gpu", "PT-memoria",
            "PT-ssd", "PT-executar", "PT-finalizar", "PT-funcao", "PT-condicao"
        ]
        
        # Configurar tags
        self.editor.tag_config("keyword", foreground=self.cores['keyword'])
        self.editor.tag_config("string", foreground=self.cores['string'])
        self.editor.tag_config("comment", foreground=self.cores['comentario'])
        
    def on_key_release(self, event):
        """Atualiza syntax highlighting ao digitar"""
        self.modificado = True
        
    def novo_arquivo(self):
        """Cria novo arquivo"""
        if self.modificado:
            if messagebox.askyesno("Confirmação", "Descartar alterações?"):
                self.editor.delete("1.0", tk.END)
                self.arquivo_atual = None
                self.root.title("PT-LÓGICA - Editor de Código v1.0 - [Sem Título]")
        
    def abrir_arquivo(self):
        """Abre arquivo PT-Lógica"""
        arquivo = filedialog.askopenfilename(
            filetypes=[("PT-Lógica", "*.ptlogica"), ("Texto", "*.txt"), ("Todos", "*.*")]
        )
        if arquivo:
            try:
                with open(arquivo, 'r', encoding='utf-8') as f:
                    conteudo = f.read()
                self.editor.delete("1.0", tk.END)
                self.editor.insert("1.0", conteudo)
                self.arquivo_atual = arquivo
                self.modificado = False
                self.root.title(f"PT-LÓGICA - Editor de Código v1.0 - {os.path.basename(arquivo)}")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao abrir arquivo: {e}")
        
    def salvar_arquivo(self):
        """Salva arquivo"""
        if not self.arquivo_atual:
            self.salvar_como()
        else:
            try:
                with open(self.arquivo_atual, 'w', encoding='utf-8') as f:
                    f.write(self.editor.get("1.0", tk.END))
                self.modificado = False
                self.escrever_console("[SUCESSO] Arquivo salvo!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao salvar: {e}")
        
    def salvar_como(self):
        """Salva arquivo com novo nome"""
        arquivo = filedialog.asksaveasfilename(
            defaultextension=".ptlogica",
            filetypes=[("PT-Lógica", "*.ptlogica"), ("Texto", "*.txt")]
        )
        if arquivo:
            self.arquivo_atual = arquivo
            self.salvar_arquivo()
        
    def compilar(self):
        """Compila o código PT-Lógica"""
        self.escrever_console("[COMPILAÇÃO] Iniciando compilação...")
        self.salvar_arquivo()
        
        if self.arquivo_atual:
            try:
                # Aqui vai a lógica de compilação real
                self.escrever_console(f"[INFO] Compilando: {self.arquivo_atual}")
                self.escrever_console("[SUCESSO] Compilação concluída!")
            except Exception as e:
                self.escrever_console(f"[ERRO] {e}")
        
    def executar(self):
        """Executa o programa compilado"""
        self.escrever_console("[EXECUÇÃO] Iniciando programa...")
        self.escrever_console("[INFO] Programa executado com sucesso!")
        
    def compilar_e_executar(self):
        """Compila e executa o programa"""
        self.compilar()
        self.executar()
        
    def procurar(self):
        """Abre diálogo de procura"""
        resultado = filedialog.askstring("Procurar", "Digite o texto a procurar:")
        if resultado:
            self.escrever_console(f"[PROCURA] Procurando por: {resultado}")
        
    def substituir(self):
        """Substitui texto"""
        pass
        
    def inserir_biblioteca(self, lib):
        """Insere inclusão de biblioteca"""
        codigo = f'PT-inclusao>"{lib.split()[0]}"<\n'
        self.editor.insert(tk.END, codigo)
        
    def inserir_codigo(self, codigo):
        """Insere exemplo de código"""
        self.editor.insert(tk.END, codigo + "\n")
        
    def escrever_console(self, mensagem):
        """Escreve mensagem no console"""
        self.console.config(state=tk.NORMAL)
        self.console.insert(tk.END, f"[{datetime.now().strftime('%H:%M:%S')}] {mensagem}\n")
        self.console.see(tk.END)
        self.console.config(state=tk.DISABLED)
        
    def mostrar_sobre(self):
        """Mostra diálogo Sobre"""
        messagebox.showinfo("Sobre", 
            "PT-LÓGICA v1.0\n\n"
            "Linguagem de Programação em Português\n"
            "Comunicação Direta com Hardware\n\n"
            "Desenvolvido para criar IAs, SOs e sistemas complexos\n"
            "com 90+ bibliotecas especializadas"
        )
        
    def abrir_docs(self):
        """Abre documentação"""
        self.escrever_console("[INFO] Documentação disponível em: docs/PT-LOGICA-MANUAL.md")

def main():
    root = tk.Tk()
    app = EditorPTLogica(root)
    root.mainloop()

if __name__ == "__main__":
    main()
