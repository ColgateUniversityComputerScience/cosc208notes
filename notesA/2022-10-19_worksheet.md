# Assembly: conditionals
_COSC 208, Introduction to Computer Systems, 2022-10-19_

## Announcements
* Programming project 3 due tomorrow @ 11pm
* No lab this week

## Warm-up
Q1: _The following C code was compiled into assembly (using `gcc`)._
```C
1  int divide(int numerator, int denominator) {
2      int result = -1;
3      result = numerator / denominator;
4      return result;
5  }
```
```
000000000000076c <divide>:                      // Line     Low-level C
    76c:    d10083ff     sub    sp, sp, #0x20   // 1        sp = sp - 0x20
    770:    b9000fe0     str    w0, [sp, #12]   // 1        *(sp+12) = w0
    774:    b9000be1     str    w1, [sp, #8]    // 1        *(sp+8) = w1
    778:    12800000     mov    w0, #0xffffffff // 2        w0 = 0xffffffff
    77c:    b9001fe0     str    w0, [sp, #28]   // 2        *(sp+28) = w0
    780:    b9400fe1     ldr    w1, [sp, #12]   // 3        w1 = *(sp+12)
    784:    b9400be0     ldr    w0, [sp, #8]    // 3        w0 = *(sp+8)
    788:    1ac00c20     sdiv   w0, w1, w0      // 3        w0 = w1/w0
    78c:    b9001fe0     str    w0, [sp, #28]   // 3        *(sp+28) = w0
    790:    b9401fe0     ldr    w0, [sp, #28]   // 4        w0 = *(sp+28)
    794:    910083ff     add    sp, sp, #0x20   // 4        sp = sp + 0x20
    798:    d65f03c0     ret                    // 4        return
```
_Draw the contents of the stack and registers after executing the assembly code. Assume the registers initially hold the following values:_
```
sp = 0xFE0
w/x0 = 100
w/x1 = 5
```
```












```

🛑 **STOP HERE** after completing the warm-up; if you have extra time please **skip ahead** to the extra practice.

<div style="page-break-after:always;"></div>

## Conditionals — example
```C
1  int divide_safe(int numerator, int denominator) {
2      int result = -1;
3      if (denominator != 0) {
4          result = numerator / denominator;
5      }
6      return result;
7  }
```
```
000000000000076c <divide_safe>:
    76c:    d10083ff     sub    sp, sp, #0x20
    770:    b9000fe0     str    w0, [sp, #12]
    774:    b9000be1     str    w1, [sp, #8]
    778:    12800000     mov    w0, #0xffffffff
    77c:    b9001fe0     str    w0, [sp, #28]
    780:    b9400be0     ldr    w0, [sp, #8]
    784:    7100001f     cmp    w0, #0x0
    788:    540000a0     b.eq   79c <divide_safe+0x30>
    78c:    b9400fe1     ldr    w1, [sp, #12]
    790:    b9400be0     ldr    w0, [sp, #8]
    794:    1ac00c20     sdiv   w0, w1, w0
    798:    b9001fe0     str    w0, [sp, #28]
    79c:    b9401fe0     ldr    w0, [sp, #28]
    7a0:    910083ff     add    sp, sp, #0x20
    7a4:    d65f03c0     ret
```

<div style="page-break-after:always;"></div>

## Practice with conditionals
Q2: _The C code below was compiled into assembly (using `gcc`). Label each line of assembly code with the line number of the line of C code from which the assembly instruction was derived._ 
```C
1  int flip(int bit) {
2     int result = -1;
3     if (bit == 0) {
4          result = 1; 
5      } 
6      else {
7          result = 0;
8      }
9      return result;
10 }
```
```
000000000000071c <flip>:                            // Line
    71c:    d10083ff     sub    sp, sp, #0x20       // 
    720:    b9000fe0     str    w0, [sp, #12]       // 
    724:    12800000     mov    w0, #0xffffffff     // 
    728:    b9001fe0     str    w0, [sp, #28]       // 
    72c:    b9400fe0     ldr    w0, [sp, #12]       // 
    730:    7100001f     cmp    w0, #0x0            //
    734:    54000081     b.ne   744 <flip+0x28>     // 
    738:    52800020     mov    w0, #0x1            // 
    73c:    b9001fe0     str    w0, [sp, #28]       // 
    740:    14000002     b      748 <flip+0x2c>     // 
    744:    b9001fff     str    wzr, [sp, #28]      // 
    748:    b9401fe0     ldr    w0, [sp, #28]       // 
    74c:    910083ff     add    sp, sp, #0x20       // 
    750:    d65f03c0     ret                        // 
```

Q3: _Write a function called `flip_goto` that behaves the same as `flip` but matches the structure of the assembly code that will be generated for `flip`. (Hint: you'll need two `goto` statements.)_

<div style="page-break-after:always;"></div>

## Extra practice
Q4: _Assume the registers currently hold the following values:_
```
sp = 0xA980
w/x0 = 0
w/x1 = 1
w/x2 = 2
w/x3 = 3
w/x4 = 4
w/x5 = 5
```
_Draw the contents of the stack after the following instructions have been executed:_
```
sub sp, sp, #0x30
str w0, [sp, #16]
str x1, [sp]
str w2, [sp, #20]
str x3, [sp, #32]
str w4, [sp, #28]
str w5, [sp, #8]
```
```












```

Q5: _Write a function called `adjust_goto` that behaves the same as `adjust` but matches the structure of the assembly code that will be generated for `adjust`. (Hint: you'll need two `goto` statements.)_
```C
int adjust(int value) {
    if (value < 10) {
        value = value * 10;
    }
    else {
        value = value / 10;
    }
    return value;
}
```