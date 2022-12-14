# Multiprocessing: making programs multi-threaded
_COSC 208, Introduction to Computer Systems, 2022-04-27_

# Announcements
* Attend faculty candidate talks Dec 1, 8, 13, 14, & 15 at 11:20am
    * Earn 2 points of extra credit on final exam for each talk or discussion attended (maximum of 4 points)
* Project 5 due Thurs, Dec 8 @ 11pm 

## Outline
* Warm-up
* Creating multiple threads
* Returning values from threads
* Practice writing multi-threaded programs
* Passing multiple parameters to threads
* Transforming programs to be multi-threaded

## Warm-up
Q1: _What are all possible outputs produced by this program?_
```C
1   #include <pthread.h>
2   void *increment(void *arg) {
3       int *num = (char*)arg;
4       *num++;
5       return NULL;
6   }
7    void *zero(void *arg) {
8       int *num = (char*)arg;
9       *num = 0;
10      return NULL;
11   }
12   int main() {
13      pthread_t thread1, thread2;
14      int *i = malloc(sizeof(int));
15      *i = 5;
16      pthread_create(&thread1, NULL, &increment, i);
17      pthread_create(&thread2, NULL, &zero, i);
18      pthread_join(thread1, NULL);
19      pthread_join(thread2, NULL);
20      printf("i=%d\n", *i);
21  }
```
```










```

🛑 **STOP HERE** after completing the warm-up; if you have extra time please **skip ahead** to the extra practice.

<div style="page-break-after: always;"></div>

## Creating multiple threads example
```C
1   #include <pthread.h>
2   #include <stdio.h>
3   #include <stdlib.h>
4   #define NUM_THREADS 5
5   void *simple(void *arg) {
6       int *id = (int *)arg;
7       printf("I am thread %d\n", *id);
8       return NULL;
9   }
10  int main() {
11      pthread_t threads[NUM_THREADS];
12      int ids[NUM_THREADS];
13      for (int i = 0; i < NUM_THREADS; i++) {
14          ids[i] = i+1;
15          pthread_create(&(threads[i]), NULL, &simple, &(ids[i]));
16      } 
17      for (int i = 0; i < NUM_THREADS; i++) {
18          pthread_join(threads[i], NULL);
19      }
20      printf("All threads finished\n");
21  }
```

## Returning values from threads example
```C
1   #include <stdio.h>
2   #include <stdlib.h>
3   #include <string.h>
4   #include <pthread.h>
5   void *length(void *arg) {
6       char *str = (char *)arg;
7       int *len = malloc(sizeof(int));
8       *len = strlen(str);
9       return len;
10  }
11  int main() {
12      pthread_t thread;
13      char *phrase = "Hello, threads!";
14      pthread_create(&thread, NULL, &length, phrase);
15      int *result = NULL;
16      pthread_join(thread, (void **)&result);
17      printf("Length: %d\n", *result);
18      free(result);
19  }
```

<div style="page-break-after: always;"></div>

## Practice writing multi-threaded programs
Q2: _Write a function called `sum_array` which takes an array of `ARRAY_LEN` integers and returns the sum of the integers. Your function should have the appropriate prototype/implementation to serve as the entry point for a thread. Assume `ARRAY_LEN` is a constant which has been `#define`d._
```


















```

Q3: _Write a function called `sum_matrix` which takes an array of `NUM_ARRAYS` arrays of integers (i.e., an `int **`) and returns the sum of all the integers. The function should create `NUM_ARRAYS` threads, each running the `sum_array` function for a single array of integers. Assume `NUM_ARRAYS` is a constant which has been `#define`d._
```






















```

🛑 **STOP HERE** after completing the above questions; if you have extra time please **skip ahead** to the extra practice.

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

Q4: *Write a function called  `count_wrapper` that has the signature required for a thread function and calls the `count` function. (Hint: you'll need to declare a `struct` that contains all of the parameters required for `count`.)*

<div style="page-break-after:always;"></div>

Q5: *Re-write `main` to create/wait for threads that execute `count_wrapper` (instead of calling `count` sequentially).*
```C
int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Error: provide a string\n");
        return 1;
    }
    char *str = argv[1];
    char *vowels = "aeiou";
```

<div style="page-break-after:always;"></div>

## Extra practice
Q6: _What are all possible outputs produced by this program?_
```C
1   #include <pthread.h>
2   void *printer(void *arg) {
3       char *ch = (char*)arg;
4       printf("I am %c\n", *ch);
5       return NULL;
6   }
7   int main() {
8       pthread_t thread1, thread2;
9       char *ch = malloc(sizeof(char));
10      *ch = 'A';
11      pthread_create(&thread1, NULL, &printer, ch);
12      *ch = 'B';
13      pthread_create(&thread2, NULL, &printer, ch);
14      pthread_join(thread1, NULL);
15      pthread_join(thread2, NULL);
16  }
```