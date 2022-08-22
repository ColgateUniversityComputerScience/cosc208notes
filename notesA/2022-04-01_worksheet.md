# Efficiency: locality
_COSC 208, Introduction to Computer Systems, 2022-04-01_

## Announcements
* Exam 2
    * Study guide posted on Moodle
    * Take-home portion: released after class on Monday; due Thursday at 11pm 
    * In-class portion: during class on Wednesday

## Warm-up: reducing data movement
Q1: _Cross-out unecesary loads and stores for each of the following snippets of assembly code_
```
000000000000088c <interest_due>:
    88c:    sub    sp, sp, #0x20
    890:    str    w0, [sp, #12]
    894:    str    w1, [sp, #8]
    898:    ldr    w0, [sp, #12]
    89c:    ldr    w1, [sp, #8]
    8a0:    mul    w0, w1, w0
    8a4:    str    w0, [sp, #20]
    8a8:    mov    w0, #0x4b0
    8ac:    str    w0, [sp, #24]
    8b0:    ldr    w1, [sp, #20]
    8b4:    ldr    w0, [sp, #24]
    8b8:    sdiv   w0, w1, w0
    8bc:    str    w0, [sp, #28]
    8c0:    ldr    w0, [sp, #28]
    8c4:    add    sp, sp, #0x20
    8c8:    ret
```
```
0000000000400544 <sum>:
    400544:    d10043ff     sub    sp, sp, #0x10
    400548:    b9000fe0     str    w0, [sp, #12]
    40054c:    b9000be1     str    w1, [sp, #8] 
    400550:    b9400fe8     ldr    w8, [sp, #12]
    400554:    b9400be9     ldr    w9, [sp, #8] 
    400558:    0b090108     add    w8, w8, w9   
    40055c:    b90007e8     str    w8, [sp, #4] 
    400560:    b94007e0     ldr    w0, [sp, #4] 
    400564:    910043ff     add    sp, sp, #0x10
    400568:    d65f03c0     ret                 
```

🛑 **STOP HERE** after completing the above question; if you have extra time, take a few deep breaths to reduce stress.

<div style="page-break-after:always;"></div>

## Optimizing loops for locality
Q2: _Modify the following function to improve spatial locality_
```C
int *hundreds() {
    int *nums = malloc(sizeof(int) * 1000);
    for (int i = 0; i < 100; i++) {
        for (int j = 0; j < 1000; j+= 100) {
            nums[i+j] = i;
        }
    }
}
```

Q3: _Modify the following function to improve temporal locality_
```C
int odds(int *nums, int length) {
    for (int i = 0; i < length; i++) {
        nums[i] = nums[i] % 2;
    }
    int count = 0;
    for (int j = 0; j < length; j++) {
        count += nums[j];
    }
    return count;
}
```

Q4: _Modify the following function to improve spatial locality_
```C
void multiplication(int grid[][], int rows, int cols) {
    for (int c = 0; c < cols; c++) {
        for (int r = 0; r < rows; r++) {
            grid[r][c] = c * r;
        }
    }
}
```

Q5: _Modify the following function to improve temporal locality_
```C
long stdev(int *nums, int length) {
    long sum = 0;
    for (int i = 0; i < length; i++) {
        sum += nums[i];
    }
    int mean = sum / length;
    sum = 0;
    for (int j = 0; j < length; j++) {
        int diff = nums[j] - mean;
        sum += diff * diff:
    }
    mean = sum / length;
    return sqrt(mean);
}
```