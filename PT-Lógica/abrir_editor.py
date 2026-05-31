#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Abre editor PT-Lógica em tela cheia"""

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import os
import sys

# Importar editor
sys.path.insert(0, 'editor')
from editor_pt_logica import EditorPTLogica

if __name__ == "__main__":
    root = tk.Tk()
    
    # Maximizar janela
    root.state('zoomed')  # Windows
    
    app = EditorPTLogica(root)
    
    # Trazer para frente
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)
    
    root.mainloop()
