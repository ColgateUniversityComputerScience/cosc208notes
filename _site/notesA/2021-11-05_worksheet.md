# Multiprocessing: limited direct execution; system calls; processes
_COSC 208, Introduction to Computer Systems, 2021-11-05_

## Announcements
* Project 2 Part B due Tuesday

## Outline
* Limited direct execution
* System calls
* Process abstraction
* Creating processes

## No warm-up: Happy Friday!

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

<div style="page-break-after:always;"></div>

## Process abstraction
Q1: _Consider building a Lego kit as an analogy for operating systems' process abstraction. Match each component of the analogy with the corresponding component of a real computer system._
* Analogy
    * Cabinet/drawers for storing Legos
    * Lego bricks
    * Building area (e.g., tabletop)
    * Instruction booklet
    * Following the assembly instructions
    * Current step for the instruction booklet
    * Completed kit
    * You
* Real system
    * CPU
    * persistent storage
    * process
    * program
    * program counter
    * program inputs
    * program outputs
    * registers and main memory
    
## Creating processes
Q2: _What does the following code output?_
```C
int main(int argc, char **argv) {
    printf("Before fork\n");
    int pid = fork();
    printf("After fork\n");
    return 0;
}
```
```





```

Q3: _What does the following code output (assuming the new process has PID 1819)?_
```C
int main(int argc, char **argv) {
    printf("Before fork");
    int pid = fork();
    if (pid == 0) {
        printf("Child gets %d\n", pid);
    } else {
        printf("Parent gets %d\n", pid);
    }
    return 0;
}
```
```





```