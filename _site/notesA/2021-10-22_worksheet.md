# Exam 2 Review
_COSC 208, Introduction to Computer Systems, 2021-10-22_

## Announcements
* Exam 2
    * Study guide posted on Moodle
    * In-class portion: during class on Monday
    * Take-home portion: due at the beginning of class on Wednesday

## Code

### C
```C
1   int interest_due(int outstanding, int rate) {
2 	  int divisor = 12 * 100;
3 	  int annual = outstanding * rate;
4 	  int monthly = annual / divisor;
5 	  return monthly;
6   }
7
8   int make_payment(int outstanding, int payment, int rate) {
9 	  int interest = interest_due(outstanding, rate);
10  	int principal = payment - interest;
11  	if (principal > outstanding) {
12  		outstanding = 0;
13  	} else {
14  		outstanding -= principal;	
15  	}
16  	return outstanding;
17  }
18
19  int months_remain(int outstanding, int payment, int rate) {
20  	int months = 0;
21  	while (outstanding > 0) {
22  		months++;
23  		outstanding = make_payment(outstanding, payment, rate);
24  	}
25  	return months;
26  }
27
28  int main() {
29  	int outstanding = 0, payment = 0, rate = 0;
30  	printf("Outstanding principal: $");
31  	scanf("%d", &outstanding);
32  	printf("Monthly payment: $");
33  	scanf("%d", &payment);
34  	printf("Interest rate: ");
35  	scanf("%d", &rate);
36  	int remain = months_remain(outstanding, payment, rate);
37  	printf("Your loan will be paid off in %d months\n", remain);
38  }
```

<div style="page-break-after:always;"></div>

### Assembly
```
00000000004005d4 <interest_due>:
  4005d4:	d10083ff 	sub	sp, sp, #0x20
  4005d8:	52809608 	mov	w8, #0x4b0
  4005dc:	b9001fe0 	str	w0, [sp, #28]
  4005e0:	b9001be1 	str	w1, [sp, #24]
  4005e4:	b90017e8 	str	w8, [sp, #20]
  4005e8:	b9401fe8 	ldr	w8, [sp, #28]
  4005ec:	b9401be9 	ldr	w9, [sp, #24]
  4005f0:	1b097d08 	mul	w8, w8, w9
  4005f4:	b90013e8 	str	w8, [sp, #16]
  4005f8:	b94013e8 	ldr	w8, [sp, #16]
  4005fc:	b94017e9 	ldr	w9, [sp, #20]
  400600:	1ac90d08 	sdiv	w8, w8, w9
  400604:	b9000fe8 	str	w8, [sp, #12]
  400608:	b9400fe0 	ldr	w0, [sp, #12]
  40060c:	910083ff 	add	sp, sp, #0x20
  400610:	d65f03c0 	ret	

0000000000400614 <make_payment>:
  400614:	d100c3ff 	sub	sp, sp, #0x30
  400618:	f90013fe 	str	x30, [sp, #32]
  40061c:	b9001fe0 	str	w0, [sp, #28]
  400620:	b9001be1 	str	w1, [sp, #24]
  400624:	b90017e2 	str	w2, [sp, #20]
  400628:	b9401fe0 	ldr	w0, [sp, #28]
  40062c:	b94017e1 	ldr	w1, [sp, #20]
  400630:	97ffffe9 	bl	4005d4 <interest_due>
  400634:	b90013e0 	str	w0, [sp, #16]
  400638:	b9401be8 	ldr	w8, [sp, #24]
  40063c:	b94013e9 	ldr	w9, [sp, #16]
  400640:	6b090108 	subs	w8, w8, w9
  400644:	b9000fe8 	str	w8, [sp, #12]
  400648:	b9400fe8 	ldr	w8, [sp, #12]
  40064c:	b9401fe9 	ldr	w9, [sp, #28]
  400650:	6b09011f 	cmp	w8, w9
  400654:	5400006d 	b.le	400660 <make_payment+0x4c>
  400658:	b9001fff 	str	wzr, [sp, #28]
  40065c:	14000005 	b	400670 <make_payment+0x5c>
  400660:	b9400fe8 	ldr	w8, [sp, #12]
  400664:	b9401fe9 	ldr	w9, [sp, #28]
  400668:	6b080128 	subs	w8, w9, w8
  40066c:	b9001fe8 	str	w8, [sp, #28]
  400670:	b9401fe0 	ldr	w0, [sp, #28]
  400674:	f94013fe 	ldr	x30, [sp, #32]
  400678:	9100c3ff 	add	sp, sp, #0x30
  40067c:	d65f03c0 	ret	

0000000000400680 <months_remain>:
  400680:	d10083ff 	sub	sp, sp, #0x20
  400684:	f9000bfe 	str	x30, [sp, #16]
  400688:	b9000fe0 	str	w0, [sp, #12]
  40068c:	b9000be1 	str	w1, [sp, #8]
  400690:	b90007e2 	str	w2, [sp, #4]
  400694:	b90003ff 	str	wzr, [sp]
  400698:	b9400fe8 	ldr	w8, [sp, #12]
  40069c:	7100011f 	cmp	w8, #0x0
  4006a0:	37000148 	b.le 4006c8 <months_remain+0x4c>
  4006a4:	b94003e8 	ldr	w8, [sp]
  4006a8:	11000508 	add	w8, w8, #0x1
  4006ac:	b90003e8 	str	w8, [sp]
  4006b0:	b9400fe0 	ldr	w0, [sp, #12]
  4006b4:	b9400be1 	ldr	w1, [sp, #8]
  4006b8:	b94007e2 	ldr	w2, [sp, #4]
  4006bc:	97ffffd5 	bl	400614 <make_payment>
  4006c0:	b9000fe0 	str	w0, [sp, #12]
  4006c4:	17fffff4 	b	400698 <months_remain+0x18>
  4006c8:	b94003e0 	ldr	w0, [sp]
  4006cc:	f9400bfe 	ldr	x30, [sp, #16]
  4006d0:	910083ff 	add	sp, sp, #0x20
  4006d4:	d65f03c0 	ret	
```

<div style="page-break-after:always;"></div>

## Mapping assembly code to C source code
Q1: _For each line of assembly code, indicate which line of C code was used to generate that line of assembly code._
```
00000000004005d4 <interest_due>:
  4005d4:	d10083ff 	sub	sp, sp, #0x20   // 
  4005d8:	52809608 	mov	w8, #0x4b0      // 
  4005dc:	b9001fe0 	str	w0, [sp, #28]   // 
  4005e0:	b9001be1 	str	w1, [sp, #24]   // 
  4005e4:	b90017e8 	str	w8, [sp, #20]   // 
  4005e8:	b9401fe8 	ldr	w8, [sp, #28]   // 
  4005ec:	b9401be9 	ldr	w9, [sp, #24]   // 
  4005f0:	1b097d08 	mul	w8, w8, w9      // 
  4005f4:	b90013e8 	str	w8, [sp, #16]   // 
  4005f8:	b94013e8 	ldr	w8, [sp, #16]   //
  4005fc:	b94017e9 	ldr	w9, [sp, #20]   // 
  400600:	1ac90d08 	sdiv	w8, w8, w9    // 
  400604:	b9000fe8 	str	w8, [sp, #12]   // 
  400608:	b9400fe0 	ldr	w0, [sp, #12]   // 
  40060c:	910083ff 	add	sp, sp, #0x20   // 
  400610:	d65f03c0 	ret	                // 
```

Q2: _For each line of assembly code, indicate which line of C code was used to generate that line of assembly code._
```
0000000000400614 <make_payment>:
  400614:	d100c3ff 	sub	sp, sp, #0x30   // 
  400618:	f90013fe 	str	x30, [sp, #32]  // 
  40061c:	b9001fe0 	str	w0, [sp, #28]   // 
  400620:	b9001be1 	str	w1, [sp, #24]   // 
  400624:	b90017e2 	str	w2, [sp, #20]   // 
  400628:	b9401fe0 	ldr	w0, [sp, #28]   // 
  40062c:	b94017e1 	ldr	w1, [sp, #20]   // 
  400630:	97ffffe9 	bl	4005d4 <interest_due> // 
  400634:	b90013e0 	str	w0, [sp, #16]   // 
  400638:	b9401be8 	ldr	w8, [sp, #24]   // 
  40063c:	b94013e9 	ldr	w9, [sp, #16]   // 
  400640:	6b090108 	subs	w8, w8, w9    // 
  400644:	b9000fe8 	str	w8, [sp, #12]   // 
  400648:	b9400fe8 	ldr	w8, [sp, #12]   //
  40064c:	b9401fe9 	ldr	w9, [sp, #28]   // 
  400650:	6b09011f 	cmp	w8, w9          // 
  400654:	5400006d 	b.le	400660 <make_payment+0x4c>  // 
  400658:	b9001fff 	str	wzr, [sp, #28]  // 
  40065c:	14000005 	b	400670 <make_payment+0x5c>  // 
  400660:	b9400fe8 	ldr	w8, [sp, #12]   // 
  400664:	b9401fe9 	ldr	w9, [sp, #28]   // 
  400668:	6b080128 	subs	w8, w9, w8    // 
  40066c:	b9001fe8 	str	w8, [sp, #28]   // 
  400670:	b9401fe0 	ldr	w0, [sp, #28]   // 
  400674:	f94013fe 	ldr	x30, [sp, #32]  // 
  400678:	9100c3ff 	add	sp, sp, #0x30   // 
  40067c:	d65f03c0 	ret	                // 
```

<div style="page-break-after:always;"></div>

## Translating assembly into low-level C code
Q3: _For each of the following lines of assembly, write one or more lines of low-level C code that express the semantics (i.e., meaning) of the assembly code. Your C code should use register names as variable names._
```
0000000000400614 <make_payment>:
  400614:	d100c3ff 	sub	sp, sp, #0x30   // 
  400618:	f90013fe 	str	x30, [sp, #32]  // 
  40061c:	b9001fe0 	str	w0, [sp, #28]   // 
  400620:	b9001be1 	str	w1, [sp, #24]   // 
  400624:	b90017e2 	str	w2, [sp, #20]   // 
  400628:	b9401fe0 	ldr	w0, [sp, #28]   // 
  40062c:	b94017e1 	ldr	w1, [sp, #20]   // 
  400630:	97ffffe9 	bl	4005d4 <interest_due> // 
  400634:	b90013e0 	str	w0, [sp, #16]   // 
  400638:	b9401be8 	ldr	w8, [sp, #24]   // 
  40063c:	b94013e9 	ldr	w9, [sp, #16]   // 
  400640:	6b090108 	subs	w8, w8, w9    // 
  400644:	b9000fe8 	str	w8, [sp, #12]   // 
  400648:	b9400fe8 	ldr	w8, [sp, #12]   // 
  40064c:	b9401fe9 	ldr	w9, [sp, #28]   // 
  400650:	6b09011f 	cmp	w8, w9                        // 
  400654:	5400006d 	b.le	400660 <make_payment+0x4c>  //  
  400658:	b9001fff 	str	wzr, [sp, #28]  // 
  40065c:	14000005 	b	400670 <make_payment+0x5c>  // 
  400660:	b9400fe8 	ldr	w8, [sp, #12]   // 
  400664:	b9401fe9 	ldr	w9, [sp, #28]   // 
  400668:	6b080128 	subs	w8, w9, w8    // 
  40066c:	b9001fe8 	str	w8, [sp, #28]   // 
  400670:	b9401fe0 	ldr	w0, [sp, #28]   // 
  400674:	f94013fe 	ldr	x30, [sp, #32]  // 
  400678:	9100c3ff 	add	sp, sp, #0x30   // 
  40067c:	d65f03c0 	ret	                // 
```

<div style="page-break-after:always;"></div>

## Converting C code to use goto
Q4: _Create a `make_payment_goto` function that behaves the same as the `make_payment` function but uses `goto` statements, just as a compiler would do when generating assembly code._
```C















```

Q5: _Create a `months_remain_goto` function that behaves the same as the `months_remain` function but uses `goto` statements, just as a compiler would do when generating assembly code._
```C















```

<div style="page-break-after:always;"></div>

## Drawing the stack and registers after executing assembly
Q6: _Assume the code starts executing at the beginning of the `make_payment` function (i.e., `pc = 0x400614)`. Draw a digram that shows the contents of the stack and registers immediately before executing the `ret` instruction in the `interest_due` function (i.e., before executing the assembly instruction at address `0x400610`). Your stack and registers should contain values (e.g., `0x400614`) *not* variable or register names._

_Assume the initial values of the registers are as follows:_
* `pc = 0x4006c0`
* `sp = 0xf80`
* `w0 = 100000`
* `w1 = 500`
* `w2 = 3`
* `x30 = 0x96c`
