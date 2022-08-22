# Assembly: instruction formats; mapping assembly code to C code
_COSC 208, Introduction to Computer Systems, 2022-03-09_

## Announcements
* First DEI reflection due tomorrow at 11pm 

## Outline
* Warm-up
* Assembly
* Operands
* Mapping assembly code to C code

## Warm-up
Q1: _Create a 1-bit circuit for `A <= B` using `AND`, `OR`, `NOT` gates_
```





































```
🛑 **STOP HERE** after completing the warm-up; if you have extra time take a few deep breaths to reduce stress.

<div style="page-break-after: always;"></div>

## Assembly Example
C code (`seasons.c`)
```C
1   #include <stdio.h>
2   int seasons_of_love() {
3       int dpy = 365;
4       int hpd = 24;
5       int mph = 60;
6       int h = dpy * hpd;
7       int m = h * mph;
8       return m;
9   }
10  int main() {
11      int minutes = seasons_of_love();
12      printf("%d minutes\n", minutes);
13      printf("%d moments so dear\n", minutes - 600);
14      printf("%d minutes\n", minutes);
15      printf("How do you measure? Measure a year?\n");
16  }
```

Assembly code (excerpt from `seasons.txt`)
```
00000000000007ac <seasons_of_love>:
    7ac:   d10083ff        sub     sp, sp, #0x20
    7b0:   52802da0        mov     w0, #0x16d  
    7b4:   b9000fe0        str     w0, [sp, #12]
    7b8:   52800300        mov     w0, #0x18   
    7bc:   b90013e0        str     w0, [sp, #16]
    7c0:   52800780        mov     w0, #0x3c   
    7c4:   b90017e0        str     w0, [sp, #20]
    7c8:   b9400fe1        ldr     w1, [sp, #12]
    7cc:   b94013e0        ldr     w0, [sp, #16]
    7d0:   1b007c20        mul     w0, w1, w0
    7d4:   b9001be0        str     w0, [sp, #24]
    7d8:   b9401be1        ldr     w1, [sp, #24]
    7dc:   b94017e0        ldr     w0, [sp, #20]
    7e0:   1b007c20        mul     w0, w1, w0
    7e4:   b9001fe0        str     w0, [sp, #28]
    7e8:   b9401fe0        ldr     w0, [sp, #28]
    7ec:   910083ff        add     sp, sp, #0x20
    7f0:   d65f03c0        ret
```