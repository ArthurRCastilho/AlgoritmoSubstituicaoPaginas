# FIFO-SC (FIFO Second-Chance)

## Quem fez?

[Arthur Rodrigues Castilho](https://github.com/ArthurRCastilho) <br>


### 🔍 O que é substituição de páginas?
Em sistemas operacionais, quando um processo precisa acessar uma página de memória que não está carregada na RAM (Page Fault), o sistema precisa substituir uma página antiga por uma nova. O objetivo dos algoritmos de substituição de páginas é escolher qual página remover para minimizar impactos no desempenho.

### 🛠 Como funciona o FIFO-SC?
O algoritmo FIFO-SC é uma melhoria do FIFO (First-In-First-Out), que substitui simplesmente a página que está há mais tempo na memória. O problema do FIFO puro é que ele pode remover páginas que ainda estão sendo usadas. Para evitar isso, o FIFO-SC adiciona um bit de acesso (R) como critério secundário.<br>

1️⃣ Manter uma fila<br>

As páginas na RAM são organizadas em uma fila circular.<br>
A mais antiga está no início e a mais recente no fim.<br>

2️⃣ Verificar o Bit R (Acesso)<br>

Antes de substituir uma página, o FIFO-SC verifica se o bit R da página é 0.
Se R = 0, a página é substituída imediatamente.
Se R = 1, significa que a página foi acessada recentemente, então:
O bit R é resetado para 0.
A página recebe uma "segunda chance" e é movida para o final da fila.
O algoritmo então repete o processo com a próxima página da fila.<br>

3️⃣ Substituir a Página

Quando encontra uma página com R = 0, ela é substituída pela nova página.<br>
#### 📌 Resumo da lógica
✅ FIFO puro → Remove a página mais antiga sem considerar se ainda está sendo usada.
✅ FIFO-SC → Dá uma segunda chance para páginas que foram acessadas recentemente.