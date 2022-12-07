# Exam 3 (Final) Review
_COSC 208, Introduction to Computer Systems, 2022-05-06_

## Announcements
* Final exam
    * Study guide posted on Moodle
    * Take-home portion due Friday, May 13 at 9am
    * In-class portion Friday May 13 9am-11am
* Finals week office hours
    * Monday 8:30am-2pm
    * Tuesday 8:30am-10am
    * Thursday 8:30am-12pm

## No warm-up — Happy last day of the semester!

## Cloud service models
Q1: _For each of the following service providers, indicate what type of service they offer._
* _Box provides secure file sharing and storage_
    ```

    ```
* _Microsoft Azure provides virtual machines running Windows or Linux_
    ```

    ```
* _Heroku allows tenants to deploy code written in Ruby, Java, PHP, Python, Go, Scala, or Clojure_
    ```

    ```
* _Oracle Supply Chain Management (SCM) is software that allows businesses to manage their supply chain_
    ```

    ```

## Memory hierarchy
Q2: What is the **fastest volatile** memory?
```

```

Q3: What is the **fastest non-volatile** memory?
```


```

Q4: Why is a hard disk drive (HDD) slower than a solid state drive (SSD)?
```


```

Q5: Why is accessing main memory (i.e., Random Access Memory (RAM)) slower than accessing a cache?
```


```

<div style="page-break-after:always;"></div>

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

<div style="page-break-after:always;"></div>

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

<div style="page-break-after:always;"></div>

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

<div style="page-break-after:always;"></div>

_For each of the following main methods, list **all possible outputs** the program could produce. Assume threads are only preempted if they become blocked waiting for other threads._

Q18:
```C
int main() {
    int *total = malloc(sizeof(int));
    *total = 2;
    pthread_t thrA, thrB;
    pthread_create(&thrA, NULL, &inc, total);
    pthread_create(&thrB, NULL, &inc, total);
    pthread_join(thrA, NULL);
    pthread_join(thrB, NULL);
    printf("%d\n", *total);
}
```
```


```

Q19:
```C
int main() {
    int *total = malloc(sizeof(int));
    *total = 2;
    pthread_t thrA, thrB;
    pthread_create(&thrA, NULL, &dec, total);
    pthread_create(&thrB, NULL, &zero, total);
    pthread_join(thrA, NULL);
    pthread_join(thrB, NULL);
    printf("%d\n", *total);
} 
```
```


```

Q20:
```C
int main() {
    int *total = malloc(sizeof(int));
    *total = 2;
    pthread_t thrA, thrB;
    pthread_create(&thrA, NULL, &zero, total);
    pthread_join(thrA, NULL);
    pthread_create(&thrB, NULL, &inc, total);
    pthread_join(thrB, NULL);
    printf("%d\n", *total);
} 
```

<div style="page-break-after:always;"></div>

## Memory
The intended behavior of the program below is to output a string that contains multiple copies of a word (e.g., `"byebye"`). The code below compiles without warnings, but it contains multiple errors.
```C
1   #include <stdlib.h>
2   #include <string.h>
3   #include <stdio.h>
4   char *repeat(char *word, int count) {
5       char *dup = malloc(sizeof(*word) * count + 1);
6       int k = 0;
7       for (int i = 0; i < count; i++) {
8           for (int j = 0; j <= strlen(word) * count; j++) {
9               dup[k] = word[j];
10              k++;
11          }
12      }
13      free(dup);
14      return dup;
15  }
16  int main() {
17      char *orig = malloc(4);
18      strcpy(orig, "bye");
19      char *result = repeat(orig, 2);
20      printf("%s\n", result);
21  }
```
For each of the following errors produced by valgrind, describe (in 2-3 sentences) **why** the error is occurring and **how** you would modify the code to correct the error.

Q21:
```
Invalid write of size 1
    at 0x4006CA: repeat (repeat.c:9)
    by 0x400752: main (repeat.c:19)
Address 0x5204093 is 0 bytes after a block of size 3 alloc'd
    at 0x4C2DB8F: malloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
    by 0x40066B: repeat (repeat.c:5)
    by 0x400752: main (repeat.c:19)
```
```



```

Q22:
```
Invalid read of size 1
    at 0x4006BF: repeat (repeat.c:9)
    by 0x400752: main (repeat.c:19)
Address 0x5204044 is 0 bytes after a block of size 4 alloc'd
    at 0x4C2DB8F: malloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
    by 0x400723: main (repeat.c:17)
```

<div style="page-break-after:always;"></div>

Q23:
```
Invalid read of size 1
    at 0x4E88CD0: vfprintf (vfprintf.c:1632)
    by 0x4E8F8A8: printf (printf.c:33)
    by 0x40076B: main (repeat.c:20)
Address 0x5204090 is 0 bytes inside a block of size 3 free'd
    at 0x4C2EDEB: free (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
    by 0x4006FF: repeat (repeat.c:13)
    by 0x400752: main (repeat.c:19)
Block was alloc'd at
    at 0x4C2DB8F: malloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
    by 0x40066B: repeat (repeat.c:5)
    by 0x400752: main (repeat.c:19)
```
```



```

Q24:
```
4 bytes in 1 blocks are definitely lost in loss record 1 of 1
    at 0x4C2DB8F: malloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
    by 0x400723: main (repeat.c:17)
```
```



```

<div style="page-break-after:always;"></div>

## Threads
A program contains the following global variables and functions:
```C
void *dbl(void *arg) {
    int *t = (int *)arg;
    *t = *t * 2;
}

void *one(void *arg) {
    int *t = (int *)arg;
    *t = 1;
}
```

_For each of the following main methods, list **all possible outputs** the program could produce. Assume threads are only preempted if they become blocked waiting for other threads._

Q25:
```C
int main() {
    int *total = malloc(sizeof(int));
    *total = 3;
    pthread_t thrA, thrB;
    pthread_create(&thrA, NULL, &dbl, total);
    pthread_create(&thrB, NULL, &one, total);
    pthread_join(thrA, NULL);
    pthread_join(thrB, NULL);
    printf("%d\n", total);
}
```
```


```

Q26:
```C
int main() {
    int *total = malloc(sizeof(int));
    *total = 3
    pthread_t thrA, thrB;
    pthread_create(&thrA, NULL, &one, total);
    pthread_join(thrA, NULL);
    pthread_create(&thrB, NULL, &dbl, total);
    pthread_join(thrB, NULL);
    printf("%d\n", total);
}
```