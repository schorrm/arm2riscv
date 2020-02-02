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
int min_check = 10000;
unsigned int unsigned_min_check = 10000;
int max_check = 0;
unsigned int unsigned_max_check = 0;

struct timespec ts = {0, 1000L};


void *mythread(void *arg) {
	int thread_index = *(int *)arg;
	int copy_thread_index = thread_index;

	for (int n = 0; n < 10; n++) {
		__atomic_fetch_add(&atomic_counter, 1, __ATOMIC_SEQ_CST);
		__atomic_fetch_add(&total_sum, thread_index, __ATOMIC_SEQ_CST);
		__atomic_fetch_xor(&xor_check, thread_index, __ATOMIC_SEQ_CST);
		__atomic_fetch_or(&or_check, thread_index, __ATOMIC_SEQ_CST);
		// __atomic_fetch_add(&total_sum, thread_index, __ATOMIC_SEQ_CST);
		// atomic_max
	}

	return NULL;
}

int main(void) {
	int i;
	pthread_t threads[NUM_THREADS];
	for (i = 0; i < NUM_THREADS; ++i) {
		int *arg = malloc(sizeof(*arg));
		*arg = i;
		pthread_create(&threads[i], NULL, mythread, arg);
	}
	for (i = 0; i < NUM_THREADS; ++i)
		pthread_join(threads[i], NULL);
	printf("atomic add %d\n", atomic_counter);
	printf("atomic ad2 %d\n", total_sum);
	printf("atomic xor %d\n", xor_check);
	printf("atomic or  %d\n", or_check);
	// printf("non-atomic %d\n", non_atomic_counter); // Non-Atomic counter will fault here
}
