# LRU (Least Recently Used)

## Quem fez?

[Gabriel Cândido Ferreira Dias](https://github.com/Gabriel-Candido-Ferreira)  

### 🔍 O que é substituição de páginas?
Em sistemas operacionais, quando um processo precisa acessar uma página de memória que não está carregada na RAM (Page Fault), o sistema precisa substituir uma página antiga por uma nova. O objetivo dos algoritmos de substituição de páginas é escolher qual página remover para minimizar impactos no desempenho.

### 🛠 Como funciona o LRU?
O algoritmo LRU (Least Recently Used) substitui a página que não foi utilizada há mais tempo. Esse método presume que páginas usadas recentemente tendem a ser usadas novamente em breve, enquanto páginas menos utilizadas são menos prováveis de serem acessadas novamente.

1️⃣ Manter um histórico de acesso

Cada página na RAM tem um contador que registra a última vez que foi acessada. Esse histórico é atualizado a cada nova instrução processada.

2️⃣ Verificar se a página está na RAM

Se a página solicitada está na RAM, ela tem seu contador atualizado para indicar que foi recentemente utilizada.

Se a página não está na RAM, ocorre um Page Fault e uma página precisa ser substituída.

3️⃣ Substituir a página menos utilizada

O algoritmo encontra a página que tem o contador mais antigo (ou seja, a que foi usada há mais tempo) e a substitui pela nova página solicitada.

4️⃣ Atualizar os contadores

Depois de cada substituição, os contadores de todas as páginas são ajustados para refletir a ordem de acesso correta.

#### 📌 Resumo da lógica
✅ LRU → Substitui a página que foi menos usada recentemente, otimizando a alocação de memória.

### 📌 Vantagens do LRU
- Evita substituir páginas que estão sendo usadas com frequência.
- Tem melhor desempenho em comparação com FIFO em cenários reais de execução.
- Se aproxima de uma gestão ótima de memória, pois segue padrões de uso previsíveis.

### ⚠ Desvantagens do LRU
- Requer maior controle e armazenamento de histórico de acessos.
- Pode ser ineficiente em sistemas que têm um alto volume de trocas de páginas.

### 🚀 Aplicação no código

- No código desenvolvido, a lógica do LRU foi aplicada através do dicionário envelhecimento, que rastreia o tempo de uso de cada página na RAM. Quando uma nova página precisa ser carregada e não há espaço disponível, a página com o maior tempo de inatividade é substituída.

- A função substituir_pagina(nova_pagina) realiza essa troca, garantindo que a página menos recentemente usada seja removida e a nova página seja inserida corretamente.

- A cada execução da função processar_instrucao(instrucao), o acesso às páginas é atualizado e o contador de tempo é ajustado para manter a coerência do algoritmo.

