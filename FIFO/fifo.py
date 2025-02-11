import numpy as np
import random


swap = np.zeros((100, 6), dtype=int)
ram = np.zeros((10, 6), dtype=int)


for i in range(100):
    swap[i] = [i, i + 1, random.randint(1, 50), 0, 0, random.randint(100, 9999)]


indices_ram = random.sample(range(100), 10)
for i, index in enumerate(indices_ram):
    ram[i] = swap[index]


fifo_queue = list(indices_ram)  

def imprimir_matrizes():
    print("\nMATRIZ RAM:")
    print(ram)
    print("\nMATRIZ SWAP:") 
    print(swap[:15]) 

imprimir_matrizes()


for instrucao in range(1000):
    instrucao_atual = random.randint(1, 100)
    encontrada = False

   
    for linha in ram:
        if linha[1] == instrucao_atual:  
            linha[3] = 1  
            if random.random() < 0.5:  
                linha[2] += 1  
                linha[4] = 1  
            encontrada = True
            break

    if not encontrada:
       
        pagina_removida = fifo_queue.pop(0)
        
       
        for i in range(10):
            if ram[i][0] == pagina_removida:
                if ram[i][4] == 1:
                    swap[ram[i][0]] = ram[i]
                    swap[ram[i][0]][4] = 0 
                break

        nova_pagina = random.choice(swap)
        ram[i] = nova_pagina
        fifo_queue.append(nova_pagina[0])

   
    if instrucao % 10 == 0:
        for linha in ram:
            linha[3] = 0

print("\nApós execução das 1000 instruções:")
imprimir_matrizes()
