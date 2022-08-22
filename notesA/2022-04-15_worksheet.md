# Multiprocessing: processes; fork & wait
_COSC 208, Introduction to Computer Systems, 2022-04-15_

## Announcements
* Project 3 deadline extended to Monday at 11pm

## No warm-up — Happy Friday!

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

🛑 **STOP HERE** after completing the above question; if you have extra time please **skip ahead** to the extra practice.
    
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

<div style="page-break-after:always;"></div>

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
🛑 **STOP HERE** after completing the above questions; if you have extra time please **skip ahead** to the extra practice.

## Waiting for processes
Q4: _What are all possible outputs of this program?_
```C
int main() {
    int pid = fork();
    if (pid == 0) {
        printf("Child\n");
    } else {
        wait(NULL);
        printf("Parent\n");
    }
    return 0;
}
```

<div style="page-break-after:always;"></div>

Q5: _What are all possible outputs of this program (assuming the new process has PID 13346)?_
```C
int main() {
    int pid = fork();
    printf("A %d\n", pid);
    if (pid == 0) {
        printf("B\n");
    } else {
        wait(NULL);
        printf("C\n");
    }
}
```
```














```

## Extra practice
Q6: _What does the following code output?_
```C
int main(int argc, char **argv) {
    int value = 100;
    int pid = fork();
    if (pid == 0) {
        value -= 50;
    } else {
        value += 50;
    }
    printf("My value is %d\n", value);
    return 0;
}
```

<div style="page-break-after:always;"></div>
    
Q7: _What does the following code output?_
```C
int main(int argc, char **argv) {
    printf("Begin\n");
    int pid = fork();
    if (pid == 0) {
        printf("Child\n");
        return 0;
    } else {
        printf("Parent\n");
    }
    printf("End\n");
}
```
```














```

Q8: _How would you modify the above program such that `Child` always prints before `Parent`?_