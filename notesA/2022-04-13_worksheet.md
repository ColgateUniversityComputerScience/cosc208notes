# Multiprocessing: limited direct execution; system calls
_COSC 208, Introduction to Computer Systems, 2022-04-13_

## Announcements
* Project 3 due tomorrow @ 11pm

## No warm-up: Happy Wednesday!

## System calls
* Example program
    ```C
    #include <stdio.h>
    #include <unistd.h>
    int user() {
        int uid = getuid();
        return uid;
    }
    int main() {
        int u = user();
        printf("User %d is running this process\n", u);
    }
    ```
* Assembly code
    ```
    00000000004006ac <user>:
        4006ac:	d10083ff 	sub	sp, sp, #0x20
        4006b0:	f9000bfe 	str	x30, [sp, #16]
        4006b4:	94007713 	bl	41e300 <__getuid>
        4006b8:	b9000fe0 	str	w0, [sp, #12]
        4006bc:	b9400fe0 	ldr	w0, [sp, #12]
        4006c0:	f9400bfe 	ldr	x30, [sp, #16]
        4006c4:	910083ff 	add	sp, sp, #0x20
        4006c8:	d65f03c0 	ret
    000000000041e300 <__getuid>:
        41e300:	d28015c8 	mov	x8, #0xae
        41e304:	d4000001 	svc	#0x0
        41e308:	d65f03c0 	ret
    ```
