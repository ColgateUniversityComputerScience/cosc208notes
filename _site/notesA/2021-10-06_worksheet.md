# Assembly: instruction formats; load/store
_COSC 208, Introduction to Computer Systems, 2021-10-06_

## Announcements
* First DEI reflection due tomorrow at 11pm 

## Outline
* Warm-up
* Assembly
* Operands
* Load/store
* Practice

## Warm-up
Q1: _Create a 1-bit circuit for `A <= B` using `AND`, `OR`, `NOT` gates_
```





































```
🛑 **STOP HERE** after completing the warm-up; if you have extra time take a few deep breaths to help reduce stress.

## Assembly Example
C code (`deref.c`)
```C
1  #include <stdio.h>
2  long deref(long *p) {
3      long v = *p;
4      return v;
5  }
6  int main() {
7      long x = 2;
8      long y = deref(&x);
9      printf("y = %ld\n", y);
10     return 0;
11 }
```

Assembly code (excerpt from `deref.txt`)
```
000000000000083c <deref>:
    83c:   d10083ff        sub     sp, sp, #0x20
    840:   f90007e0        str     x0, [sp, #8]
    844:   f94007e0        ldr     x0, [sp, #8]
    848:   f9400000        ldr     x0, [x0]
    84c:   f9000fe0        str     x0, [sp, #24]
    850:   f9400fe0        ldr     x0, [sp, #24]
    854:   910083ff        add     sp, sp, #0x20
    858:   d65f03c0        ret
```

<div style="page-break-after: always;"></div>

## Practice
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

Q2: _Write the C code equivalent for each line of assembly, treating registers as if they were variable names. The assembly code for the `operandsA` function has already been translated into C code._
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

Q3: _How does the assembly code for `operandsA` and `operandsB` differ? Why?_
```






```

Q4: _How does the assembly code for `operandsB` and `operandsD` differ? Why?_
```






```

Q5: _How does the assembly code for `operandsC` and `operandsD` differ? Why?_
```






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
