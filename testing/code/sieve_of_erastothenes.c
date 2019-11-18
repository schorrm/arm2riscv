#include <stdio.h>

#define N 10000
#define SQRT_N 100 // TODO: replace later with calculating the square root

int main () {
    short int composites[N + 1] = {0};
    for (int i = 2; i <= SQRT_N; i++) {
        for (int j = 2 * i; j <= N; j += i) {
            composites[j] = 1; // mark not prime with 1
        }
    }
    printf("prime numbers through %d are:\n", N);
    for (int i=2; i<=N; i++) {
        if (!composites[i]) {
            printf("%d ", i);
        }
    }
    printf("\n");
    return 0;
}