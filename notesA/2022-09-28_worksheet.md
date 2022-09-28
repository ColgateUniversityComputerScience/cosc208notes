# Program memory: free; 2D arrays; command-line arguments
_COSC 208, Introduction to Computer Systems, 2022-09-28_

## Announcements
* DEI assignment 2 due tomorrow @ 11pm
* Programming project 2 due Thurs, Oct 6 @ 11pm

## Outline
* Warm-up
* Heap memory deallocation
* 2D arrays on the stack
* 2D arrays as 1D arrays
* 2D arrays as arrays-of-arrays
* Command-line arguments

## Warm-up
_Assume you wanted to write a function that creates a copy of a string. What is wrong with each of the following attempts at writing such a function?_

Q1:
```C
char *copy1(char strA[]) {
    char strB[strlen(strA) + 1];
    strcpy(strB, strA);
    return strB;
}
```
```
```

Q2:
```C
char copy2(char strA[]) {
    char *strB = malloc(sizeof(char) * (strlen(strA) + 1));
    strcpy(strB, strA);
    return *strB;
}
```
```
```

Q3:
```C
char *copy3(char strA[]) {
    char *strB = malloc(sizeof(char *));
    strcpy(strB, strA);
    return strB;
}
```
```

```
🛑 **STOP HERE** after completing the warm-up; if you have extra time please **take a few deep breaths** to reduce stress.

## free
_What memory deallocation mistake has been made in each of the following code snippets?_

Q4: 
```C
int *ptrA = malloc(sizeof(int) * 3);
int *ptrB = ptrA;
free(ptrA);
free(ptrB);
```
```
```

<div style="page-break-after: always;"></div>

Q5:
```C
int *ptr = malloc(sizeof(int) * 3);
ptr[0] = 1;
free(ptr);
ptr[1] = 2;
```
```
```

Q6: 
```C
int *ptr = malloc(sizeof(int) * 3);
ptr++;
free(ptr);
```
```
```

Q7:
```C
int *ptrA = malloc(sizeof(int) * 3);
int *ptrB = ptrA;
ptrA[0] = 0;
ptrB[1] = 1;
free(ptrA);
ptrB[2] = 2;
```
```
```
🛑 **STOP HERE** after completing the above questions; if you have extra time please **take a few deep breaths** to reduce stress.

## 2D arrays on the stack
Q8: _Assume we wanted to create an array to represent a calendar:_
```
+----+----+----+----+----+----+----+
|  1 |  2 |  3 |  4 |  5 |  6 |  7 |
+----+----+----+----+----+----+----+
|  8 |  9 | 10 | 11 | 12 | 13 | 14 |
+----+----+----+----+----+----+----+
| 15 | 16 | 17 | 18 | 19 | 20 | 21 |
+----+----+----+----+----+----+----+
| 22 | 23 | 24 | 25 | 26 | 27 | 28 |
+----+----+----+----+----+----+----+
```
_Write a function called `fill_calendar` that creates a 2D array on the stack and populates the array with the appropriate values._

<div style="page-break-after: always;"></div>

🛑 **STOP HERE** after completing the above question; if you have extra time please **take a few deep breaths** to reduce stress.

## 2D arrays as 1D arrays
Q9: _Fill-in the blanks to complete the `fill_calendar_linear` function which creates a fully linear calendar._
```C
void fill_calendar_linear() {
    int calendar[_____];
    int day = 1;
    for (int week = 0; week < 4; week++) {
        for (int dow = 0; dow < 7; dow++) {
            calendar[__________________] = day;
            day++;
        }
    }
}
```

## 2D arrays as arrays-of-arrays
```C
int **fill_calendar_arrayofarrays_heap() {
    int **calendar = malloc(sizeof(int *) * 4);
    int day = 1;
    for (int week = 0; week < 4; week++) {
        calendar[week] = malloc(sizeof(int) * 7);
        for (int dow = 0; dow < 7; dow++) {
            calendar[week][dow] = day;
            day++;
        }
    }
    return calendar;
}
```
