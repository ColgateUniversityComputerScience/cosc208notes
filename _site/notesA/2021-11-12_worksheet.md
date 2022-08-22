# Multiprocessing: threads
_COSC 208, Introduction to Computer Systems, 2021-11-12_

## Announcements
* Exam 3
    * Study guide posted on Moodle
    * In-class portion: during class next Friday
    * Take-home portion: due at 11pm on Monday, November 22
* Project 3 due Thursday, December 2

## Outline
* Warm-up
* Threads

## Warm-up
Q1: _Consider the following processes:_

| Process | Arrival time   | Duration | 
|---------|----------------|----------|
| A       | Just before 0  | 60       |
| B       | Just before 5  | 15       |
| C       | Just before 10 | 15       |

_Determine the schedule for the above processes using a Round Robin (RR) scheduler a time quantum of 10._

```







```

🛑 **STOP HERE** after completing the warm-up; if you have extra time, please **skip ahead** to the extra practice.

## Threads

### Example
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
    int *z = malloc(sizeof(int));
    *z = 0;
    // Start thread running thread1_main(z)
    // Start thread running thread2_main(z)
    // Wait for threads to finish
    printf("z is %d\n", *z);
}
```

<div style="page-break-after:always;"></div>

### Practice 
Q2: _What are all possible outputs produced by this program?_
```C
void *thread_main(void *arg) {
    char *id = (char *)arg;
    printf("I am thread %c\n", *id);
    return NULL;
}
int main() {
    char a = 'A';
    char b = 'B';
    // Start thread running thread_main(&a)
    // Start thread running thread_main(&b)
    // Wait for threads to finish
}
```

```






```

Q3: _What are all possible outputs produced by this program?_
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

<div style="page-break-after:always;"></div>

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