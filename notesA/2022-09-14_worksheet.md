# Number representation: overflow; bitwise operators; real numbers
_COSC 208, Introduction to Computer Systems, 2022-09-14_

## Announcements
* Programming project 1 due tomorrow @ 11pm

## Outline
* Warm-up
* Overflow
* Bitwise operators
* Real numbers

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

## Overflow
_For each of the following computations, determine whether the computation overflows, underflows, or neither. Assume we are using 8-bit signed integers._

Q4: `0b10000000` + `0b01111111`
```


```

Q5: `0b10000001` + `0b01111111`
```


```

Q6: `0b10000000` + `0b10000001`
```


```

Q7: `0b11000000` + `0b11000000`
```



```

Q8: `0b01111111` + `0b00000001`
```


```

🛑 **STOP HERE** after completing the above questions; if you have extra time please **skip ahead** to the extra practice.

## Bitwise operators
Q9: `0b1010 | 0b0101`
```

```

Q10: `0b1010 & 0b0101`
```

```

Q11: `~(0b1100 & 0b0110)`
```

```

Q12: `0b1000 >> 0b011`
```

```

Q13: `0b0001 << 0b0010`
```

```

Q14: `0b1111 & (~0b0010)`
```

```

Q15: `0b0000 | 0b0010`
```

```

## Extra practice
_How many bytes of memory are reserved for each of the following variables?_
Q16: `int a;`
```
```

Q17: `unsigned int b;`
```
```

Q18: `char c;`
```
```

Q19: `long d;`
```
```

Q20: `int e[5];`
```
```

Q21: `char f[30];`
```
```


_Compute the following powers of two_
Q22: `2^4`
```
```

Q23: `2^6`
```
```

Q24: `2^8`
```
```

Q25: `2^10`
```
```

Q26: _Write a function called `sign` that takes a number expressed in binary using two's complement and returns `-1` if the number is negative, `0` if the number is zero, or `1` if the number is positive. The binary is stored as a character array that starts with `0b` and contains an arbitrary number of `'0'` and `'1'` characters._