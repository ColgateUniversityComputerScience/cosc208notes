# Assembly: Tracing assembly code
_COSC 208, Introduction to Computer Systems, 2022-10-17_

## Announcements
* Programming project 3 due Thursday @ 11pm
* No lab this week
* Exam 2
      * Take-home portion: released Wed, Oct 26; due Fri, Oct 28
      * In-class portion: Fri, Oct 28

## Warm-up
Q1: _The following C code was compiled into assembly (using `clang`)._
```C
1  int sum(int a, int *b) {
2     int c = *b;
3     int d = a + c;
4     return d;
5  }
```
_For each line of assembly: (1) indicate which original line of C code (above) the assembly instruction was derived from; and (2) write the low-level C code equivalent of the assembly instruction, treating registers as if they were variable names._
```
0000000000400584 <sum>:                            // Line     Low-level C
    400584:    d10083ff     sub    sp, sp, #0x20   // 
    400588:    b9001fe0     str    w0, [sp, #28]   // 
    40058c:    f9000be1     str    x1, [sp, #16]   // 
    400590:    f9400be8     ldr    x8, [sp, #16]   // 
    400594:    b9400109     ldr    w9, [x8]        // 
    400598:    b9000fe9     str    w9, [sp, #12]   // 
    40059c:    b9401fe9     ldr    w9, [sp, #28]   // 
    4005a0:    b9400fea     ldr    w10, [sp, #12]  // 
    4005a4:    0b0a0129     add    w9, w9, w10     // 
    4005a8:    b9000be9     str    w9, [sp, #8]    // 
    4005ac:    b9400be0     ldr    w0, [sp, #8]    // 
    4005b0:    910083ff     add    sp, sp, #0x20   // 
    4005b4:    d65f03c0     ret                    // 
```

🛑 **STOP HERE** after completing the warm-up; if you have extra time please **skip ahead** to the extra practice.

<div style="page-break-after:always"></div>

## Tracing assembly code example
```
sp = 0xFB0
w/x0 = 2
w/x1 = 0xFC8
```
```
















sp -> +--+--+--+--+--+--+--+--+
0xFB0 |                       |
      +--+--+--+--+--+--+--+--+
0xFB8 |                       |
      +--+--+--+--+--+--+--+--+
0xFC0 |         0xFC8         |
      +--+--+--+--+--+--+--+--+
0xFC8 |     3     |     2     |
      +--+--+--+--+--+--+--+--+
0xFD0 |       0x400618        |
      +--+--+--+--+--+--+--+--+
0xFD8 |                       |
      +--+--+--+--+--+--+--+--+
```

<div style="page-break-after:always"></div>

## Practice tracing assembly code
Q2: _Assume the following assembly code was generated (using `gcc`) for a C function with the prototype `int seasons_of_love()`:_
```
00000000000007ac <seasons_of_love>:
    7ac:   d10083ff        sub     sp, sp, #0x20
    7b0:   52802da0        mov     w0, #0x16d   // 365
    7b4:   b9000fe0        str     w0, [sp, #12]
    7b8:   52800300        mov     w0, #0x18    // 24
    7bc:   b90013e0        str     w0, [sp, #16]
    7c0:   52800780        mov     w0, #0x3c    // 60
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
_Draw the contents of the stack and registers just prior to the execution of the second-to-last instruction (`add sp, sp, #0x20`). Assume the initial value in the `sp` register is `0x7FE0`._
```

























```
🛑 **STOP HERE** after completing the above question; if you have extra time please **skip ahead** to the extra practice.

<div style="page-break-after:always"></div>

## Practice mapping, translating, and tracing assembly code
Q3: _The following C code was compiled into assembly (using `gcc`)._
```C
1  int divide(int numerator, int denominator) {
2      int result = -1;
3      result = numerator / denominator;
4      return result;
5  }
```
_For each line of assembly: (1) indicate which original line of C code (above) the assembly instruction was derived from; and (2) write the low-level C code equivalent of the assembly instruction, treating registers as if they were variable names._
```
000000000000076c <divide>:                      // Line     Low-level C
    76c:    d10083ff     sub    sp, sp, #0x20   // 
    770:    b9000fe0     str    w0, [sp, #12]   // 
    774:    b9000be1     str    w1, [sp, #8]    // 
    778:    12800000     mov    w0, #0xffffffff // 
    77c:    b9001fe0     str    w0, [sp, #28]   // 
    780:    b9400fe1     ldr    w1, [sp, #12]   // 
    784:    b9400be0     ldr    w0, [sp, #8]    // 
    788:    1ac00c20     sdiv   w0, w1, w0      // 
    78c:    b9001fe0     str    w0, [sp, #28]   //
    790:    b9401fe0     ldr    w0, [sp, #28]   // 
    794:    910083ff     add    sp, sp, #0x20   // 
    798:    d65f03c0     ret                    // 
```

Q4: _Assume the registers initially hold the following values:_
```
sp = 0xFE0
w/x0 = 100
w/x1 = 5
```
_Draw the contents of the stack and registers just prior to the execution of the second-to-last instruction (`add sp, sp, #0x10`) above._

<div style="page-break-after:always"></div>

## Extra practice
Q5: _Assume the following assembly code was generated (using `gcc`) for a C function with the prototype `int years_to_double(int rate)`:_
```
000000000000076c <years_to_double>:
    76c:    d10083ff     sub    sp, sp, #0x20
    770:    b9000fe0     str    w0, [sp, #12]
    774:    52800900     mov    w0, #0x48   // 72
    778:    b9001be0     str    w0, [sp, #24]
    77c:    b9401be1     ldr    w1, [sp, #24]
    780:    b9400fe0     ldr    w0, [sp, #12]
    784:    1ac00c20     sdiv   w0, w1, w0
    788:    b9001fe0     str    w0, [sp, #28]
    78c:    b9401fe0     ldr    w0, [sp, #28]
    790:    910083ff     add    sp, sp, #0x20
    794:    d65f03c0     ret
```
Assume the registers initially hold the following values:_
```
sp = 0x780
w/x0 = 9
```
_Draw the contents of the stack and registers just prior to the execution of the second-to-last instruction (`add sp, sp, #0x10`) above._