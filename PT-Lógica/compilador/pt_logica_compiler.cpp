#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <regex>
#include <windows.h>

using namespace std;

// ============================================
// PT-LÓGICA - COMPILADOR PRINCIPAL
// Linguagem de Programação em Português
// Comunicação Direta com Hardware
// ============================================

class PTLogicaCompiler {
private:
    map<string, string> keywords;
    map<string, int> variables;
    vector<string> compiled_code;
    
public:
    PTLogicaCompiler() {
        initializeKeywords();
    }
    
    void initializeKeywords() {
        // Palavras-chave PT-Lógica
        keywords["PT-pt"] = "INICIO";
        keywords["PT-inclusao"] = "INCLUDE";
        keywords["PT-variavel"] = "VAR";
        keywords["PT-condicao"] = "IF";
        keywords["PT-laco"] = "LOOP";
        keywords["PT-funcao"] = "FUNC";
        keywords["PT-retorno"] = "RETURN";
        keywords["PT-escrever"] = "WRITE";
        keywords["PT-ler"] = "READ";
        keywords["PT-cpu"] = "CPU_ACCESS";
        keywords["PT-gpu"] = "GPU_ACCESS";
        keywords["PT-memoria"] = "MEMORY_ACCESS";
        keywords["PT-ssd"] = "STORAGE_ACCESS";
        keywords["PT-executar"] = "RUN";
        keywords["PT-finalizar"] = "EXIT";
    }
    
    bool validateSyntax(string line) {
        // Validação básica de sintaxe PT-Lógica
        if (line.empty()) return true;
        if (line[0] == '/') return true; // Comentário
        
        // Verifica se começa com PT-pt
        if (line.find("PT-pt") != 0 && line.find("PT-inclusao") != 0) {
            if (!line.empty() && line[0] != ' ') {
                return false;
            }
        }
        return true;
    }
    
    string parseInclude(string line) {
        // PT-inclusao>"PT-cpu"<
        regex include_pattern("PT-inclusao>\"([^\"]+)\"<");
        smatch match;
        
        if (regex_search(line, match, include_pattern)) {
            return match[1].str();
        }
        return "";
    }
    
    string parseVariable(string line) {
        // PT-pt(variavel)<tipo-valor>
        regex var_pattern("PT-pt\\(([^)]+)\\)<([^>]+)>");
        smatch match;
        
        if (regex_search(line, match, var_pattern)) {
            return match[1].str() + ":" + match[2].str();
        }
        return "";
    }
    
    bool compile(const string& input_file, const string& output_file) {
        ifstream infile(input_file);
        if (!infile.is_open()) {
            cout << "[ERRO] Não foi possível abrir o arquivo: " << input_file << endl;
            return false;
        }
        
        string line;
        cout << "[COMPILAÇÃO] Iniciando compilação de: " << input_file << endl;
        
        while (getline(infile, line)) {
            if (!validateSyntax(line)) {
                cout << "[AVISO] Sintaxe inválida: " << line << endl;
                continue;
            }
            
            // Processa diferentes tipos de instruções
            if (line.find("PT-inclusao") != string::npos) {
                string lib = parseInclude(line);
                compiled_code.push_back("INCLUDE: " + lib);
                cout << "[INCLUSO] Biblioteca carregada: " << lib << endl;
            }
            else if (line.find("PT-pt") != string::npos) {
                compiled_code.push_back(line);
            }
        }
        
        infile.close();
        
        // Escreve código compilado
        ofstream outfile(output_file);
        for (const string& code : compiled_code) {
            outfile << code << "\n";
        }
        outfile.close();
        
        cout << "[SUCESSO] Compilação concluída! Arquivo: " << output_file << endl;
        return true;
    }
};

int main() {
    SetConsoleCP(65001);
    SetConsoleOutputCP(65001);
    
    cout << "╔═══════════════════════════════════════════════════════╗\n";
    cout << "║         PT-LÓGICA - COMPILADOR v1.0                  ║\n";
    cout << "║    Linguagem de Programação em Português             ║\n";
    cout << "║    Comunicação Direta com Hardware (CPU/GPU)         ║\n";
    cout << "╚═══════════════════════════════════════════════════════╝\n\n";
    
    PTLogicaCompiler compiler;
    
    string input = "exemplo.ptlogica";
    string output = "exemplo.compiled";
    
    if (compiler.compile(input, output)) {
        cout << "\n[INFO] Próximo passo: Execute o programa com o interpretador\n";
    }
    
    return 0;
}
