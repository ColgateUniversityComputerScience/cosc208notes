# C: arrays; strings; input
_COSC 208, Introduction to Computer Systems, 2021-09-06_

## Warm-up: Arrays
Q1: _What is the output of this program?_
```C
int main() {
    int sum = 0;
    int nums[] = { 1, 3, 5, 7 };
    for (int i = 0; i < 3; i++) {
        nums[i+1] -= 1;
        sum += nums[i];
    }
    printf("%d\n", sum);
}
```

Q2: _What is the output of this program?_
```C
int main() {
    int sum = 0;
    int zeros[10];
    for (int i = 0; i < 10; i++) {
        sum += zeros[i];
    }
    printf("%d\n", sum);
}
```

Q3: _What is the output of this program?_
```C
int main() {
    int sum = 0;
    int nums[] = { 1, 2, 3 };
    for (int i = 0; i <= 3; i++) {
        sum += nums[i];
    }
    printf("%d\n", sum);
}
```

🛑 Stop here after completing the warm-up; if you have extra time please **skip ahead** to the extra practice.

## Strings
Q4: _What is the output of this program?_
```C
#include <stdio.h>
#include <string.h>
int main() {
    char first[] = "Colgate";
    char second[10] = "Univ";
    printf("%lu\n", strlen(first));
    printf("%lu\n", strlen(second));
    first[strlen(first)] = '-';
    second[strlen(second)-1] = '.';
    printf("%s%s\n", first, second);
    first[3] = '.';
    first[4] = '\0';
    printf("%s %s\n", first, second);
}
```

Q5: _What is the output of this program?_
```C
int main() {
    char first[] = "Systems is fun!";
    char second[] = "Systems is fun!";
    if (first == second) {
        printf("1st == 2nd\n");
    }
    if (strcmp(first, second) == 0) {
        printf("1st cmp 2nd\n");
    }
    if (first == first) {
        printf("1st == 1st\n");
    }
    if (strcmp(first, first) == 0) {
        printf("1st cmp 1st\n");
    }
}
```

Q6: _Write a program that asks the user for a string and prints the string backwards._
```C

















```

## Extra practice
Q7: _Write a function called `avg` that takes an array of integers and the length of the array and returns the average of those integers._

Q8: _Write a function called `count` that takes an array of integers,  the length of the array, and an integer to search for and returns the number of times the specified integer appears in the array._

Q9: _Write a program that asks the user for a string and converts all lowercase letters to uppercase and all uppercase letters to lowercase; numbers and punctuation should be left unchanged._

Q10: _Write a program that asks the user for a string and checks if the string is a palindrome (i.e., reads the same forwards and backwards)._

