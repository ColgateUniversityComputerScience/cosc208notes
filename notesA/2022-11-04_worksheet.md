# Efficiency: cache replacement (continued); optimizing for locality
_COSC 208, Introduction to Computer Systems, 2022-11-04_

## Announcements
* No open lab hours on Tuesdays for the rest of the semester
* Project 4 due Thursday
* DEI Assignment 3 (Awareness of the Culture and Contributions of Indigenous Peoples) due Tues, Nov 15

## Outline
* Warm-up
* Cache replacement
* Optimizing loops for locality

## Warm-up
Q1: _For each of the following instances of caching, indicate whether the caching is motivated by temporal or spatial locality._
* A CPU caches the first 32 instructions of a function when the function is called
* A CPU caches all of the instructions for a frequently called function
* A web browser caches the Moodle pages for your courses, which you view multiple times per week
* A content distribution network (CDN) caches a video that has gone viral
* A content distribution network (CDN) caches "recommended videos" related to a video

🛑 **STOP HERE** after completing the warm-up; if you have extra time, take a few deep breaths to reduce stress.

## Cache replacement
_Assume a cache can hold 3 entries and the following 15 data accesses occur: 3, 4, 4, 5, 3, 2, 3, 4, 1, 4, 4, 2, 5, 2, 4. Assuming the cache is initially empty, what is the hit ratio for each of the following algorithms?_
* _Optimal_
    ```




    ```
* Q1: _FIFO_
    ```




    ```
* Q2: _LRU_
    ```




    ```

🛑 **STOP HERE** after completing the above questions; if you have extra time, take a few deep breaths to reduce stress.

<div style="page-break-after:always;"></div>

## Optimizing loops for locality
Q4: _Modify the following function to improve spatial locality_
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

Q5: _Modify the following function to improve temporal locality_
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

Q6: _Modify the following function to improve spatial locality_
```C
void multiplication(int grid[][], int rows, int cols) {
    for (int c = 0; c < cols; c++) {
        for (int r = 0; r < rows; r++) {
            grid[r][c] = c * r;
        }
    }
}
```

Q7: _Modify the following function to improve temporal locality_
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