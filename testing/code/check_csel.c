#include <stdio.h>
#include <stdlib.h>

// int main(int argc, char *argv[]) {

int main() {

    // int x = atoi(argv[1]);
    // int y = atoi(argv[2]);

    int x = 32;
    int y = 35;

    int lo = 0;

    asm(
        "mov x10, %[x]\n"
        "mov x11, %[y]\n"
        "cmp x10, x11\n"
        "csel %[lo], x10, x11, LE\n"
        : [lo] "=r" (lo)
        : [x] "r" (x), [y] "r" (y)
    );

    printf("The smaller number is: %d\n", lo);
    return 0;
}