# Multithreading: threads
_COSC 208, Introduction to Computer Systems, 2022-11-28_

## Announcements
* DEI Assignment 3 due today @ 11pm
* Project 5 due Thurs, Dec 8 @ 11pm 

## Outline
* Warm-up
* Threads
* Pthreads API
* Creating multiple threads

## Warm-up
Q1: _What are all possible outputs produced by this program?_
```C
void *proc1_main(void *arg) {
    int *x = (int *)arg;
    *x += 1;
    return NULL;
}
void *proc2_main(void *arg) {
    int *y = (int *)arg;
    *y += 2;
    return NULL;
}
int main() {
    int z = 0;
    int pid = fork();
    if (pid == 0) {
        proc1_main(&z);
    } else {
        proc2_main(&z);
        wait(NULL);
    }
    printf("z is %d\n", z);
}
```
```






```

🛑 **STOP HERE** after completing the warm-up; if you have extra time please **skip ahead** to the extra practice.

<div style="page-break-after: always;"></div>

## Threads
Example program
```C
void *thread1_main(void *arg) {
    int *x = (int *)arg;
    *x += 1;
    return NULL;
}
void *thread2_main(void *arg) {
    int *y = (int *)arg;
    *y += 2;
    return NULL;
}
int main() {
    int *z = malloc(sieof(int));
    *z = 0;
    // Start thread running thread1_main(z)
    // Start thread running thread2_main(z)
    // Wait for threads to finish
    printf("z is %d\n", *z);
}
```

Q2: _What are all possible outputs produced by this program?_
```C
void *thread_main(void *arg) {
    char *id = (char *)arg;
    printf("I am thread %c\n", *id);
    return NULL;
}
int main() {
    char *a = malloc(sizeof(char));
    *a = 'A';
    char *b = malloc(sizeof(char));
    *b = 'B';
    // Start thread running thread_main(a)
    // Start thread running thread_main(b)
    // Wait for threads to finish
}
```
```






```
🛑 **STOP HERE** after completing the above question; if you have extra time please **skip ahead** to the extra practice.

<div style="page-break-after: always;"></div>

## Pthreads API
Q3: _What are all possible outputs produced by this program?_
```C
1   #include <pthread.h>
2   void *printer(void *arg) {
3       char *ch = (char*)arg;
4       printf("I am %c\n", *ch);
5       return NULL;
6   }
7   int main() {
8       pthread_t thread1, thread2;
9       char *ch1 = malloc(sizeof(char));
10      *ch1 = 'X';
11      char *ch2 = malloc(sizeof(char));
12      *ch2 = 'Y';
13      pthread_create(&thread1, NULL, &printer, ch1);
14      pthread_create(&thread2, NULL, &printer, ch2);
15      pthread_join(thread1, NULL);
16      pthread_join(thread2, NULL);
17  }
```
```





```

Q4: _What are all possible outputs produced by this program?_
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
10      *ch = 'P';
11      pthread_create(&thread1, NULL, &printer, ch);
12      pthread_join(thread1, NULL);
13      *ch = 'Q';
14      pthread_create(&thread2, NULL, &printer, ch);
15      pthread_join(thread2, NULL);
16  }
```

<div style="page-break-after: always;"></div>

## Creating multiple threads
Example
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

## Extra practice
Q5: _What are all possible outputs produced by this program?_
```C
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
int main() {
    int pid = fork();
    if (pid == 0) {
        printf("Child\n");
        exit(22);
    } else {
        int status = 0;
        wait(&status);
        printf("Status %d\n", WEXITSTATUS(status));
        exit(44);
    }
}
```

<div style="page-break-after: always;"></div>

Q6: _What output is produced by the following program? (Note: there is only one possible ordering.)_
```C
1   #include <stdio.h>
2   #include <stdlib.h>
3   #include <sys/wait.h>
4   #include <unistd.h>
5   int main() {
6       printf("A\n");
7       int x = fork();
8       if (x == 0) {
9           int y = fork();
10          if (y == 0) {
11              printf("B\n");
12          }
13          else {
14              wait(NULL);
15              printf("C\n");
16          }
17      }
18      else {
19          wait(NULL);
20          printf("D\n");
21      }
22      printf("E\n");
23  }
```
  
Q7: _What are all possible outputs produced by this program?_
```C
1   #include <stdio.h>
2   #include <pthread.h>
3   void *printer2(void *arg) {
4       char *ch = (char*)arg;
5       printf("Start %c\n", *ch);
6       printf("End %c\n", *ch);
7       return NULL;
8   }
9   int main() {
10      pthread_t thread1, thread2;
11      char *ch1 = malloc(sizeof(char));
12      *ch1 = 'X';
13      char *ch2 = malloc(sizeof(char));
14      *ch2 = 'Y';
15      pthread_create(&thread1, NULL, &printer2, ch1);
16      pthread_create(&thread2, NULL, &printer2, ch2);
17      pthread_join(thread1, NULL);
18      pthread_join(thread2, NULL);
19  }
```