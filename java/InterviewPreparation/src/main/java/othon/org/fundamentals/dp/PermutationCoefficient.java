package othon.org.fundamentals.dp;

import lombok.extern.slf4j.Slf4j;
// https://www.geeksforgeeks.org/permutation-coefficient/
@Slf4j
public class PermutationCoefficient {
    public static void main(String[] args) {
        log.info("P({},{})={}", 10, 2,  p(10,2 ));
        int n = 10, k=2;
        int[][] mem = new int[n+1][k+1];
        log.info("P({},{})={}", n, k,  p(n,k , mem));
        log.info("P({},{})={}", n, k,  p2(n,k ));
    }

    static int p(int n, int k) {
        if (n == 0) {
            return 1;
        }
        return p(n - 1, k) + k * p(n-1, k-1);
    }
    static int p(int n, int k, int[][] mem) {
        if (n == 1) {
            return 1;
        }
        if (k ==0 ) {
            return 1;
        }
        if (mem[n][k]!=0) {
            return mem[n][k];
        }
        mem[n][k] =p(n - 1, k, mem) + k * p(n-1, k-1, mem);
        return mem[n][k];
    }
    static int p2(int n, int k) {
        int[][] mem = new int[n+1][k+1];
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= Math.min(i,k); j++) {
                // base case
                if (j==0) {
                    mem[i][0] = 1;
                } else {
                    mem[i][j] = mem[i-1][j] + (j*mem[i-1][j-1]);
                }
            }
        }
        return mem[n][k];
    }
}
