# Multiprocessing: exec; non-preemptive scheduling
_COSC 208, Introduction to Computer Systems, 2022-11-11_

## Announcements
* DEI Assignment 3 due Tuesday
* Exam 3
    * Study guide posted on Moodle
    * Take-home portion: released Wed, Nov 16; due Fri, Nov 18
    * In-class portion: Fri, Nov 18 

## Outline
* Warm-up
* Running a different program
* Scheduling processes
* First In First Out (FIFO) scheduling
* Shortest Job First (SJF) scheduling

## Warm-up (Q5 from Wednesday)

🛑 **STOP HERE** after completing the warm-up; if you have extra time take a few deep breaths to reduce stress.


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

🛑 **STOP HERE** after completing the above questions; if you have extra time take a few deep breaths to reduce stress.


<div style="page-break-after:always;"></div>

## First In First Out (FIFO) scheduling
Q3: _Consider the following processes:_

| Process | Arrival time | Duration | 
|---------|--------------|----------|
| A       | 0            | 15       |
| B       | 5            | 15       |
| C       | 10           | 60       |

_Determine the schedule and compute the turnaround time for each process using First In First Out (FIFO) scheduling._