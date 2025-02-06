import numpy as np # type: ignore
import random

# Inicialização da MATRIZ SWAP (100x6)
swap = np.zeros((100, 6), dtype=int)
for i in range(100):
    swap[i][0] = i  # Número da Página (N)
    swap[i][1] = i + 1  # Instrução (I)
    swap[i][2] = random.randint(1, 50)  # Dado (D)
    swap[i][3] = 0  # Bit de Acesso (R)
    swap[i][4] = 0  # Bit de Modificação (M)
    swap[i][5] = random.randint(100, 9999)  # Tempo de Envelhecimento (T)

# Inicialização da MATRIZ RAM (10x6)
ram = np.zeros((10, 6), dtype=int)
ram_indices = random.sample(range(100), 10)
for i, idx in enumerate(ram_indices):
    ram[i] = swap[idx]

def print_matriz(nome, matriz):
    print(f"\n{nome}:")
    print("N\tI\tD\tR\tM\tT")
    for linha in matriz:
        print("\t".join(map(str, linha)))

print_matriz("MATRIZ SWAP", swap)
print_matriz("MATRIZ RAM", ram)

# Algoritmo FIFO-SC (First-In-First-Out Second-Chance)
fifo_sc_queue = list(range(10))  # Fila de páginas na RAM

def fifo_sc_substituir(nova_pagina):
    global fifo_sc_queue
    while True:
        idx = fifo_sc_queue.pop(0)
        if ram[idx][3] == 0:  # Se R == 0, substituir
            # print(f"Substituindo página {ram[idx][0]} por {nova_pagina[0]}")
            if ram[idx][4] == 1:
                swap[ram[idx][0]] = ram[idx]
                swap[ram[idx][0]][4] = 0  # Resetando M em SWAP
            ram[idx] = nova_pagina
            fifo_sc_queue.append(idx)
            return
        else:  # Se R == 1, dar segunda chance e mover para o fim da fila
            ram[idx][3] = 0
            fifo_sc_queue.append(idx)

def executar_simulador():
    global ram
    for instrucao in range(1000):
        num_instrucao = random.randint(1, 100)
        idx_ram = np.where(ram[:, 1] == num_instrucao)[0]
        if idx_ram.size > 0:
            idx = idx_ram[0]
            ram[idx][3] = 1
            if random.random() < 0.5:
                ram[idx][2] += 1
                ram[idx][4] = 1
        else:
            nova_pagina_idx = random.randint(0, 99)
            nova_pagina = swap[nova_pagina_idx].copy()
            fifo_sc_substituir(nova_pagina)
        if instrucao % 10 == 0:
            ram[:, 3] = 0  # Resetando o bit R a cada 10 instruções
    print_matriz("MATRIZ FINAL RAM", ram)
    print_matriz("MATRIZ FINAL SWAP", swap)

executar_simulador()
