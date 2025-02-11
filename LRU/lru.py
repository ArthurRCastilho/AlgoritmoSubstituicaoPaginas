import numpy as np
import random

# Definição de constantes para a simulação
NUM_PAGINAS_SWAP = 100  # Número total de páginas na SWAP
NUM_PAGINAS_RAM = 10  # Número total de páginas na RAM
CAMPOS = 6  # Número de atributos para cada página

# Índices dos campos dentro da matriz
N, I, D, R, M, T = range(CAMPOS)

# Inicializa a matriz SWAP com páginas fictícias
matriz_swap = np.zeros((NUM_PAGINAS_SWAP, CAMPOS), dtype=int)
for i in range(NUM_PAGINAS_SWAP):
    matriz_swap[i] = [
        i,  # Número da página
        i + 1,  # Identificador fictício da instrução associada
        random.randint(1, 50),  # Dado aleatório para simular modificações
        0,  # Bit de Referência (R), indicando se foi acessada
        0,  # Bit de Modificação (M), indicando se foi alterada
        random.randint(100, 9999)  # Timestamp fictício para envelhecimento
    ]

# Inicializa a matriz RAM com páginas aleatórias da SWAP
matriz_ram = np.zeros((NUM_PAGINAS_RAM, CAMPOS), dtype=int)
indices_ram = random.sample(range(NUM_PAGINAS_SWAP), NUM_PAGINAS_RAM)
for i, index in enumerate(indices_ram):
    matriz_ram[i] = matriz_swap[index]

# Dicionário para rastrear o envelhecimento das páginas na RAM
envelhecimento = {matriz_ram[i, N]: 0 for i in range(NUM_PAGINAS_RAM)}

# Número total de instruções a serem processadas
num_instrucoes = 1000
reset_r_counter = 0  # Contador para resetar bits de referência periodicamente

def substituir_pagina(nova_pagina):
    """ Substitui a página menos recentemente utilizada (LRU) por uma nova página. """
    global matriz_ram, envelhecimento

    # Verifica se a página existe na SWAP
    swap_indices = np.where(matriz_swap[:, N] == nova_pagina)[0]
    if swap_indices.size == 0:
        return  # Se não existir, não faz nada
    
    # Encontra a página na RAM que está há mais tempo sem uso (menor timestamp)
    pagina_substituir = min(envelhecimento, key=envelhecimento.get)
    idx_substituir = np.where(matriz_ram[:, N] == pagina_substituir)[0][0]
    
    # Se a página que será removida foi modificada (M = 1), grava de volta na SWAP
    if matriz_ram[idx_substituir, M] == 1:
        swap_idx = np.where(matriz_swap[:, N] == matriz_ram[idx_substituir, N])[0][0]
        matriz_swap[swap_idx] = matriz_ram[idx_substituir]
        matriz_swap[swap_idx, M] = 0  # Resetando o bit de modificação na SWAP
    
    # Substitui a página na RAM pela nova página da SWAP
    matriz_ram[idx_substituir] = matriz_swap[swap_indices[0]]

    # Atualiza o envelhecimento da nova página
    envelhecimento[nova_pagina] = num_instrucoes - reset_r_counter
    del envelhecimento[pagina_substituir]  # Remove a página antiga do rastreamento

def processar_instrucao(instrucao):
    """ Processa uma instrução e atualiza as estruturas de memória. """
    global reset_r_counter
    
    # Verifica se a instrução já está na RAM
    idx_ram = np.where(matriz_ram[:, I] == instrucao)[0]
    
    if idx_ram.size > 0:  
        # Se a página está na RAM, marca como acessada
        idx = idx_ram[0]
        matriz_ram[idx, R] = 1  # Define o bit de referência
        
        # Simula a chance de modificar a página (50% de chance)
        if random.random() < 0.5:
            matriz_ram[idx, D] += 1
            matriz_ram[idx, M] = 1  # Marca a página como modificada
        
        # Atualiza o envelhecimento da página na RAM
        envelhecimento[matriz_ram[idx, N]] = num_instrucoes - reset_r_counter
    else:
        # Se a página não está na RAM, verifica se está na SWAP
        swap_indices = np.where(matriz_swap[:, I] == instrucao)[0]
        if swap_indices.size > 0:
            nova_pagina = matriz_swap[swap_indices[0], N]
            substituir_pagina(nova_pagina)  # Executa a substituição

    # Incrementa o contador e reseta os bits R a cada 10 instruções
    reset_r_counter += 1
    if reset_r_counter % 10 == 0:
        matriz_ram[:, R] = 0  # Reseta o bit de referência periodicamente

# Simulação: Processa as instruções e salva os resultados em arquivos
with open("matriz_swap.txt", "w") as f_swap, open("matriz_ram.txt", "w") as f_ram:
    for _ in range(num_instrucoes):
        instrucao_sorteada = random.randint(1, 100)
        processar_instrucao(instrucao_sorteada)

        np.savetxt(f_swap, matriz_swap, fmt="%d")
        np.savetxt(f_ram, matriz_ram, fmt="%d")

print("Simulação concluída! Dados salvos em arquivos txt.")
