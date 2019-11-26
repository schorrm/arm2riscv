// Test file for a full range of **integer** math instructions

#include <stdio.h>

int main() {
    int x = 99;
    int y = 10;

    printf("Signed Ops:\n");
    printf("Addition: %d\n", x + y);
    printf("Subtraction: %d\n", x - y);
    printf("Multiplication: %d\n", x * y);
    printf("Division: %d\n", x / y);
    printf("Modulus: %d\n", x % y);

    unsigned int w = 99;
    unsigned int z = 10;

    printf("Unsigned Ops:\n");
    printf("Addition: %d\n", w + z);
    printf("Subtraction: %d\n", w - z);
    printf("Multiplication: %d\n", w * z);
    printf("Division: %d\n", w / z);
    printf("Modulus: %d\n", w % z);
    return 0;
}