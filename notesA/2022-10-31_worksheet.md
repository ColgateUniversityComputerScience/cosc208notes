# Efficiency: memory hierarchy; locality
_COSC 208, Introduction to Computer Systems, 2022-10-31_

## Announcements
* Project 4 due Thurs, Nov 10
* DEI Assignment 3 due Tues, Nov 15
* Exam 3 in-class portion: Fri, Nov 18
* DEI Assignment 4 canceled
* Complete the National College Health Assessment (NCHA) – [https://www.colgate.edu/oia/survey/ncha](https://www.colgate.edu/oia/survey/ncha)

## Outline
* Memory hierarchy
* Better use of registers
* Temporal vs. spatial locality

## No warm-up – Happy Halloween!

## Better use of registers
Q1: _Cross-out unnecessary loads and stores for each of the following snippets of assembly code_
```
000000000000088c <interest_due>:
    88c:    sub    sp, sp, #0x20
    890:    str    w0, [sp, #12]
    894:    str    w1, [sp, #8]
    898:    ldr    w0, [sp, #12]
    89c:    ldr    w1, [sp, #8] 
    8a0:    mul    w0, w1, w0
    8a4:    str    w0, [sp, #20]
    8a8:    mov    w0, #0x4b0
    8ac:    str    w0, [sp, #24]
    8b0:    ldr    w1, [sp, #20]
    8b4:    ldr    w0, [sp, #24] 
    8b8:    sdiv   w0, w1, w0
    8bc:    str    w0, [sp, #28] 
    8c0:    ldr    w0, [sp, #28] 
    8c4:    add    sp, sp, #0x20
    8c8:    ret
```
```
0000000000400544 <sum>:
    400544:    d10043ff     sub    sp, sp, #0x10
    400548:    b9000fe0     str    w0, [sp, #12]
    40054c:    b9000be1     str    w1, [sp, #8] 
    400550:    b9400fe8     ldr    w8, [sp, #12]
    400554:    b9400be9     ldr    w9, [sp, #8] 
    400558:    0b090108     add    w8, w8, w9   
    40055c:    b90007e8     str    w8, [sp, #4] 
    400560:    b94007e0     ldr    w0, [sp, #4] 
    400564:    910043ff     add    sp, sp, #0x10
    400568:    d65f03c0     ret                 
```