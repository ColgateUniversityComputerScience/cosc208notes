# Networking: cloud computing; review
_COSC 208, Introduction to Computer Systems, 2021-12-10_

## Announcements
* Office hours
    * Today 10:15am-11:45am
    * Monday 12pm-4pm
    * Wednesday 8:30am-10:30am
    * Thursday 9:30am-11:30am
* Final exam
    * Study guide posted on Moodle
    * Take-home portion due Friday at 9am
    * In-class portion Friday 9am-11am

## Outline
* Warm-up
* Virtual machines
* Characteristics of cloud computing
* Cloud service models
* Review

## Warm-up
_Below is a simplified picture of Aaron’s home._

<img src="../images/wireless/home.png" style="width:375px;" />

_Aaron’s wireless smart television with built-in video streaming does not work well: videos pause frequently to buffer, and videos have low resolution._

Q1: _What are two potential causes of this problem?_
```





```

Q2: _What can Aaron change to address each of these problems?_
```





```
🛑 **STOP HERE** after completing the warm-up; please **DO NOT WORK AHEAD**.

<div style="page-break-after:always;"></div>

## Cloud service models
Q3: _For each of the following service providers, indicate what type of service they offer._
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


## Review: memory
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

<div style="page-break-after:always;"></div>

For each of the following errors produced by valgrind, describe (in 2-3 sentences) **why** the error is occurring and **how** you would modify the code to correct the error.

Q4:
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

Q5:
```
Invalid read of size 1
    at 0x4006BF: repeat (repeat.c:9)
    by 0x400752: main (repeat.c:19)
Address 0x5204044 is 0 bytes after a block of size 4 alloc'd
    at 0x4C2DB8F: malloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
    by 0x400723: main (repeat.c:17)
```
```



```

Q6:
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

Q7:
```
4 bytes in 1 blocks are definitely lost in loss record 1 of 1
    at 0x4C2DB8F: malloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
    by 0x400723: main (repeat.c:17)
```
```



```

<div style="page-break-after:always;"></div>

## Review: threads
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

Q8:
```C
int main() {
    int *total = malloc(sizeof(int));
    *total = 3;
    pthread_t thrA, thrB;
    pthread_create(&thrA, NULL, &dbl, total);
    pthread_create(&thrB, NULL, &one, total);
    pthread_join(&thrA);
    pthread_join(&thrB);
    printf("%d\n", total);
}
```

Q9:
```C
int main() {
    int *total = malloc(sizeof(int));
    *total = 3
    pthread_t thrA, thrB;
    pthread_create(&thrA, NULL, &one, total);
    pthread_join(&thrA);
    pthread_create(&thrB, NULL, &dbl, total);
    pthread_join(&thrB);
    printf("%d\n", total);
}
```

## Review: sockets
Q10: _What sequence of socket functions should a server application call?_
