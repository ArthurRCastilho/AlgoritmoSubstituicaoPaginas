import java.util.*;

class Pagina {
    int N, I, D, R, M, T;

    public Pagina(int n, int i, int d, int t) {
        this.N = n;
        this.I = i;
        this.D = d;
        this.R = 0;
        this.M = 0;
        this.T = t;
    }

    public void resetR() {
        this.R = 0;
    }
}

class Memoria {
    Pagina[] RAM = new Pagina[10];
    Pagina[] SWAP = new Pagina[100];
    Random rand = new Random();

    public Memoria() {
        inicializarSwap();
        carregarRAM();
    }

    private void inicializarSwap() {
        for (int i = 0; i < 100; i++) {
            SWAP[i] = new Pagina(i, i + 1, rand.nextInt(50) + 1, rand.nextInt(9900) + 100);
        }
    }

    private void carregarRAM() {
        Set<Integer> indicesUsados = new HashSet<>();
        for (int i = 0; i < 10; i++) {
            int index;
            do {
                index = rand.nextInt(100);
            } while (!indicesUsados.add(index));
            RAM[i] = new Pagina(SWAP[index].N, SWAP[index].I, SWAP[index].D, SWAP[index].T);
        }
    }

    public void executarSimulacao() {
        for (int i = 0; i < 1000; i++) {
            int instrucao = rand.nextInt(100) + 1;
            boolean encontrada = false;

            for (Pagina p : RAM) {
                if (p.I == instrucao) {
                    p.R = 1;
                    if (rand.nextBoolean()) {
                        p.D++;
                        p.M = 1;
                    }
                    encontrada = true;
                    break;
                }
            }

            if (!encontrada) {
                substituirPagina(instrucao);
            }

            if ((i + 1) % 10 == 0) {
                for (Pagina p : RAM)
                    p.resetR();
            }
        }
    }

    private void substituirPagina(int instrucao) {
        int EP = rand.nextInt(9900) + 100;
        int indexSwap = -1;

        for (int i = 0; i < 10; i++) {
            Pagina p = RAM[i];
            if (EP > p.T) {
                indexSwap = i;
                break;
            }
        }

        if (indexSwap == -1) {
            for (int i = 0; i < 10; i++) {
                if (RAM[i].R == 0) {
                    indexSwap = i;
                    break;
                }
            }
        }

        if (indexSwap == -1) {
            indexSwap = 0;
        }

        if (RAM[indexSwap].M == 1) {
            SWAP[RAM[indexSwap].N] = new Pagina(RAM[indexSwap].N, RAM[indexSwap].I, RAM[indexSwap].D, RAM[indexSwap].T);
        }

        int indexNovo = rand.nextInt(100);
        RAM[indexSwap] = new Pagina(SWAP[indexNovo].N, SWAP[indexNovo].I, SWAP[indexNovo].D, SWAP[indexNovo].T);
    }

    public void imprimirMemoria() {
        System.out.println("MATRIZ RAM:");
        for (Pagina p : RAM) {
            System.out.println(p.N + " " + p.I + " " + p.D + " " + p.R + " " + p.M + " " + p.T);
        }

        System.out.println("\nMATRIZ SWAP:");
        for (Pagina p : SWAP) {
            System.out.println(p.N + " " + p.I + " " + p.D + " " + p.R + " " + p.M + " " + p.T);
        }
    }
}

public class WSClockSimulador {
    public static void main(String[] args) {
        Memoria memoria = new Memoria();
        memoria.imprimirMemoria();
        memoria.executarSimulacao();
        memoria.imprimirMemoria();
    }
}
