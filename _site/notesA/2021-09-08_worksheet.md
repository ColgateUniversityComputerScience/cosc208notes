# C: structs; Number representation: number bases
_COSC 208, Introduction to Computer Systems, 2021-09-08_

## Warm-up
Q1: _Write a function called `count_words` that takes a string and counts the number of words in the string. Assume each word is separated by a single space, and the string will contain at least one word. For example, `"Today is Wednesday."` contains 3 words._
```C













```
🛑 Stop here after completing the warm-up; if you have extra time please **skip ahead** to the extra practice.

## Structs
Q2: _What is the output of this program?_
```C
struct one {
    char x;
    char y;
    short z;
};
struct two {
    int m;
    int n[10];
};
int main() {
    struct one a;
    struct two b;
    printf("%d %d\n", sizeof(struct one), sizeof(a.z));
    printf("%d %d\n", sizeof(b), sizeof(b.n));
}
```

<div style="page-break-after:always;"></div>
 
Q3: _What is the output of this program?_
```C
struct alpha {
    char x[10];
    int y;
};
struct beta {
    int b;
    int c;
};
int main() {
    struct alpha a = { "Colgate", 13 };
    struct beta b = { 1, 2 };
    struct beta c = { 3, 4 };
    a.y += -13;
    b.b = 5;
    c = b;
    b.c = 6;
    printf("a %s %d\n", a.x, a.y);
    printf("b %d %d\n", b.b, b.c);
    printf("c %d %d\n", c.b, c.c);
}
```
```




```
🛑 Stop here after completing the above questions; if you have extra time please **skip ahead** to the extra practice.

## Binary (i.e., base 2)
_Convert these binary numbers to decimal (i.e., base 10):_

Q4: `0b10`
```


```

Q5: `0b11`
```


```

Q6: `0b1010`
```


```

Q7: `0b1111`
```


```

Q8: `0b11001100`
```


```

🛑 Stop here after completing the above conversions; if you have extra time please **skip ahead** to the extra practice.

## Hexadecimal (i.e., base 16)
_Convert these hexadecimal numbers to decimal (i.e., base 10):_

Q9: `0x9`
```


```

Q10: `0xB`
```


```

Q11: `0xF`
```


```

Q12: `0x11`
```


```

Q13: `0x248`
```


```

🛑 Stop here after completing the above conversions; if you have extra time please **skip ahead** to the extra practice.

## Extra practice
Q14: _Write a struct definition to represent a date (year, month number, and day)._
```C






```

Q15: _Write a function called `compare` that takes two date structs and returns -1 if the first date occurs before the second, 0 if the dates are equal, and 1 if the first date occurs after the second._