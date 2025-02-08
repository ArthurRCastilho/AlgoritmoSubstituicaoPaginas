import random

# 📌 Tamanho das matrizes
TOTAL_PAGINAS = 100  # SWAP tem 100 páginas
TOTAL_MOLDURAS = 10  # RAM tem 10 molduras

# 📌 Estrutura da Página: [N, I, D, R, M, T]
def criar_matriz_swap():
    """Cria e inicializa a matriz SWAP (100x6)."""
    swap = []
    for i in range(TOTAL_PAGINAS):
        swap.append([
            i,  # N (Número da Página)
            i + 1,  # I (Instrução)
            random.randint(1, 50),  # D (Dado)
            0,  # R (Bit de Acesso)
            0,  # M (Bit de Modificação)
            random.randint(100, 9999)  # T (Tempo de Envelhecimento)
        ])
    return swap

def criar_matriz_ram(swap):
    """Cria a matriz RAM (10x6) sorteando páginas da SWAP."""
    ram = []
    paginas_carregadas = random.sample(range(TOTAL_PAGINAS), TOTAL_MOLDURAS)
    for i in paginas_carregadas:
        ram.append(swap[i][:])  # Copia os dados da SWAP
    return ram

def imprimir_matriz(matriz, nome):
    """Imprime a matriz formatada."""
    print(f"\n📌 {nome}")
    print("N\tI\tD\tR\tM\tT")
    for linha in matriz:
        print("\t".join(map(str, linha)))

def substituir_pagina_relogio(ram, swap, ponteiro):
    """
    Substitui uma página na RAM usando o Algoritmo do Relógio.
    - Percorre as páginas circulando pela RAM.
    - Se encontrar R=0, substitui a página.
    - Se encontrar R=1, zera R e avança.
    """
    while True:
        # Página apontada pelo ponteiro
        pagina = ram[ponteiro]

        if pagina[3] == 0:  # Se R == 0, pode substituir
            if pagina[4] == 1:  # Se M == 1, salvar na SWAP antes de remover
                swap[pagina[0]] = pagina[:]
                swap[pagina[0]][4] = 0  # Resetando M na SWAP
            
            return ponteiro  # Retorna índice da página a ser substituída
        
        else:
            # Se R == 1, zera o bit e avança o ponteiro
            ram[ponteiro][3] = 0
            ponteiro = (ponteiro + 1) % TOTAL_MOLDURAS  # Movimento circular

def executar_simulacao(swap, ram):
    """Executa 1000 instruções simulando page faults e substituições."""
    ponteiro = 0  # Ponteiro do Relógio
    for i in range(1000):
        instrucao = random.randint(1, 100)  # Sorteia uma instrução

        # Verifica se a instrução já está na RAM
        presente_na_ram = next((pagina for pagina in ram if pagina[1] == instrucao), None)

        if presente_na_ram:
            # Se estiver na RAM, seta R=1 e verifica modificação
            presente_na_ram[3] = 1  # R = 1
            if random.random() < 0.5:  # 50% de chance de modificação
                presente_na_ram[2] += 1  # D = D + 1
                presente_na_ram[4] = 1  # M = 1
        else:
            # Se não estiver na RAM, ocorre page fault
            indice_substituir = substituir_pagina_relogio(ram, swap, ponteiro)
            nova_pagina = swap[instrucao - 1][:]  # Pega página da SWAP
            ram[indice_substituir] = nova_pagina  # Substitui na RAM
            ponteiro = (indice_substituir + 1) % TOTAL_MOLDURAS  # Atualiza ponteiro

        # A cada 10 instruções, zera os bits R
        if i % 10 == 0:
            for pagina in ram:
                pagina[3] = 0

# 📌 Inicializando as matrizes
matriz_swap = criar_matriz_swap()
matriz_ram = criar_matriz_ram(matriz_swap)

# 📌 Imprimindo estado inicial
imprimir_matriz(matriz_swap, "MATRIZ SWAP (Inicial)")
imprimir_matriz(matriz_ram, "MATRIZ RAM (Inicial)")

# 📌 Executando a simulação
executar_simulacao(matriz_swap, matriz_ram)

# 📌 Imprimindo estado final
imprimir_matriz(matriz_swap, "MATRIZ SWAP (Final)")
imprimir_matriz(matriz_ram, "MATRIZ RAM (Final)")
