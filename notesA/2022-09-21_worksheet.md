# Exam 1 Review
_COSC 208, Introduction to Computer Systems, 2022-09-21_

## Announcements
* Exam 1
    * Study guide posted on Moodle
    * Take-home portion: released after class on Wednesday; due at the beginning of class on Friday
    * In-class portion: during class on Friday
* DEI assignment 2 due Thurs, Sept 29

## Binary arithmetic
_Perform the following calculations. Operands are encoded using two's complement encoding with 6 bits. For each calculation, express the result in binary and decimal, and indicate whether the result overflows, underflows, or neither._

Q1: `0b110000 + 0b111111`
```





```

Q2: `0b001111 + 0b000001`
```





```

Q3: `0b101010 + 0b100100`
```





```

Q4: `0b001000 + 0b011000`
```





```

Q5: `0b110000 + 0b010000`
```





```

<div style="page-break-after:always;"></div>

## Logical & bitwise operators
_For each of the following expressions, select all operators that make the expression evaluate to true. Operands are encoded using two's complement._

Q6: `0b110000 __ 0b111111`  
```
&   &&   |   ||   ^   <
```

Q7: `0b011110 __ 0b000001`  
```
&   &&   |   ||   ^   <
```

Q8: `0b000000 __ 0b000000`  
```
&   &&   |   ||   ^   <
```

Q9: `0b000111 __ 0b000111`  
```
&   &&   |   ||   ^   <
```

## Strings
Q10: _The following program should ask the user to enter a word, then print the word's length and whether it is a palindrome (i.e., reads the same backward as forward). For example, if the user enters `"kayak"` the program should print `"The word is 5 characters long and is a palindrome."` However, the program contains several errors. Modify the program to correct the errors._

```C
#include <stdio.h>

void palindrome(char word[]) {
    int i = 0;
    int j = strlen(word);
    while (i < j) {
        if (word[i] != word[j]) {
            return -1;
        }
        i++;
        j--;
    }
    return 1;
}

int main() {
    printf("Enter a word: ");
    char word[50];
    fgets(word, 50, stdin);
    word[strlen(word)-1] = '\0'; // Remove newline
    int len = strlen(word);
    printf("The word is %c characters long and is ", len);
    if (palindrome(word)) {
        printf("a palindrome.\n");
    } else {
        printf("not a palindrome.\n");
    }
}
```

<div style="page-break-after:always;"></div>

Q11: _Write a function called `molecular_formula` that takes a string containing the constituent atoms of a molecule and updates the string to contain the molecular formula. For example, the string `"HHO"` should be changed to `"H20"`, and the string `"HHSOOOO"` should be changed to `"H2SO4"`. You can assume:_
* _Molecules will only contain elements that are represented by a single letter — e.g., a molecule may contain `'H'` but not `"Na"`_
* _All atoms of the same element are listed consecutively — e.g., the constituent atoms may be provided as `"HHO"` but not `"HOH"`_
* _The elements are listed in the order they should appear in the molecular formula — e.g., the constituent atoms `"HHO"` are changed to the molecular formula `"H2O"`, whereas the constituent atoms `"OHH"` are changed to the molecular formula `"OH2"`_
* _There will be at most 9 atoms of each element — e.g., `"H9C9"` may occur, but `"H10C11"` will not occur_

<div style="page-break-after:always;"></div>

## Number base conversions
_Perform the following conversions_

Q12: `97` to 8-bit unsigned binary
```



```

Q13: `-42` to 8-bit two's complement
```



```

Q14: `0b11001100` to unsigned decimal
```



```

Q15: `0b11001100` to signed decimal
```



```

Q16: `0x27` to unsigned decimal
```



```

Q17: `0xDEAD` to 16-bit binary
```



```

## Pointers
Q18: _What is the output of this program?_
```C
#include <stdio.h>
#include <string.h>

int main() {
    char first[10] = "Go";
    char second[] = "Raiders";
    char *f = first;
    char *s = &second[1];
    printf("%d %d\n", strlen(f), strlen(s));
    *(s+2) = 'n';
    f += 1;
    *(++f) = 't';
    first[3] = '\0';
    second[4] = '\0';
    printf("%d %d\n", strlen(f), strlen(s));
    printf("%s %s\n", first, second);
}
```

<div style="page-break-after:always;"></div>

Q19: _What is the output of this program?_
```C
#include <stdio.h>
#include <string.h>

void modify(char *str, int idx) {
    char tmp = str[0];
    idx--;
    str[0] = str[idx];
    str[idx] = tmp;
}

int main() {
    char a[5] = "none";
    char b[3] = "no";
    char *x = &(a[1]);
    printf("%s %s\n", b, x);

    char *y = b;
    int i = strlen(y);
    printf("%s %d\n", y, i);

    modify(y, i);
    printf("%s-%s-%s %d\n", x, y, x, i);

    *(a+2) = '\0';
    i = strlen(a);
    printf("%s %d\n", a, i);
}
```