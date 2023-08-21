# Efficiency: caching
_COSC 208, Introduction to Computer Systems, 2022-11-02_

## Announcements
* No open lab hours on Tuesdays for the rest of the semester
* Project 4 due Thurs, Nov 10
* DEI Assignment 3 due Tues, Nov 15

## Outline
* Warm-up
* Instances of caching
* Cache replacement

## Warm-up
Q1: _Cross-out unnecessary loads and stores in the following assembly code._
```
0000000000400584 <pow2>:
    400584:       d10043ff        sub     sp, sp, #0x10
    400588:       b9000fe0        str     w0, [sp, #12]
    40058c:       52800028        mov     w8, #0x1
    400590:       b9000be8        str     w8, [sp, #8]
    400594:       b9400fe8        ldr     w0, [sp, #12]
    400598:       7100011f        cmp     w0, #0x0
    40059c:       37000128        b.le    4005c0 <pow2+0x3c>
    4005a0:       b9400be8        ldr     w8, [sp, #8]
    4005a4:       52800049        mov     w9, #0x2
    4005a8:       1b097d08        mul     w8, w8, w9
    4005ac:       b9000be8        str     w8, [sp, #8]
    4005b0:       b9400fe8        ldr     w0, [sp, #12]
    4005b4:       71000508        subs    w0, w0, #0x1
    4005b8:       b9000fe8        str     w0, [sp, #12]
    4005bc:       17fffff5        b       400594 <pow2+0x10>
    4005c0:       b9400be0        ldr     w0, [sp, #8]
    4005c4:       910043ff        add     sp, sp, #0x10
    4005c8:       d65f03c0        ret
```

Q2: _Where are caches used in computer systems?_