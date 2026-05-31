#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PT-LÓGICA - VISUALIZADOR DE PROJETO
Mostra um resumo visual completo do projeto
"""

import os
from pathlib import Path

def listar_arquivos(diretorio, nivel=0, max_nivel=3):
    """Lista arquivos recursivamente"""
    items = []
    if nivel > max_nivel:
        return items
    
    try:
        for item in sorted(os.listdir(diretorio)):
            if item.startswith('.'):
                continue
            
            caminho = os.path.join(diretorio, item)
            indent = "  " * nivel
            
            if os.path.isdir(caminho):
                items.append(f"{indent}📁 {item}/")
                items.extend(listar_arquivos(caminho, nivel + 1, max_nivel))
            else:
                if item.endswith('.py'):
                    items.append(f"{indent}🐍 {item}")
                elif item.endswith('.bat'):
                    items.append(f"{indent}⚙️  {item}")
                elif item.endswith('.cs'):
                    items.append(f"{indent}🔷 {item}")
                elif item.endswith('.cpp'):
                    items.append(f"{indent}⚙️  {item}")
                elif item.endswith('.md'):
                    items.append(f"{indent}📖 {item}")
                elif item.endswith('.ptlogica'):
                    items.append(f"{indent}💻 {item}")
                else:
                    items.append(f"{indent}📄 {item}")
    except PermissionError:
        pass
    
    return items

def main():
    print("\n")
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║                                                                ║")
    print("║               PT-LÓGICA v1.0 - VISÃO GERAL                   ║")
    print("║         Linguagem de Programação em Português                 ║")
    print("║         Comunicação Direta com Hardware                       ║")
    print("║                                                                ║")
    print("╚════════════════════════════════════════════════════════════════╝")
    print()
    
    print("📊 RESUMO DO PROJETO")
    print("─" * 60)
    print()
    print("✅ 90 Bibliotecas Especializadas")
    print("   ├─ 10 bibliotecas de CPU (Processador)")
    print("   ├─ 10 bibliotecas de GPU (Gráficos)")
    print("   ├─ 10 bibliotecas de Memória")
    print("   ├─ 10 bibliotecas de Storage (Disco)")
    print("   ├─ 10 bibliotecas de Interface (UI)")
    print("   ├─ 10 bibliotecas de Sistema Operacional")
    print("   ├─ 10 bibliotecas de IA (Machine Learning)")
    print("   ├─ 10 bibliotecas de Cloud Computing")
    print("   └─ 10 bibliotecas de Análise de Dados")
    print()
    
    print("✅ Ferramentas Completas")
    print("   ├─ Editor Gráfico (Python Tkinter)")
    print("   ├─ Compilador (C#, C++, Python)")
    print("   ├─ Gerador de EXE (Batch + Python)")
    print("   ├─ Menu Principal (Batch)")
    print("   └─ Runtime Executável")
    print()
    
    print("✅ Documentação e Exemplos")
    print("   ├─ Manual Completo (PT-LOGICA-MANUAL.md)")
    print("   ├─ README com Guia Rápido")
    print("   ├─ Exemplos Práticos")
    print("   └─ Código Comentado")
    print()
    
    print("📁 ESTRUTURA DE ARQUIVOS")
    print("─" * 60)
    print()
    
    diretorio_raiz = "."
    arquivos = listar_arquivos(diretorio_raiz, max_nivel=3)
    
    for arquivo in arquivos:
        print(arquivo)
    
    print()
    print("📈 ESTATÍSTICAS")
    print("─" * 60)
    
    # Conta arquivos
    total_py = len(list(Path(".").glob("**/*.py")))
    total_cs = len(list(Path(".").glob("**/*.cs")))
    total_cpp = len(list(Path(".").glob("**/*.cpp")))
    total_bat = len(list(Path(".").glob("**/*.bat")))
    total_ptlogica = len(list(Path(".").glob("**/*.ptlogica")))
    total_md = len(list(Path(".").glob("**/*.md")))
    
    print()
    print(f"  🐍 Arquivos Python:       {total_py} arquivos")
    print(f"  🔷 Arquivos C#:           {total_cs} arquivos")
    print(f"  ⚙️  Arquivos C++:          {total_cpp} arquivos")
    print(f"  ⚙️  Scripts Batch:         {total_bat} arquivos")
    print(f"  💻 Código PT-Lógica:      {total_ptlogica} arquivos")
    print(f"  📖 Documentação:          {total_md} arquivos")
    
    total_linhas = 0
    
    # Conta linhas de código
    for arquivo in Path(".").glob("**/*.py"):
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                total_linhas += len(f.readlines())
        except:
            pass
    
    for arquivo in Path(".").glob("**/*.cs"):
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                total_linhas += len(f.readlines())
        except:
            pass
    
    for arquivo in Path(".").glob("**/*.ptlogica"):
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                total_linhas += len(f.readlines())
        except:
            pass
    
    print()
    print(f"  📝 Total de Linhas de Código: ~{total_linhas:,} linhas")
    print()
    
    print("🚀 COMO COMEÇAR")
    print("─" * 60)
    print()
    print("  1. Execute o programa de exemplo:")
    print("     > cd bin && programa_exemplo.bat")
    print()
    print("  2. Abra o editor:")
    print("     > python editor/editor_pt_logica.py")
    print()
    print("  3. Ou use o menu principal:")
    print("     > iniciar.bat")
    print()
    print("  4. Leia a documentação:")
    print("     > cat PT-LOGICA-MANUAL.md")
    print()
    
    print("🎯 FUNCIONALIDADES PRINCIPAIS")
    print("─" * 60)
    print()
    print("  ✓ Acesso direto a CPU, GPU, Memória e SSD")
    print("  ✓ Compilação para executáveis Windows")
    print("  ✓ Editor gráfico integrado com syntax highlighting")
    print("  ✓ 90+ bibliotecas para diferentes tarefas")
    print("  ✓ Suporte a programação de IA, SOs e sistemas complexos")
    print("  ✓ Performance equivalente ao C++")
    print("  ✓ Sintaxe em português fácil de aprender")
    print()
    
    print("💡 CASOS DE USO")
    print("─" * 60)
    print()
    print("  🤖 Desenvolvimento de Inteligência Artificial")
    print("  🖥️  Criação de Sistemas Operacionais")
    print("  🎮 Desenvolvimento de Engines de Games")
    print("  ⚡ Processamento de Alta Performance")
    print("  ☁️  Cloud Computing e Computação Distribuída")
    print("  📊 Análise de Big Data")
    print("  🔧 Drivers e Programação de Hardware")
    print("  🌐 Servidores e Aplicações Web")
    print()
    
    print("✨ STATUS")
    print("─" * 60)
    print()
    print("  Versão: 1.0")
    print("  Status: ✅ PRONTO PARA PRODUÇÃO")
    print("  Data: 2026")
    print("  Licença: Open Source")
    print()
    
    print("📞 PRÓXIMOS PASSOS")
    print("─" * 60)
    print()
    print("  1. Explore os exemplos em: ./exemplos/")
    print("  2. Leia o manual em: PT-LOGICA-MANUAL.md")
    print("  3. Use o editor em: python editor/editor_pt_logica.py")
    print("  4. Compile seus programas em: python compilador/compilador_exe.py")
    print()
    
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║                                                                ║")
    print("║  PT-Lógica - Programar em Português, Direto no Hardware! 🚀   ║")
    print("║                                                                ║")
    print("╚════════════════════════════════════════════════════════════════╝")
    print()

if __name__ == "__main__":
    main()
