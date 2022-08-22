# Assembly: load/store operations; arithmetic operations; translating assembly code to low-level C code
_COSC 208, Introduction to Computer Systems, 2022-03-11_

## Announcements
* Project 2 Part A due Thursday, Mar 31 

## Outline
* Warm-up
* Load/store operations 
* Arithmetic and bitwise operations
* Translating assembly code to low-level C code

## Warm-up: mapping assembly code to C code
Q1: _The following C code was compiled into assembly._
```C
1   #include <stdio.h>
2   int years_to_double(int rate) {
3       int ruleof72 = 72;
4       int years = ruleof72 / rate;
5       return years;
6   }
7   int main() {
8       int r = 10;
9       int y = years_to_double(r);
10      printf("With an interest rate of %d%% it will take ~%d 
            years to double your money\n", r, y);
11  }
```
_For each line of assembly, indicate which original line of C code (above) the assembly instruction was derived from._
```
000000000000076c <years_to_double>:
    76c:	d10083ff 	sub	sp, sp, #0x20
    770:	b9000fe0 	str	w0, [sp, #12]
    774:	52800900 	mov	w0, #0x48
    778:	b9001be0 	str	w0, [sp, #24]
    77c:	b9401be1 	ldr	w1, [sp, #24]
    780:	b9400fe0 	ldr	w0, [sp, #12]
    784:	1ac00c20 	sdiv	w0, w1, w0
    788:	b9001fe0 	str	w0, [sp, #28]
    78c:	b9401fe0 	ldr	w0, [sp, #28]
    790:	910083ff 	add	sp, sp, #0x20
    794:	d65f03c0 	ret
```

🛑 **STOP HERE** after completing the warm-up; if you have extra time please **skip ahead** to the extra practice.

## Load/store operations
 _Write the C code equivalent for each line of assembly, treating registers as if they were variable names._

Q2: `ldr x0, [sp]`
```C


```

Q3: `str w0, [sp]`
```C


```

Q4: `ldr x1, [sp,#12]`
```C


```

Q5: `str x2, [x3,#0x10]`
```C


```

🛑 **STOP HERE** after completing the above questions; if you have extra time please **skip ahead** to the extra practice.

## Arithmetic and logical operations
_Write the C code equivalent for each line of assembly, treating registers as if they were variable names._

Q6: `lsl w9, w9, w10`
```C


```

Q7: `and w9, w9, w10`
```C


```

Q8: `mul w9, w9, w10`
```C


```

Q9: `sdiv w9, w9, w10`
```C


```

🛑 **STOP HERE** after completing the above questions; if you have extra time please **skip ahead** to the extra practice.

## Translating assembly code to low-level C code
The following C program (`operands.c`) has been compiled into assembly:
```C
int operandsA(int a) {
    return a;
}
long operandsB(long b) {
    return b;
}
int operandsC(int *c) {
    return *c;
}
long operandsD(long *d) {
    return *d;
}
int main() {
    operandsA(5);
    operandsB(5);
    int x = 5;
    operandsC(&x);
    long y = 5;
    operandsD(&y);
}
```

Q10: _Write the C code equivalent for each line of assembly, treating registers as if they were variable names. The assembly code for the `operandsA` function has already been translated into low-level C code._
```
00000000000007ec <operandsA>:
    7ec:	d10043ff 	sub	sp, sp, #0x10   // sp = sp - 0x10
    7f0:	b9000fe0 	str	w0, [sp, #12]   // *(sp + 12) = w0
    7f4:	b9400fe0 	ldr	w0, [sp, #12]   // w0 = *(sp + 12)
    7f8:	910043ff 	add	sp, sp, #0x10   // sp = sp + 0x10
    7fc:	d65f03c0 	ret	                // return

0000000000000800 <operandsB>:
    800:	d10043ff 	sub	sp, sp, #0x10   //
    804:	f90007e0 	str	x0, [sp, #8]    //
    808:	f94007e0 	ldr	x0, [sp, #8]    //
    80c:	910043ff 	add	sp, sp, #0x10   //
    810:	d65f03c0 	ret	                //

0000000000000814 <operandsC>:
    814:	d10043ff 	sub	sp, sp, #0x10   //
    818:	f90007e0 	str	x0, [sp, #8]    //
    81c:	f94007e0 	ldr	x0, [sp, #8]    //
    820:	b9400000 	ldr	w0, [x0]        //
    824:	910043ff 	add	sp, sp, #0x10   //
    828:	d65f03c0 	ret	                //

000000000000082c <operandsD>:
    82c:	d10043ff 	sub	sp, sp, #0x10   //
    830:	f90007e0 	str	x0, [sp, #8]    //
    834:	f94007e0 	ldr	x0, [sp, #8]    //
    838:	f9400000 	ldr	x0, [x0]        //
    83c:	910043ff 	add	sp, sp, #0x10   //
    840:	d65f03c0 	ret	                //
```

Q11: _How does the assembly code for `operandsA` and `operandsB` differ? Why?_
```






```

Q12: _How does the assembly code for `operandsB` and `operandsD` differ? Why?_
```






```

Q13: _How does the assembly code for `operandsC` and `operandsD` differ? Why?_
```




```

## Extra practice
_Write the C code equivalent for each line of assembly, treating registers as if they were variable names._

Q14: 
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

Q15: 
```
000000000000076c <years_to_double>:
    76c:	d10083ff 	sub	sp, sp, #0x20
    770:	b9000fe0 	str	w0, [sp, #12]
    774:	52800900 	mov	w0, #0x48
    778:	b9001be0 	str	w0, [sp, #24]
    77c:	b9401be1 	ldr	w1, [sp, #24]
    780:	b9400fe0 	ldr	w0, [sp, #12]
    784:	1ac00c20 	sdiv	w0, w1, w0
    788:	b9001fe0 	str	w0, [sp, #28]
    78c:	b9401fe0 	ldr	w0, [sp, #28]
    790:	910083ff 	add	sp, sp, #0x20
    794:	d65f03c0 	ret
```

<!--
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



Q6: _Write the C code equivalent for each line of assembly, treating registers as if they were variable names._
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
-->