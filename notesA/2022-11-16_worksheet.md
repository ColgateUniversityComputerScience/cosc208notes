# Exam 3 Review
_COSC 208, Introduction to Computer Systems, 2022-11-16_

## Announcements
* Exam 3
    * Study guide posted on Moodle
    * Take-home portion: due Friday before class
    * In-class portion: Friday during **either class period (8:20am or 10:20am)**
* DEI Assignment 3 due Monday, Nov 29 @ 11pm

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

## Reducing memory accesses
Q5: _Cross-out unnecessary loads and stores for the following assembly code:_
```
000000000000076c <divide>:                      
    76c:    d10083ff     sub    sp, sp, #0x20
    770:    b9000fe0     str    w0, [sp, #12]
    774:    b9000be1     str    w1, [sp, #8]
    778:    12800000     mov    w0, #0xffffffff
    77c:    b9001fe0     str    w0, [sp, #28]
    780:    b9400fe1     ldr    w1, [sp, #8]
    784:    b9400be0     ldr    w0, [sp, #12]
    788:    1ac00c20     sdiv   w0, w1, w0
    78c:    b9001fe0     str    w0, [sp, #28]
    790:    b9401fe0     ldr    w0, [sp, #28]
    794:    910083ff     add    sp, sp, #0x20
    798:    d65f03c0     ret
```

<div style="page-break-after:always;"></div>

Q6: _Cross-out unnecessary loads and stores for the following assembly code:_
```
000000000000071c <flip>:
    71c:    d10083ff     sub    sp, sp, #0x20
    720:    b9000fe0     str    w0, [sp, #12]
    724:    12800000     mov    w1, #0xffffffff
    728:    b9001fe0     str    w1, [sp, #28]
    72c:    b9400fe0     ldr    w0, [sp, #12]
    730:    7100001f     cmp    w0, #0x0
    734:    54000081     b.eq   740 <flip+0x28>
    738:    b9001fff     str    wzr, [sp, #28]
    73c:    14000002     b      748 <flip+0x2c>
    740:    52800020     mov    w0, #0x1
    744:    b9001fe0     str    w0, [sp, #28]
    748:    b9401fe0     ldr    w0, [sp, #28]
    74c:    910083ff     add    sp, sp, #0x20
    750:    d65f03c0     ret    
```


## Locality
Q7: _For each of the following scenarios, indicate whether it is an example of temporal locality, spatial locality, or neither._
* Gates for flights on the same airline are located in the same airport terminal/concourse
    ```

    ```
* A grocery list is arranged in alphabetical order – neither
    ```

    ```
* Clothes in a closet are grouped into outfits, with a sweater, a shirt, and a pair of pants stored next to each other – spatial locality
    ```

    ```
* Boxes of cereal, bowls, and spoons are stored in adjacent kitchen cabinets/drawers – spatial locality
    ```

    ```
* You repeatedly check your phone for new messages
    ```

    ```
* A variable used in a for loop
    ```

    ```
* Variables used in different functions
    ```

    ```
* A function's parameters, which are each used once within the function
    ```

    ```

<div style="page-break-after:always;"></div>

## Caching
Q8: _Assume the cache size is 3 and the **optimal** cache replacement algorithm is used. Indicate what happens with the cache on each data access._
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

Q9: _Assume the cache size is 3 and the **least recently used (LRU)** cache replacement algorithm is used. Indicate what happens with the cache on each data access._
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

## Loop optimization
Q10: _Modify the following code to perform all relevant loop optimizations. You should assume the length of the key is **significantly smaller** than the length of the plain string, such that the entire key will fit in the cache but the entire plain string will not fit in the cache._
```C
char *vigenere(char *plain, char *key, int keylen) {
    char *cipher = malloc(sizeof(char) * (strlen(plain) + 1));
    cipher[strlen(plain)] = '\0';
    int j = 0;
    while (j < keylen) {
        int i = j;
        while (i < strlen(plain)) {
            cipher[i] = (((plain[i] - 'A') + key[j]) % 26) + 'A';
            i += keylen;
        }
        j++;
    }
    return cipher;
}
```

<div style="page-break-after:always;"></div>

## Processes
Q11: _Write a program that creates a new process. The child process should print "I am a child"; the parent process should print "I am a parent; my child is CPID" (replacing CPID with the child’s PID)._
```C
















```

Q12: _Will the output produced by your program always appear in a particular order? Why or why not?_
```




```

Q13: _Write a program that creates two new processes. The first process should run the executable `/usr/bin/whoami`. The second process should print `I have a sibling` after the first process has finished._
```C
















```

<div style="page-break-after:always;"></div>

Q14: _What are all possible outputs the following program may produce?_
```C
int main() {
    printf("A\n");
    int retval = fork();
    printf("B\n");
    if (retval == 0) {
        printf("C\n");
    }
    else {
        printf("D\n");
    }
}
```
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
Q15: _Draw the schedule when a First In First Out (FIFO) scheduling algorithm is used._
```




```

Q16: _Compute the turnaround and wait time for each process based on the above schedule._

| Process | Turnaround | Wait |
|---------|------------|------|
| A       |            |      |
| B       |            |      |
| C       |            |      |
| D       |            |      |

```
```

<div style="page-break-after:always;"></div>

Q17: _Draw the schedule when a Shortest Job First (SJF) scheduling algorithm is used._
```





```

Q18: _Compute the turnaround and wait time for each process based on the above schedule._

| Process | Turnaround | Wait |
|---------|------------|------|
| A       |            |      |
| B       |            |      |
| C       |            |      |
| D       |            |      |

```
```
Q19: _Draw the schedule when a Shortest Time to Completion First (STCF) scheduling algorithm is used._
```






```

Q20: _Compute the turnaround and wait time for each process based on the above schedule._

| Process | Turnaround | Wait |
|---------|------------|------|
| A       |            |      |
| B       |            |      |
| C       |            |      |
| D       |            |      |

```
```

Q21: _Draw the schedule when a Round Round (RR) scheduling algorithm is used with a time quantum of 10._
```






```

Q22: _Compute the turnaround and wait time for each process based on the above schedule._

| Process | Turnaround | Wait |
|---------|------------|------|
| A       |            |      |
| B       |            |      |
| C       |            |      |
| D       |            |      |