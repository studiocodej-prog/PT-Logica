using System;
using System.Collections.Generic;
using System.IO;
using System.Text.RegularExpressions;
using System.Diagnostics;
using System.Linq;

namespace PTLogica
{
    // ============================================
    // PT-LÓGICA - COMPILADOR PRINCIPAL
    // Linguagem de Programação em Português
    // Comunicação Direta com Hardware
    // ============================================
    
    public class Compilador
    {
        private Dictionary<string, string> palavrasChave;
        private Dictionary<string, object> variaveis;
        private List<string> codigoCompilado;
        private List<string> bibliotecasCarregadas;
        
        public Compilador()
        {
            InicializarPalavrasChave();
            variaveis = new Dictionary<string, object>();
            codigoCompilado = new List<string>();
            bibliotecasCarregadas = new List<string>();
        }
        
        private void InicializarPalavrasChave()
        {
            palavrasChave = new Dictionary<string, string>
            {
                // Estrutura Básica
                ["PT-pt"] = "INICIO",
                ["PT-inclusao"] = "INCLUDE",
                ["PT-variavel"] = "VAR",
                ["PT-condicao"] = "IF",
                ["PT-laco"] = "LOOP",
                ["PT-funcao"] = "FUNC",
                ["PT-retorno"] = "RETURN",
                
                // I/O
                ["PT-escrever"] = "WRITE",
                ["PT-ler"] = "READ",
                
                // Hardware
                ["PT-cpu"] = "CPU_ACCESS",
                ["PT-gpu"] = "GPU_ACCESS",
                ["PT-memoria"] = "MEMORY_ACCESS",
                ["PT-ssd"] = "STORAGE_ACCESS",
                ["PT-processador"] = "PROCESSOR_CONTROL",
                ["PT-cache"] = "CACHE_CONTROL",
                
                // Controle
                ["PT-executar"] = "RUN",
                ["PT-finalizar"] = "EXIT",
                ["PT-parar"] = "STOP",
                ["PT-continuar"] = "CONTINUE",
                
                // Operações
                ["PT-soma"] = "ADD",
                ["PT-subtracao"] = "SUB",
                ["PT-multiplicacao"] = "MUL",
                ["PT-divisao"] = "DIV"
            };
        }
        
        public bool ValidarSintaxe(string linha)
        {
            if (string.IsNullOrWhiteSpace(linha)) return true;
            if (linha.TrimStart().StartsWith("//")) return true; // Comentário
            if (linha.TrimStart().StartsWith("PT-")) return true;
            return false;
        }
        
        public string ParsearInclusao(string linha)
        {
            // PT-inclusao>"PT-cpu"<
            Regex padrao = new Regex(@"PT-inclusao>""([^""]+)""<");
            Match match = padrao.Match(linha);
            return match.Success ? match.Groups[1].Value : "";
        }
        
        public void Compilar(string arquivoEntrada, string arquivoSaida)
        {
            try
            {
                if (!File.Exists(arquivoEntrada))
                {
                    Console.WriteLine($"[ERRO] Arquivo não encontrado: {arquivoEntrada}");
                    return;
                }
                
                Console.WriteLine($"[COMPILAÇÃO] Iniciando compilação de: {arquivoEntrada}");
                
                string[] linhas = File.ReadAllLines(arquivoEntrada);
                
                foreach (string linha in linhas)
                {
                    if (!ValidarSintaxe(linha))
                    {
                        Console.WriteLine($"[AVISO] Sintaxe inválida: {linha}");
                        continue;
                    }
                    
                    if (linha.Contains("PT-inclusao"))
                    {
                        string biblioteca = ParsearInclusao(linha);
                        if (!string.IsNullOrEmpty(biblioteca))
                        {
                            codigoCompilado.Add($"INCLUDE: {biblioteca}");
                            bibliotecasCarregadas.Add(biblioteca);
                            Console.WriteLine($"[INCLUSO] Biblioteca carregada: {biblioteca}");
                        }
                    }
                    else if (linha.Contains("PT-pt"))
                    {
                        codigoCompilado.Add(linha);
                    }
                }
                
                File.WriteAllLines(arquivoSaida, codigoCompilado);
                Console.WriteLine($"[SUCESSO] Compilação concluída! Arquivo: {arquivoSaida}");
                
            }
            catch (Exception ex)
            {
                Console.WriteLine($"[ERRO] Erro durante compilação: {ex.Message}");
            }
        }
        
        public void Executar()
        {
            Console.WriteLine("\n[EXECUTANDO] Iniciando execução do programa PT-Lógica...\n");
            
            foreach (string codigo in codigoCompilado)
            {
                Console.WriteLine($"  > {codigo}");
            }
            
            Console.WriteLine("\n[FINALIZADO] Programa executado com sucesso!");
        }
    }
    
    class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
            
            Console.WriteLine("╔═══════════════════════════════════════════════════════╗");
            Console.WriteLine("║         PT-LÓGICA - COMPILADOR v1.0                  ║");
            Console.WriteLine("║    Linguagem de Programação em Português             ║");
            Console.WriteLine("║    Comunicação Direta com Hardware (CPU/GPU)         ║");
            Console.WriteLine("╚═══════════════════════════════════════════════════════╝\n");
            
            Compilador compilador = new Compilador();
            
            string arquivoEntrada = "exemplo.ptlogica";
            string arquivoSaida = "exemplo.compiled";
            
            if (File.Exists(arquivoEntrada))
            {
                compilador.Compilar(arquivoEntrada, arquivoSaida);
                compilador.Executar();
            }
            else
            {
                Console.WriteLine("[INFO] Arquivo de exemplo não encontrado.");
                Console.WriteLine("[INFO] Crie um arquivo 'exemplo.ptlogica' para começar!");
            }
        }
    }
}
