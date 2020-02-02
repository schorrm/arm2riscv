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

int current_thread_index = 0;
int thread_reader_lock = 0;

struct timespec ts = {0, 1000L};

//  load / store lock
// We can then do atomics inside or something?
void acquire_lock(int thread_index) {
	// int current = 1;
	// acquire:
	while (1) {
		int allowed_thread = __atomic_load_n(&current_thread_index, __ATOMIC_ACQUIRE);
		if (allowed_thread == thread_index) {
			break;
		}
		nanosleep(&ts, NULL);
	}
}

void release_lock(int new_lock_value) {
	__atomic_store_n(&current_thread_index, new_lock_value, __ATOMIC_RELEASE);
}

void *mythread(void *arg) {
	int thread_index = *(int *)arg;
	int copy_thread_index = thread_index;

	acquire_lock(thread_index);

	printf("Thread %d\n", thread_index);
	for (int n = 0; n < 1000; ++n) {
		++non_atomic_counter;
		__atomic_fetch_add(&atomic_counter, 1, __ATOMIC_SEQ_CST);
	}

	release_lock(thread_index + 1);
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
