# Multiprocessing: threads
_COSC 208, Introduction to Computer Systems, 2022-04-22_

## Announcements
* Project 4 due Thursday, May 5

## Warm-up
_Consider the following processes:_

| Process | Arrival time   | Duration | 
|---------|----------------|----------|
| A       | 0              | 30       |
| B       | 10             | 40       |
| C       | 10             | 15       |
| D       | 20             | 10       |

Q1: _Draw the schedule for the above processes using a First In First Out (FIFO) scheduling algorithm._
```





```

Q2: _Calculate the turnaround time for each process._
```





```

Q3: _Draw the schedule for the above processes using a Shortest Job First (SJF) scheduling algorithm._
```






```

Q4: _Calculate the turnaround time for each process._
```





```

<div style="page-break-after:always;"></div>

| Process | Arrival time   | Duration | 
|---------|----------------|----------|
| A       | 0              | 30       |
| B       | 10             | 40       |
| C       | 10             | 15       |
| D       | 20             | 10       |

Q5: _Draw the schedule for the above processes using a Shortest Time to Completion First (STCF) scheduling algorithm._
```





```

Q6: _Calculate the turnaround time and wait time for each process._
```











```

Q7: _Draw the schedule for the above processes using a Round Robin (RR) scheduling algorithm with a quantum of 10._
```





```

Q8: _Calculate the turnaround time and wait time for each process._
```











```

🛑 **STOP HERE** after completing the warm-up; if you have extra time, **skip ahead** to the extra practice.

<div style="page-break-after:always;"></div>

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

### Practice 
Q9: _What are all possible outputs produced by this program?_
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

<div style="page-break-after:always;"></div>

Q10: _What are all possible outputs produced by this program?_
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

## Extra practice
Q11: _What are all possible outputs produced by this program?_
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