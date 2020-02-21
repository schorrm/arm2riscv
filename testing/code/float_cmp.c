// Test file for float compares
#include <stdio.h>
#include <stdlib.h>

// typedef union {
//     unsigned long int ui;
//     double d;
// } flpun;

double random_double() {
    // int mul = 4;
    // double d = mul; // Indirect to avoid inline FP in ASM (not supported in R-V)
    return (double)rand()/(double)(RAND_MAX);
}

int main () {
    srand(123); // For reproducibility
    int a = 2;
    double x = a;
    double y = a; // First run tests equality
    for (int i = 0; i < 1000; i++) {
        if (x < y) {
            printf("<");
        }
        if (x > y) {
            printf(">");
        }
        if (x <= y) {
            printf("<=");
        }
        if (x >= y) {
            printf(">=");
        }
        if (x == y) {
            printf("==");
        }
        if (x != y) {
            printf("!=");
        }
        printf("\n");
        // Putting at the end so the first time will test equality
        x = random_double();
        y = random_double();
    }
    return 0;
}
