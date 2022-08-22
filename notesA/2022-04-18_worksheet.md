# Multiprocessing: exec; non-preemptive scheduling
_COSC 208, Introduction to Computer Systems, 2022-04-18_

## Announcements
* Project 3 due today at 11pm
* 3rd DEI activity due Thursday

## Warm-up (Q5 from Friday)
Q1: _What are all possible outputs of this program (assuming the new process has PID 13346)?_
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
🛑 **STOP HERE** after completing the warm-up; if you have extra time take a few deep breaths to help reduce stress.

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

<div style="page-break-after:always;"></div>

Q2: _What is the output produced by running `./progA`, assuming no errors occur?_
**progA:**
```C
int main() {
    pid_t a = fork();
    if (a == 0) {
        execv("./progB", NULL);
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