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
int non_atomic_counter = 0;

int current_thread_index;

struct timespec ts = {0, 10000L};

void *mythread(void *arg) {
	int thread_index = *(int *)arg;
	int copy_thread_index = thread_index;
	while (!__atomic_compare_exchange_n(&current_thread_index,
										&copy_thread_index, thread_index, 0,
										__ATOMIC_ACQ_REL, __ATOMIC_RELAXED)) {
		nanosleep(&ts, NULL);
		copy_thread_index = thread_index;
	}
	printf("Thread %d\n", thread_index);
	for (int n = 0; n < 1000; ++n) {
		++non_atomic_counter;
		__atomic_fetch_add(&atomic_counter, 1, __ATOMIC_SEQ_CST);
	}
	__atomic_compare_exchange_n(&current_thread_index, &thread_index,
								thread_index + 1, 0, __ATOMIC_ACQ_REL,
								__ATOMIC_RELAXED);
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
	printf("atomic     %d\n", atomic_counter);
	printf("non-atomic %d\n", non_atomic_counter);
}
