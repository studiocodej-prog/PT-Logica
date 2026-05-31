PT-inclusao>"PT-cpu"<
PT-inclusao>"PT-memoria"<
PT-inclusao>"PT-gpu"<

PT-pt(programa-principal)<
    
    // Abre e inicia comunicação com CPU
    PT-pt()<Abrir-codigo><conversar-processador-cpu>
    
        // Aloca memória para variáveis
        PT-pt(alocar-memoria)<
            PT-pt()<nucleos{4}>
            PT-pt()<frequencia-ghz{3.5}>
        PT-pt()>finalizar
        
        // Ativa núcleos de processamento
        PT-pt(ativar-nucleos)<
            PT-pt()<nucleo-1{ativo}>
            PT-pt()<nucleo-2{ativo}>
            PT-pt()<nucleo-3{ativo}>
            PT-pt()<nucleo-4{ativo}>
            PT-pt()<guardar-um-nucleo{4/2=2-nucleos}>
        PT-pt()>finalizar
        
        // Monitora desempenho
        PT-pt(monitorar-cpu)<
            PT-pt()<temperatura-atual{65.5}>
            PT-pt()<uso-percentual{45%}>
            PT-pt()<frequencia-dinamica{3.8GHz}>
        PT-pt()>finalizar
        
        // GPU acceleration para processamento paralelo
        PT-pt(renderizar-com-gpu)<
            PT-pt()<shader-vertex{compilado}>
            PT-pt()<shader-fragment{compilado}>
            PT-pt()<texturas-carregadas{128MB}>
        PT-pt()>finalizar
        
        // Sincroniza dados em memória
        PT-pt(sincronizar-memoria)<
            PT-pt()<heap-status{80% utilizado}>
            PT-pt()<cache-status{L1:32KB, L2:256KB, L3:8MB}>
        PT-pt()>finalizar
        
    // Fecha comunicação com CPU
    PT-pt(Fechar-codigo)<terminar-de-conversar-e-programar>
    
PT-pt()>finalizar

// Executa o programa
PT-pt()<executar>

// Saída esperada:
// [SISTEMA] Comunicação iniciada com CPU
// [PROCESSADOR] 4 núcleos ativados a 3.5 GHz
// [GPU] Renderização acelerada iniciada
// [MEMÓRIA] Alocação de 2GB realizada
// [MONITORAMENTO] CPU: 45%, Temp: 65.5°C
// [SINCRONIZAÇÃO] Memória sincronizada
// [SISTEMA] Programa finalizado com sucesso

