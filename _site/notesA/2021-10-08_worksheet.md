# Assembly: Tracing assembly; operations
_COSC 208, Introduction to Computer Systems, 2021-10-08_

## Announcements
* Project 2 Part A due Thursday, Oct 21 

## Outline
* Warm-up
* Tracing assembly code
* Arithmetic operations

## Warm-up
Q0: _Write the C code equivalent for each line of assembly, treating registers as if they were variable names._
```
000000000000083c <deref>:
        83c:   d10083ff        sub     sp, sp, #0x20    //
        840:   f90007e0        str     x0, [sp, #8]     //
        844:   f94007e0        ldr     x0, [sp, #8]     //
        848:   f9400000        ldr     x0, [x0]         //
        84c:   f9000fe0        str     x0, [sp, #24]    //
        850:   f9400fe0        ldr     x0, [sp, #24]    //
        854:   910083ff        add     sp, sp, #0x20    //
        858:   d65f03c0        ret                      //
```

Q1: _Write the C code equivalent for each line of assembly, treating registers as if they were variable names. For example, the C code equivalent for `sub sp, sp, #0x20` is `sp = sp - 0x20`._
```
00000000000007ec <sum>:
    7ec:	d10083ff 	sub	sp, sp, #0x20   // 
    7f0:	b9000fe0 	str	w0, [sp, #12]   //
    7f4:	f90003e1 	str	x1, [sp]        // 
    7f8:	f94003e0 	ldr	x0, [sp]        // 
    7fc:	b9400000 	ldr	w0, [x0]        // 
    800:	b9001be0 	str	w0, [sp, #24]   // 
    804:	b9400fe1 	ldr	w1, [sp, #12]   // 
    808:	b9401be0 	ldr	w0, [sp, #24]   // 
    80c:	0b000020 	add	w0, w1, w0      // 
    810:	b9001fe0 	str	w0, [sp, #28]   // 
    814:	b9401fe0 	ldr	w0, [sp, #28]   // 
    818:	910083ff 	add	sp, sp, #0x20   // 
    81c:	d65f03c0 	ret	                // 
```
🛑 **STOP HERE** after completing the warm-up; if you have extra time take a few deep breaths to help reduce stress.

<div style="page-break-after: always;"></div>

## Tracing assembly code
C code
```C
1  int sum(int a, int *b) {
2     int c = *b;
3     int d = a + c;
4     return d;
5  }
```

Assembly code
```
00000000000007ec <sum>:
    7ec:	d10083ff 	sub	sp, sp, #0x20   // 
    7f0:	b9000fe0 	str	w0, [sp, #12]   // 
    7f4:	f90003e1 	str	x1, [sp]        // 
    7f8:	f94003e0 	ldr	x0, [sp]        // 
    7fc:	b9400000 	ldr	w0, [x0]        // 
    800:	b9001be0 	str	w0, [sp, #24]   // 
    804:	b9400fe1 	ldr	w1, [sp, #12]   // 
    808:	b9401be0 	ldr	w0, [sp, #24]   // 
    80c:	0b000020 	add	w0, w1, w0      // 
    810:	b9001fe0 	str	w0, [sp, #28]   // 
    814:	b9401fe0 	ldr	w0, [sp, #28]   //
    818:	910083ff 	add	sp, sp, #0x20   // 
    81c:	d65f03c0 	ret	                // 
```

<div style="page-break-after: always;"></div>

## Arithmetic operations
_Write the C code equivalent for each line of assembly, treating registers as if they were variable names._

Q2: `lsl w9, w9, w10`
```C


```

Q3: `and w9, w9, w10`
```C


```

Q4: `mul w9, w9, w10`
```C


```

Q5: `sdiv w9, w9, w10`
```C


```

## Practice tracing assembly code
Q6: _The following is the assembly code for a C function with the following prototype: `int seasons_of_love()`. Write the C code equivalent for each line of assembly, treating registers as if they were variable names._
```
0000000000400584 <seasons_of_love>:
    400584:	d10083ff 	sub	sp, sp, #0x20   //
    400588:	52802da8 	mov	w8, #0x16d      //
    40058c:	52800309 	mov	w9, #0x18       //
    400590:	5280078a 	mov	w10, #0x3c      //
    400594:	b9001fe8 	str	w8, [sp, #28]   //
    400598:	b9001be9 	str	w9, [sp, #24]   //
    40059c:	b90017ea 	str	w10, [sp, #20]  //
    4005a0:	b9401fe8 	ldr	w8, [sp, #28]   //
    4005a4:	b9401be9 	ldr	w9, [sp, #24]   //
    4005a8:	1b097d08 	mul	w8, w8, w9      //
    4005ac:	b90013e8 	str	w8, [sp, #16]   //
    4005b0:	b94013e8 	ldr	w8, [sp, #16]   //
    4005b4:	b94017e9 	ldr	w9, [sp, #20]   //
    4005b8:	1b097d08 	mul	w8, w8, w9      //
    4005bc:	b9000fe8 	str	w8, [sp, #12]   //
    4005c0:	b9400fe0 	ldr	w0, [sp, #12]   //
    4005c4:	910083ff 	add	sp, sp, #0x20   //
    4005c8:	d65f03c0 	ret	                //
```

Q7: _Draw the contents of the stack and registers just prior to the execution of the second-to-last instruction. Assume the initial value of `sp` is `0x7FE0`._

<div style="page-break-after: always;"></div>

Q8: _Label each line of assembly code with the line number of the line of C code from which the assembly instruction was derived._
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
10
11  int main() {
12      int minutes = seasons_of_love();
13      printf("%d minutes\n", minutes);
14      printf("%d moments so dear\n", minutes - 600);
15      printf("%d minutes\n", minutes);
16      printf("How do you measure? Measure a year?\n");
17  }
```
```
0000000000400584 <seasons_of_love>:
    400584:	d10083ff 	sub	sp, sp, #0x20   //
    400588:	52802da8 	mov	w8, #0x16d      //
    40058c:	52800309 	mov	w9, #0x18       //
    400590:	5280078a 	mov	w10, #0x3c      //
    400594:	b9001fe8 	str	w8, [sp, #28]   //
    400598:	b9001be9 	str	w9, [sp, #24]   //
    40059c:	b90017ea 	str	w10, [sp, #20]  //
    4005a0:	b9401fe8 	ldr	w8, [sp, #28]   //
    4005a4:	b9401be9 	ldr	w9, [sp, #24]   //
    4005a8:	1b097d08 	mul	w8, w8, w9      //
    4005ac:	b90013e8 	str	w8, [sp, #16]   //
    4005b0:	b94013e8 	ldr	w8, [sp, #16]   //
    4005b4:	b94017e9 	ldr	w9, [sp, #20]   //
    4005b8:	1b097d08 	mul	w8, w8, w9      //
    4005bc:	b9000fe8 	str	w8, [sp, #12]   //
    4005c0:	b9400fe0 	ldr	w0, [sp, #12]   //
    4005c4:	910083ff 	add	sp, sp, #0x20   //
    4005c8:	d65f03c0 	ret	                //
```