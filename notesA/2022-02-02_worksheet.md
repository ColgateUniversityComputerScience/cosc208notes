# C: arrays; strings; input
_COSC 208, Introduction to Computer Systems, 2022-02-02_

## Announcements
* First DEI activity due Thurs, Feb 10

## Warm-up
Q1: _Draw the contents of the stack immediately before the program prints "n=2"_
```C
int recurse(int n) {
    printf("n=%d\n", n);
    if (n == 1) {
        return 0;
    }
    else {
        return 1 + recurse(n/2);
    }
}
int main() {
    int x = 16;
    int r = recurse(x);
    printf("result=%d\n", r);
}
```

Q2: _If `main` initialized `x` to `64` (instead of `16`), how many stack frames would exist immediately before the program printed "n=2"?_

## Arrays
Q3: _What is the output of this program?_
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

Q4: _What is the output of this program?_
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

Q5: _What is the output of this program?_
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

🛑 Stop here after completing the above questions; if you have extra time please **skip ahead** to the extra practice.

## Strings
Q6: _What is the output of this program?_
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

Q7: _What is the output of this program?_
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
}
```

Q8: _Write a program that asks the user for a string and prints the string backwards._
```C

















```

## Extra practice
Q9: _Write a function called `avg` that takes an array of integers and the length of the array and returns the average of those integers._

Q10: _Write a function called `count` that takes an array of integers,  the length of the array, and an integer to search for and returns the number of times the specified integer appears in the array._

Q11: _Write a program that asks the user for a string and converts all lowercase letters to uppercase and all uppercase letters to lowercase; numbers and punctuation should be left unchanged._

Q12: _Write a program that asks the user for a string and checks if the string is a palindrome (i.e., reads the same forwards and backwards)._

