# Multiprocessing: wait & exec; scheduling
_COSC 208, Introduction to Computer Systems, 2022-11-11_

## Announcements
* Project 4 deadline extended to Monday @ 11pm
* DEI Assignment 3 deadline extended to Monday, Nov 29 @ 11pm
* Exam 3
    * Take-home portion: released Wed, Nov 16; due Fri, Nov 18
    * In-class portion: Fri, Nov 18 

## Outline
* Warm-up
* Waiting for processes
* Running a different program
* Scheduling processes

## Warm-up
Q1: _What does the following code output?_
```C
int main() {
    int x = 10;
    int y = 20;
    int retval = fork();
    if (retval == 0) {
        y -= 5;
    } else {
        y+= 5;
    }
    printf("x=%d y=%d\n", x, y);
    return 0;
}
```

🛑 **STOP HERE** after completing the warm-up; if you have extra time take a few deep breaths to reduce stress.

## Waiting for processes
Q2: _What are all possible outputs of this program?_
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

Q3: _What are all possible outputs of this program (assuming the new process has PID 13346)?_
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

🛑 **STOP HERE** after completing the above questions; if you have extra time take a few deep breaths to reduce stress.

<div style="page-break-after:always;"></div>

## Running a different program
Example program
```C
int main(int argc, char **argv) {
    printf("Begin\n");
    int pid = fork();
    if (pid == 0) {
        printf("Child\n");
        char *cmd[] = { "/usr/bin/date", NULL };
        execv(cmd[0], cmd);
    } else {
        printf("Parent\n");
    }
    printf("End\n");
    return 0;
}
```

Q4: _What is the output produced by running `./progA`, assuming no errors occur?_
**progA:**
```C
int main() {
    pid_t a = fork();
    if (a == 0) {
        char *cmd[] = { "./progB", NULL };
        execv(cmd[0], cmd);
        printf("A 2nd gen\n");
        return 0;
    } else {
        wait(NULL);
        printf("A 1st gen\n");
        return 0;
    }
}
```
**progB:**
```C
int main() {
    pid_t b = fork();
    if (b == 0) {
        printf("B 2nd gen\n");
        return 0;
    } else {
        wait(NULL);
        printf("B 1st gen\n");
        return 0;
    }
}
```