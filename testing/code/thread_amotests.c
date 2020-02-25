#define _XOPEN_SOURCE 700
#include <pthread.h>
#include <stdatomic.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

enum Constants {
	NUM_THREADS = 1000,
};

int atomic_counter = 0;
int total_sum = 0;
int or_check = 0;
int xor_check = 0;
int and_check = 1000;
int and_check_2 = 1000;
long int min_check = 10000;
long unsigned int unsigned_min_check = 10000;
long int max_check = 0;
long unsigned int unsigned_max_check = 0;

struct timespec ts = {0, 1000L};

/* Overview:
 * 
 * We're going to stress test the atomics here, failure to translate 
 * correctly or include the correct semantics will result in misordered 
 * instructions and hence garble the answers (e.g. XORs will not cancel out)
 * 
 */


void *mythread(void *arg) {
	int thread_index = *(int *)arg;
	int copy_thread_index = thread_index;

	for (int n = 0; n < 10; n++) {
		// For each of these intrinsics, we expect the AArch64 --> RISC-V chain:
		// ldadd --> amoadd
		__atomic_fetch_add(&atomic_counter, 1, __ATOMIC_SEQ_CST);
		__atomic_fetch_add(&total_sum, thread_index, __ATOMIC_SEQ_CST);
		// ldeor --> amoxor
		__atomic_fetch_xor(&xor_check, thread_index, __ATOMIC_SEQ_CST);
		// ldset --> amoor
		__atomic_fetch_or(&or_check, thread_index, __ATOMIC_SEQ_CST);
		// ldclr --> not + amoand
		atomic_fetch_and(&and_check, 1000-thread_index);
		atomic_fetch_and(&and_check_2, 1000);
		
		// No intrinsics available for various min / max
		// ldsmin --> amomin
		asm("ldsminal %[t], %[t], %[min_check]" : [min_check] "=m" (min_check) : [t] "r" (thread_index));
		// ldsmax --> amomax
		asm("ldsmaxal %[t], %[t], %[max_check]" : [max_check] "=m" (max_check) : [t] "r" (thread_index));
		// ldumin --> amominu
		asm("lduminal %[t], %[t], %[umin_check]" : [umin_check] "=m" (unsigned_min_check) : [t] "r" (thread_index));
		// ldumax --> amomaxu
		asm("ldumaxal %[t], %[t], %[umax_check]" : [umax_check] "=m" (unsigned_max_check) : [t] "r" (thread_index));
	}

	return NULL;
}

int main(void) {
	int i;
	pthread_t threads[NUM_THREADS];
	for (i = 0; i < NUM_THREADS; i++) {
		int *arg = malloc(sizeof(*arg));
		*arg = i;
		pthread_create(&threads[i], NULL, mythread, arg);
	}
	for (i = 0; i < NUM_THREADS; i++) {
		pthread_join(threads[i], NULL);
	}
	printf("atomic add %d\n", atomic_counter);
	printf("atomic ad2 %d\n", total_sum);
	printf("atomic xor %d\n", xor_check);
	printf("atomic or  %d\n", or_check);
	printf("atomic and %d\n", and_check);
	printf("atomic an2 %d\n", and_check_2);
	printf("atomic min %ld\n", min_check);
	printf("atomic max %ld\n", max_check);
	printf("atomic umn %ld\n", unsigned_min_check);
	printf("atomic umx %ld\n", unsigned_max_check);
	
	// printf("non-atomic %d\n", non_atomic_counter); // Non-Atomic counter will fault here
}
