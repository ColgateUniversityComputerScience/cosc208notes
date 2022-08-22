# Exam 3 Review
_COSC 208, Introduction to Computer Systems, 2021-11-17_

## Announcements
* Exam 3
    * Study guide posted on Moodle
    * In-class portion: during class Friday
    * Take-home portion: due at 11pm on Monday
* Project 3 due Thursday, December 2

## Outline
* Memory hierarchy
* Caching
* Processes
* Scheduling
* Threads

## Memory hierarchy
Q1: What is the **fastest volatile** memory?
```

```

Q2: What is the **fastest non-volatile** memory?
```


```

Q3: Why is a hard disk drive (HDD) slower than a solid state drive (SSD)?
```


```

Q4: Why is accessing main memory (i.e., Random Access Memory (RAM)) slower than accessing a cache?
```


```

Q5: Why do solid state drives (SSDs) cost less per unit of capacity than main memory (i.e., Random Access Memory (RAM))?
```


```

## Caching
Q6: _Assume the cache size is 3 and the **optimal** cache replacement algorithm is used. Indicate what happens with the cache on each data access._
* Access 2
* Access 4
* Access 1
* Access 2
* Access 4
* Access 3
* Access 2
* Access 4
* Access 1
* Access 2
* Access 4
* Access 1

Q7: _Assume the cache size is 3 and the **least recently used (LRU)** cache replacement algorithm is used. Indicate what happens with the cache on each data access._
* Access 2
* Access 4
* Access 1
* Access 2
* Access 4
* Access 3
* Access 2
* Access 4
* Access 1
* Access 2
* Access 4
* Access 1

## Processes
Q8: _Write a program that creates a new process. The child process should print "I am a child"; the parent process should print "I am a parent; my child is CPID" (replacing CPID with the child’s PID)._
```C
















```

Q9: _Will the output produced by your program always appear in a particular order? Why or why not?_
```



```

## Scheduling
_Consider the following set of processes:_

| Process | Duration | Arrival Time |
|---------|----------|--------------|
| A       | 20       | 0            |
| B       | 15       | 0            |
| C       | 25       | 5            |
| D       | 5        | 10           |

```
```
Q10: _Draw the schedule when a First In First Out (FIFO) scheduling algorithm is used._
```




```

Q11: _Compute the turnaround and wait time for each process based on the above schedule._

| Process | Turnaround | Wait |
|---------|------------|------|
| A       |            |      |
| B       |            |      |
| C       |            |      |
| D       |            |      |

```
```
Q12: _Draw the schedule when a Shortest Job First (SJF) scheduling algorithm is used._
```





```

Q13: _Compute the turnaround and wait time for each process based on the above schedule._

| Process | Turnaround | Wait |
|---------|------------|------|
| A       |            |      |
| B       |            |      |
| C       |            |      |
| D       |            |      |

```
```
Q14: _Draw the schedule when a Shortest Time to Completion First (STCF) scheduling algorithm is used._
```






```

Q15: _Compute the turnaround and wait time for each process based on the above schedule._

| Process | Turnaround | Wait |
|---------|------------|------|
| A       |            |      |
| B       |            |      |
| C       |            |      |
| D       |            |      |

```
```
Q16: _Draw the schedule when a Round Round (RR) scheduling algorithm is used with a time quantum of 10._
```






```

Q17: _Compute the turnaround and wait time for each process based on the above schedule._

| Process | Turnaround | Wait |
|---------|------------|------|
| A       |            |      |
| B       |            |      |
| C       |            |      |
| D       |            |      |

<div style="page-break-after:always;"></div>

## Threads
_A program contains the following functions:_
```C
void *dec(void *arg) {
    int *t = (int *)arg;
    *t--;
    return NULL:
}

void *inc(void *arg) {
    int *t = (int *)arg;
    *t++;
    return NULL;
}

void *zero(void *arg) {
    int *t = (int *)arg;
    *t = 0;
    return NULL;
}
```
_For each of the following main methods, list **all possible outputs** the program could produce. Assume threads are only preempted if they become blocked waiting for other threads._

Q18:
```C
int main() {
    int *total = malloc(sizeof(int));
    *total = 2;
    pthread_t thrA, thrB;
    pthread_create(&thrA, NULL, &inc, total);
    pthread_create(&thrB, NULL, &inc, total);
    pthread_join(&thrA);
    pthread_join(&thrB);
    printf("%d\n", *total);
}
```

Q19:
```C
int main() {
    int *total = malloc(sizeof(int));
    *total = 2;
    pthread_t thrA, thrB;
    pthread_create(&thrA, NULL, &dec, total);
    pthread_create(&thrB, NULL, &zero, total);
    pthread_join(&thrA);
    pthread_join(&thrB);
    printf("%d\n", *total);
} 
```

Q20:
```C
int main() {
    int *total = malloc(sizeof(int));
    *total = 2;
    pthread_t thrA, thrB;
    pthread_create(&thrA, NULL, &zero, total);
    pthread_join(&thrA);
    pthread_create(&thrB, NULL, &inc, total);
    pthread_join(&thrB);
    printf("%d\n", *total);
} 
```