# Multiprocessing: making programs multi-threaded (continued)
_COSC 208, Introduction to Computer Systems, 2022-04-29_

## Announcements
* Project 4 due Thursday @ 11pm

## No warm-up — Happy Friday!

## Practice writing multi-threaded programs (continued)
```C
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

#define ARRAY_LEN 10
#define NUM_ARRAYS 5

void *sum_array(void *args) {
    int *nums = (int *)args;
    int *sum = malloc(sizeof(int));
    *sum = 0;
    for (int i = 0; i < ARRAY_LEN; i++) {
        *sum += nums[i];
    }
    return sum;
}

int sum_matrix(int *matrix[]) {
    pthread_t threads[NUM_ARRAYS];
    for (int i = 0; i < NUM_ARRAYS; i++) {
        pthread_create(&(threads[i]), NULL, &sum_array, matrix[i]);
    }

    int total = 0;
    for (int i = 0; i < NUM_ARRAYS; i++) {
        int *sum;
        pthread_join(threads[i], (void **)(&sum));
        total += *sum;
        free(sum);
    }
    
    return total;
}

int main() {
    int *matrix[NUM_ARRAYS];
    for (int i = 0; i < NUM_ARRAYS; i++) {
        matrix[i] = malloc(sizeof(int) * ARRAY_LEN);
        for (int j = 0; j < ARRAY_LEN; j++) {
            matrix[i][j] = i * 100 + j;
        }
    }

    int sum = sum_matrix(matrix);
    printf("%d\n", sum);
}
```

<div style="page-break-after:always;"></div>

## Transforming programs to be multi-threaded
_Assume you are given the following code:_
```C
#include <ctype.h>
#include <stdio.h>
#include <string.h>
int count(char *str, char ch) {
    int num = 0;
    while (*str != '\0') {
        if (tolower(*str) == ch) {
            num++;
        }
        str++;
    }
    return num;
}
int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Error: provide a string\n");
        return 1;
    }
    char *str = argv[1];
    char *vowels = "aeiou";
    int counts[strlen(vowels)];
    for (int i = 0; i < strlen(vowels); i++) {
        counts[i] = count(str, vowels[i]);
    }

    for (int i = 0; i < strlen(vowels); i++) {
        printf("%c %d\n", vowels[i], counts[i]);
    }
}
```

<div style="page-break-after:always;"></div>

Q1: *Write a function called  `count_wrapper` that has the signature required for a thread function and calls the `count` function. (Hint: you'll need to declare a `struct` that contains all of the parameters required for `count`.)*
```















```


Q2: *Re-write `main` to create/wait for threads that execute `count_wrapper` (instead of calling `count` sequentially).*
```
int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Error: provide a string\n");
        return 1;
    }
    char *str = argv[1];
    char *vowels = "aeiou";
```