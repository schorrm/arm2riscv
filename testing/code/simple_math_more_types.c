// Test file for a full range of **integer** math instructions
#include <stdint.h>
#include <stdio.h>

int main() {
    int32_t x = 99;
    int32_t y = 10;

    printf("Signed Ops:\n");
    printf("Addition: %d\n", x + y);
    printf("Subtraction: %d\n", x - y);
    printf("Multiplication: %d\n", x * y);
    printf("Division: %d\n", x / y);
    printf("Modulus: %d\n", x % y);

    x = -x;
    y = -y;

    printf("More checks with the sign:\n");
    printf("Addition: %d\n", x + y);
    printf("Subtraction: %d\n", x - y);
    printf("Multiplication: %d\n", x * y);
    printf("Division: %d\n", x / y);
    printf("Modulus: %d\n", x % y);

    uint32_t w = 99;
    uint32_t z = 10;

    printf("Unsigned Ops:\n");
    printf("Addition: %d\n", w + z);
    printf("Subtraction: %d\n", w - z);
    printf("Multiplication: %d\n", w * z);
    printf("Division: %d\n", w / z);
    printf("Modulus: %d\n", w % z);

    int64_t sllx = 1;
    sllx = sllx << 35;
    int64_t slly = 1;
    slly = slly << 34;
    printf("Testing long (64 bit) signed:\n");
    printf("Addition: %li\n", sllx + slly);
    printf("Subtraction: %li\n", sllx - slly);
    printf("Multiplication: %li\n", sllx * slly);
    printf("Division: %li\n", sllx / slly);
    printf("Modulus: %li\n", sllx % slly);

    uint64_t ullx = 1;
    ullx = ullx << 35;
    uint64_t ully = 1;
    ully = ully << 34;
    printf("Testing long (64 bit) unsigned:\n");
    printf("Addition: %lu\n", sllx + slly);
    printf("Subtraction: %lu\n", sllx - slly);
    printf("Multiplication: %lu\n", sllx * slly);
    printf("Division: %lu\n", sllx / slly);
    printf("Modulus: %lu\n", sllx % slly);

    return 0;
}