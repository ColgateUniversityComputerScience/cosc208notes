# Efficiency: memory hierarchy
_COSC 208, Introduction to Computer Systems, 2022-03-30_

## Announcements
* Project 2 due tomorrow at 11pm

## Warm-up
Q1: _The following C code was compiled into assembly (using `clang`). For each line of assembly, indicate which original line of C code the assembly instruction was derived from._
```C
1   int sum(int a, int b) {
2       int c = a + b;
3       return c;
4   }
5   int triple(int u, int v) {
6       int r = 3;
7       int s = sum(u, v);
8       int t = s * r;
9       return t;
10   }
11  int main() {
12      int x = 2;
13      int y = 3;
14      int z = triple(x, y);
15      return z;
16  }
```
```
0000000000400544 <sum>:
    400544:    d10043ff     sub    sp, sp, #0x10   // 
    400548:    b9000fe0     str    w0, [sp, #12]   // 
    40054c:    b9000be1     str    w1, [sp, #8]    // 
    400550:    b9400fe8     ldr    w8, [sp, #12]   // 
    400554:    b9400be9     ldr    w9, [sp, #8]    // 
    400558:    0b090108     add    w8, w8, w9      // 
    40055c:    b90007e8     str    w8, [sp, #4]    // 
    400560:    b94007e0     ldr    w0, [sp, #4]    // 
    400564:    910043ff     add    sp, sp, #0x10   // 
    400568:    d65f03c0     ret                    // 
000000000040056c <triple>:
    40056c:    d100c3ff     sub    sp, sp, #0x30   // 
    400570:    f90013fe     str    x30, [sp, #32]  // 
    400574:    b9001fe0     str    w0, [sp, #28]   // 
    400578:    b9001be1     str    w1, [sp, #24]   // 
    40057c:    52800068     mov    w8, #0x3        // 
    400580:    b90017e8     str    w8, [sp, #20]   // 
    400584:    b9401fe0     ldr    w0, [sp, #28]   // 
    400588:    b9401be1     ldr    w1, [sp, #24]   // 
    40058c:    97ffffee     bl     400544 <sum>    //  
    400590:    b90013e0     str    w0, [sp, #16]   // 
    400594:    b94013e8     ldr    w8, [sp, #16]   // 
    400598:    b94017e9     ldr    w9, [sp, #20]   // 
    40059c:    1b097d08     mul    w8, w8, w9      // 
    4005a0:    b9000fe8     str    w8, [sp, #12]   // 
    4005a4:    b9400fe0     ldr    w0, [sp, #12]   // 
    4005a8:    f94013fe     ldr    x30, [sp, #32]  // 
    4005ac:    9100c3ff     add    sp, sp, #0x30   // 
    4005b0:    d65f03c0     ret                    // 
```

<div style="page-break-after:always;"></div>

```
```

<div style="page-break-after:always;"></div>

```
00000000004005b4 <main>:
    4005b4:    d10083ff     sub    sp, sp, #0x20   // 
    4005b8:    f9000bfe     str    x30, [sp, #16]  // 
    4005bc:    52800048     mov    w8, #0x2        // 
    4005c0:    b9000be8     str    w8, [sp, #8]    // 
    4005c4:    52800069     mov    w9, #0x3        // 
    4005c8:    b90007e9     str    w9, [sp, #4]    // 
    4005cc:    b9400be0     ldr    w0, [sp, #8]    // 
    4005d0:    b94007e1     ldr    w1, [sp, #4]    // 
    4005d4:    97ffffe5     bl     40056c <triple> //  
    4005d8:    b90003e0     str    w0, [sp]        // 
    4005dc:    b94003e0     ldr    w0, [sp]        // 
    4005e0:    f9400bfe     ldr    x30, [sp, #16]  // 
    4005e4:    910083ff     add    sp, sp, #0x20   // 
    4005e8:    d65f03c0     ret                    // 
```

Q2: _Draw the contents of the stack and registers just prior to the execution of the second-to-last assembly instruction in `sum`. Assume the registers have the following initial values:_
* `pc` = `0x4005b4` 
* `sp` = `0xF80`
* `x30` = `0x400488`

```






















```

🛑 **STOP HERE** after completing the warm-up; if you have extra time, take a few deep breaths to reduce stress.

<div style="page-break-after:always;"></div>

## Optimizing assembly code for locality
* Q3: _Cross-out redundant loads and stores from the assembly code_
    ```
    000000000000088c <interest_due>:
        88c:    sub    sp, sp, #0x20
        890:    str    w0, [sp, #12] 
        894:    str    w1, [sp, #8]
        898:    ldr    w0, [sp, #12]
        89c:    ldr    w1, [sp, #8]
        8a0:    mul    w0, w1, w0
        8a4:    str    w0, [sp, #20]
        8a8:    mov    w0, #0x4b
        8ac:    str    w0, [sp, #24] 
        8b0:    ldr    w1, [sp, #20
        8b4:    ldr    w0, [sp, #24]  
        8b8:    sdiv   w0, w1, w0
        8bc:    str    w0, [sp, #28]
        8c0:    ldr    w0, [sp, #28] 
        8c4:    add    sp, sp, #0x2
        8c8:    ret
    ```
