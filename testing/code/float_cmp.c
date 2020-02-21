// Test file for float compares
#include <stdio.h>
#include <stdlib.h>

typedef union {
    unsigned long int ui;
    double d;
} flpun;

double random_double() {
    // int mul = 4;
    // double d = mul; // Indirect to avoid inline FP in ASM (not supported in R-V)
    return (double)rand()/(double)(RAND_MAX);
}

int main () {
    srand(123); // For reproducibility
    int a = 2;
    flpun x, y;
    x.d = a;
    y.d = a; // First run tests equality
    for (int i = 0; i < 1000; i++) {
        printf("%lu, %lu\t", x.ui, y.ui);
        if (x.d < y.d) {
            printf("<");
        }
        if (x.d > y.d) {
            printf(">");
        }
        if (x.d <= y.d) {
            printf("<=");
        }
        if (x.d >= y.d) {
            printf(">=");
        }
        if (x.d == y.d) {
            printf("==");
        }
        if (x.d != y.d) {
            printf("!=");
        }
        printf("\n");
        // Putting at the end so the first time will test equality
        x.d = random_double();
        y.d = random_double();
    }
    return 0;
}
