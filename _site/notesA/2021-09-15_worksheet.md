# Number representation: bitwise operators; real numbers
_COSC 208, Introduction to Computer Systems, 2021-09-15_

## Announcements
* Project 1 Part A due tomorrow at 11pm
* Exam 1
    * Study guide posted on Moodle
    * Take-home portion: released Friday at the end of class; due Monday at the start of class
    * In-class portion: during class on Monday

## Warm-up 
_Perform the following computations with 8-bit signed integers_

Q1: `0b10100011 + 7`
```



```

Q2: `48 - 0b01100001`
```



```

Q3: `0b00100000 + 0b01100000`
```



```
🛑 **STOP HERE** after completing the warm-up; if you have extra time please **skip ahead** to the extra practice.


## Bitwise operators
Q4: `0b1010 | 0b0101`
```

```

Q5: `0b1010 & 0b0101`
```

```

Q6: `~(0b1100 & 0b0110)`
```

```

Q7: `0b1000 >> 0b011`
```

```

Q8: `0b0001 << 0b0010`
```

```

Q9: `0b1111 & (~0b0010)`
```

```

Q10: `0b0000 | 0b0010`
```

```

## Extra practice
_How many bytes of memory are reserved for each of the following variables?_
Q11: `int a;`
```
```

Q12: `unsigned int b;`
```
```

Q13: `char c;`
```
```

Q14: `long long d;`
```
```

Q15: `int e[5];`
```
```

Q16: `char f[30];`
```
```


_Compute the following powers of two_
Q17: `2^4`
```
```

Q18: `2^6`
```
```

Q19: `2^8`
```
```

Q20: `2^10`
```
```

Q21: `2^12`
```
```

Q22: `2^16`
```
```


Q23: _Write a function called `sign` that takes a number expressed in binary using two's complement and returns `-1` if the number is negative, `0` if the number is zero, or `1` if the number is positive. The binary is stored as a character array that starts with `0b` and contains an arbitrary number of `'0'` and `'1'` characters._