@echo off
REM PT-LÓGICA - Menu Principal
REM Central de Controle para toda a plataforma

setlocal enabledelayedexpansion

:menu
cls
chcp 65001 > nul

echo.
echo ╔═══════════════════════════════════════════════════════════╗
echo ║                                                           ║
echo ║            PT-LÓGICA - CENTRAL DE CONTROLE               ║
echo ║            Linguagem de Programação em Português         ║
echo ║            Versão 1.0 - Hardware Communication           ║
echo ║                                                           ║
echo ╚═══════════════════════════════════════════════════════════╝
echo.

echo [MENU PRINCIPAL]
echo ─────────────────────────────────────────────────────────
echo.
echo   1) 📝 Abrir Editor PT-Lógica
echo   2) ▶️  Executar Programa de Exemplo
echo   3) 🛠️  Compilar Novo Programa
echo   4) 📚 Ver Bibliotecas Disponíveis
echo   5) 📖 Ler Documentação Completa
echo   6) 📁 Abrir Explorador de Arquivos
echo   7) ⚙️  Configurações
echo   8) ❌ Sair
echo.
echo ─────────────────────────────────────────────────────────

set /p opcao="Digite sua opção (1-8): "

if "%opcao%"=="1" goto abrir_editor
if "%opcao%"=="2" goto executar_exemplo
if "%opcao%"=="3" goto compilar
if "%opcao%"=="4" goto bibliotecas
if "%opcao%"=="5" goto documentacao
if "%opcao%"=="6" goto explorador
if "%opcao%"=="7" goto config
if "%opcao%"=="8" goto sair

echo.
echo [ERRO] Opção inválida! Digite 1-8
pause
goto menu

:abrir_editor
cls
echo [ABRINDO] Editor PT-Lógica...
echo.
python editor\editor_pt_logica.py
if %errorlevel% neq 0 (
    echo [ERRO] Falha ao abrir editor
    echo [INFO] Certifique-se que Python está instalado
    pause
)
goto menu

:executar_exemplo
cls
echo [EXECUTANDO] Programa de Exemplo...
echo.
start cmd /k "cd bin && programa_exemplo.bat"
timeout /t 2 /nobreak > nul
goto menu

:compilar
cls
echo [COMPILAÇÃO] Novo Programa
echo ─────────────────────────────────────────────────────
echo.
set /p arquivo="Nome do arquivo PT-Lógica (ex: meu_programa.ptlogica): "

if not exist "%arquivo%" (
    echo [ERRO] Arquivo não encontrado!
    pause
    goto menu
)

echo.
echo [COMPILANDO] %arquivo%...
python compilador\compilador_exe.py "%arquivo%"

if %errorlevel% equ 0 (
    echo.
    echo [SUCESSO] Programa compilado com sucesso!
    echo.
    set /p executar="Deseja executar agora? (s/n): "
    if "!executar!"=="s" (
        set "exe_name=%arquivo:~0,-9%.exe"
        if exist "!exe_name!" start !exe_name!
    )
) else (
    echo [ERRO] Falha na compilação!
)
pause
goto menu

:bibliotecas
cls
echo [BIBLIOTECAS] PT-Lógica Disponíveis
echo ═══════════════════════════════════════════════════════════
echo.

echo 📊 GRUPO 1: CPU - Controle de Processador (10 funções)
echo    PT-CPU-01 a PT-CPU-10
echo    └─ Acesso direto ao CPU, cache, núcleos, threads
echo.

echo 📊 GRUPO 2: GPU - Renderização Gráfica (10 funções)
echo    PT-GPU-11 a PT-GPU-20
echo    └─ Renderização 3D, shaders, ray tracing, CUDA
echo.

echo 📊 GRUPO 3: MEMÓRIA - Gerenciamento RAM (10 funções)
echo    PT-MEMORIA-21 a PT-MEMORIA-30
echo    └─ Alocação, heap, stack, virtual memory
echo.

echo 📊 GRUPO 4: STORAGE - Armazenamento (10 funções)
echo    PT-STORAGE-31 a PT-STORAGE-40
echo    └─ I/O disco, RAID, backup, criptografia
echo.

echo 📊 GRUPO 5: INTERFACE - GUI (10 funções)
echo    PT-INTERFACE-41 a PT-INTERFACE-50
echo    └─ Widgets, layouts, eventos, temas
echo.

echo 📊 GRUPO 6: SISTEMA OPERACIONAL - Kernel (10 funções)
echo    PT-SO-51 a PT-SO-60
echo    └─ Boot, processos, drivers, segurança
echo.

echo 📊 GRUPO 7: IA - Machine Learning (10 funções)
echo    PT-IA-61 a PT-IA-70
echo    └─ Deep learning, NLP, computer vision
echo.

echo 📊 GRUPO 8: CLOUD - Distribuição (10 funções)
echo    PT-CLOUD-71 a PT-CLOUD-80
echo    └─ Web servers, load balancing, databases
echo.

echo 📊 GRUPO 9: DADOS - Analytics (10 funções)
echo    PT-DADOS-81 a PT-DADOS-90
echo    └─ ETL, data warehouse, big data
echo.

echo ═══════════════════════════════════════════════════════════
echo TOTAL: 90 Bibliotecas Especializadas
echo.
pause
goto menu

:documentacao
cls
echo [DOCUMENTAÇÃO]
echo.
type PT-LOGICA-MANUAL.md | more
pause
goto menu

:explorador
cls
echo [ABRINDO] Explorador de Arquivos...
start explorer "!cd!"
timeout /t 1 /nobreak > nul
goto menu

:config
cls
echo [CONFIGURAÇÕES]
echo ─────────────────────────────────────────────────────────
echo.
echo 1) Verificar Python
echo 2) Verificar Compilador C#
echo 3) Listar Arquivos de Projeto
echo 4) Voltar
echo.

set /p opcao_config="Digite sua opção: "

if "%opcao_config%"=="1" (
    cls
    echo [VERIFICAÇÃO] Python
    python --version
    echo.
    pause
)

if "%opcao_config%"=="2" (
    cls
    echo [VERIFICAÇÃO] C# Compiler
    csc /? > nul 2>&1
    if %errorlevel% equ 0 (
        echo ✓ CSC encontrado
    ) else (
        echo ✗ CSC não encontrado
    )
    echo.
    pause
)

if "%opcao_config%"=="3" (
    cls
    echo [ARQUIVOS] Estrutura do Projeto
    echo.
    tree /f /a 2>nul || dir /s /b
    echo.
    pause
)

if "%opcao_config%"=="4" goto menu

goto menu

:sair
cls
echo ╔═══════════════════════════════════════════════════════════╗
echo ║                                                           ║
echo ║             Obrigado por usar PT-Lógica!                 ║
echo ║                                                           ║
echo ║  Para mais informações, visite a documentação:           ║
echo ║  PT-LOGICA-MANUAL.md                                     ║
echo ║                                                           ║
echo ║  Feliz Programação em Português!  🇧🇷                     ║
echo ║                                                           ║
echo ╚═══════════════════════════════════════════════════════════╝
echo.
endlocal
exit /b 0
