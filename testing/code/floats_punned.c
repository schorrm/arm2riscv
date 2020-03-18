// Test file for a full range of **float** math instructions
#include <stdio.h>


// Type punning to get past the variadic call to printf
typedef union {
    unsigned long int ui;
    double d;
} flpun;

int main() {
    flpun x, y, z, r;
    x.d = 12378.10844990232;
    y.d = 1233.99245;
    z.d = 4113.2329104;

    printf("Floating ops\n");
    r.d = x.d + y.d;
    printf("Addition: %lu\n", r.ui);
    r.d = x.d - y.d;
    printf("Subtraction: %lu\n", r.ui);
    r.d = x.d * y.d;
    printf("Multiplication: %lu\n", r.ui);
    r.d = x.d / y.d;
    printf("Divistion: %lu\n", r.ui);
        
        
    // Target the advanced ops:
    asm("fmadd %d[r], %d[x], %d[y], %d[z]"
        : [r] "=w"(r)
        : [x] "w"(x), [y] "w"(y), [z] "w"(z));
    printf("Multiply-Add: %lu\n" , r.ui);

    asm("fmsub %d[r], %d[x], %d[y], %d[z]"
        : [r] "=w"(r)
        : [x] "w"(x), [y] "w"(y), [z] "w"(z));
    printf("Multiply-Subtract: %lu\n" , r.ui);

    asm("fnmsub %d[r], %d[x], %d[y], %d[z]"
        : [r] "=w"(r)
        : [x] "w"(x), [y] "w"(y), [z] "w"(z));
    printf("Negative Multiply-Subtract: %lu\n" , r.ui);

    asm("fnmadd %d[r], %d[x], %d[y], %d[z]"
        : [r] "=w"(r)
        : [x] "w"(x), [y] "w"(y), [z] "w"(z));
    printf("Negative Multiply-Add: %lu\n" , r.ui);

    asm("fneg %d[r], %d[x]"
        : [r] "=w"(r)
        : [x] "w"(x));
    printf("FNegate: %lu\n" , r.ui);

    asm("fsqrt %d[r], %d[x]"
        : [r] "=w"(r)
        : [x] "w"(x));
    printf("Square Root: %lu \n" , r.ui);

    return 0;
}