# Simulador de Algoritmo de Substituição de Páginas - Algoritmo do Relógio

## 📌 Introdução
Este projeto implementa um simulador para execução de algoritmos de substituição de páginas em um ambiente de memória virtual. A parte deste trabalho realizada por [Wisley César ](https://github.com/wisley-cesar) refere-se à implementação do **algoritmo do Relógio**, um método eficiente de substituição de páginas.

## 📌 Descrição do Algoritmo do Relógio
O algoritmo do Relógio é uma melhoria sobre o algoritmo FIFO (First-In, First-Out), usando um ponteiro circular para gerenciar a substituição de páginas. As regras são:

1. Cada página na RAM possui um bit de acesso (R).
2. O ponteiro percorre as molduras de páginas na RAM verificando o bit R:
   - Se **R = 0**, a página é substituída.
   - Se **R = 1**, o bit é resetado para 0 e o ponteiro avança.
3. O processo continua até encontrar uma página com **R = 0** para substituição.
4. Se a página modificada (M = 1) for removida, seus dados são salvos na SWAP.

## 📌 Estrutura da Memória
O simulador utiliza duas matrizes:

- **MATRIZ SWAP (100x6):** Representa as páginas na memória secundária.
- **MATRIZ RAM (10x6):** Representa as molduras da memória RAM.

Cada página tem os seguintes atributos:
- **N:** Número da página.
- **I:** Instrução.
- **D:** Dado armazenado.
- **R:** Bit de acesso (1 para recentemente usada, 0 para não usada).
- **M:** Bit de modificação (1 para página alterada, 0 para inalterada).
- **T:** Tempo de envelhecimento.

## 📌 Implementação
O código da minha parte do projeto inclui:

### 🔹 Inicialização das Matrizes
- A matriz SWAP é preenchida com 100 páginas.
- A matriz RAM é populada aleatoriamente com 10 páginas vindas da SWAP.

### 🔹 Algoritmo do Relógio
- Percorre as molduras da RAM procurando uma página com **R = 0** para substituir.
- Se **R = 1**, ele é zerado e o ponteiro avança.
- A página substituída é enviada para a SWAP se **M = 1**.

### 🔹 Simulação
- 1000 instruções são executadas.
- A cada 10 instruções, todos os bits R na RAM são resetados.
- As matrizes são impressas no início e no final da simulação.

## 📌 Execução do Código
Para executar o simulador, utilize Python 3:
```sh
python simulador.py
```

## 📌 Conclusão
O algoritmo do Relógio se mostrou eficiente na substituição de páginas, equilibrando desempenho e consumo de memória. Sua estratégia circular evita substituições prematuras, melhorando a gestão da RAM.

---

Desenvolvido por [Wisley César Borges Do Vale](https://github.com/wisley-cesar)  

