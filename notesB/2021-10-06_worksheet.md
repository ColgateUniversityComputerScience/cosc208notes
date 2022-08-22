# Assembly: instruction formats; load/store
_COSC 208, Introduction to Computer Systems, 2021-10-06_

## Announcements
* Exam1 Q5


## Outline
* Assembly
* Operands
* Load/store


## Assembly
```C
1  #include <stdio.h>
2  int deref(int *p) {
3      int v = *p;
4      return v;
5  }
6  int main() {
7      int x = 2;
8      int *y = &x;
9      int z = deref(y);
10     printf("deref(y) = %d\n", z);
11     return 0;
12 }
```
```

0000000000400584 <deref>:

    400584:	d10043ff 	sub	sp, sp, #0x10

    400588:	f90007e0 	str	x0, [sp, #8]

    40058c:	f94007e8 	ldr	x8, [sp, #8]

    400590:	b9400109 	ldr	w9, [x8]

    400594:	b90007e9 	str	w9, [sp, #4]

    400598:	b94007e0 	ldr	w0, [sp, #4]

    40059c:	910043ff 	add	sp, sp, #0x10

    4005a0:	d65f03c0 	ret
```


 * Q1: _What do each of the columns contain?_

* Mapping between assembly and C code

 <div style="page-break-after: always;"></div> 



## Load/store
* Q2: _What is the C code equivalent for `str x0, [x1]`, treating registers as if they were variable names?_ 

```


```


* Q3: _What is the C code equivalent for `ldr x2, [x3]`, treating registers as if they were variable names?_ 

```


```
* Q4: _Write the C code equivalent for each line of assembly, treating registers as if they were variable names. For example, the C code equivalent for `sub sp, sp, #0x20` is `sp = sp - 0x20`_


```

0000000000400584 <deref>:

    400584:	d10043ff 	sub	sp, sp, #0x10

    400588:	f90007e0 	str	x0, [sp, #8]

    40058c:	f94007e8 	ldr	x8, [sp, #8]

    400590:	b9400109 	ldr	w9, [x8]

    400594:	b90007e9 	str	w9, [sp, #4]

    400598:	b94007e0 	ldr	w0, [sp, #4]

    40059c:	910043ff 	add	sp, sp, #0x10

    4005a0:	d65f03c0 	ret
```


<img src="diagrams/load_store.png" width="400" >
