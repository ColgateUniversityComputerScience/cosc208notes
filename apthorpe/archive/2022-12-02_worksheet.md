# Multithreading: making programs multi-threaded (continued)
_COSC 208, Introduction to Computer Systems, 2022-12-02_

## Announcements
* Attend faculty candidate talks Dec 8, 13, 14, & 15 at 11:20am
    * Earn 2 points of extra credit on final exam for each talk or discussion attended (maximum of 4 points)
* Project 5 due Thursday @ 11pm 
* Final exam
    * Study guide posted on Moodle
    * Take-home portion: released next Wednesday; due Monday of finals week
    * In-class portion: Monday of finals week 9am-11am or 12pm-2pm

## Outline
* Warm-up
* Making programs multi-threaded (continued)

## Warm-up
Q1: _Consider the following program:_
```C
1   #include <ctype.h>
2   #include <pthread.h>
3   #include <stdio.h>
4   #include <stdlib.h>
5   #include <string.h>
6   int count_upper(char *str) {
7       int count = 0;
8       for (int i = 0; i < strlen(str); i++) {
9          if (isupper(str[i])) {
10              count++;
11          }
12      }
13      return count;
14  }
15  int main(int argc, char *argv[]) {
16      if (argc < 2) {
17          printf("Error: provide a string\n");
18          return 1;
19      }
20      char *str = argv[1];
21      pthread_t thr;
22      pthread_create(thr, NULL, &count_upper, str);
23      int count = 0;
24      pthread_join(thr, &count);
25      printf("There are %d uppercase letters\n", count);
26  }
```

(*continued on back of page*)

<div style="page-break-after:always;"></div>

_Compiling this program with `clang` results in the following warnings:_
```
buggy.c:22:20: warning: incompatible integer to pointer conversion passing 
'pthread_t' (aka 'unsigned long') to parameter of type 'pthread_t *' (aka 
'unsigned long *'); take the address with & [-Wint-conversion]
    pthread_create(thr, NULL, &count_upper, str);
                   ^~~
                   &
/usr/include/pthread.h:198:50: note: passing argument to parameter 
'__newthread' here
extern int pthread_create (pthread_t *__restrict __newthread,
                                                 ^

buggy.c:22:31: warning: incompatible function pointer types passing 
'int (*)(char *)' to parameter of type 'void *(*)(void *)' 
[-Wincompatible-function-pointer-types]
    pthread_create(thr, NULL, &count_upper, str);
                              ^~~~~~~~~~~~
/usr/include/pthread.h:200:15: note: passing argument to parameter 
'__start_routine' here
                           void *(*__start_routine) (void *),
                                   ^

buggy.c:24:23: warning: incompatible pointer types passing 
'int *' to parameter of type 'void **' [-Wincompatible-pointer-types]
    pthread_join(thr, &count);
                      ^~~~~~
/usr/include/pthread.h:215:49: note: passing argument to parameter 
'__thread_return' here
extern int pthread_join (pthread_t __th, void **__thread_return);
                                                ^
3 warnings generated.
```
_How would you change the code to fix these problems?_

```

















```


🛑 **STOP HERE** after completing the warm-up; if you have extra time take a few deep breaths to reduce stress.

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

Q2: *Write a function called  `count_wrapper` that has the signature required for a thread function and calls the `count` function. (Hint: you'll need to declare a `struct` that contains all of the parameters required for `count`.)*

<div style="page-break-after:always;"></div>

Q3: *Re-write `main` to create/wait for threads that execute `count_wrapper` (instead of calling `count` sequentially).*
```C
int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Error: provide a string\n");
        return 1;
    }
    char *str = argv[1];
    char *vowels = "aeiou";
```