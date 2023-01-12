# Number representation: binary arithmetic; overflow
_COSC 208, Introduction to Computer Systems, 2021-09-13_

## Announcements
* Project 1 Part 1 due Thursday (two days mercy Saturday night)
* Exam 1 this Friday

## Warm-up
_Express these decimal numbers using 8-bit two's complement:_

Q1: -49
```


```

Q2: -11
```


```
🛑 **STOP HERE** after completing the warm-up; if you have extra time please **skip ahead** to the extra practice.

## Binary arithmetic
_Use 8-bit signed integers_

Q3: 10 + 5
```




```

Q4: 7 + 15
```




```

Q5: -10 + 5
```




```

Q6: 10 - 5
```




```

Q7: 64 + 64
```




```
🛑 **STOP HERE** after completing the above questions; if you have extra time please **skip ahead** to the extra practice.

## Overflow
_For each of the following computations, determine whether the computation overflows, underflows, or neither. Assume we are using 8-bit signed integers._

Q8: `0b10000000` + `0b01111111`
```



```

Q9: `0b10000001` + `0b01111111`
```



```

<div style="page-break-after:always;"></div>

Q10: `0b10000000` + `0b10000001`
```



```

Q11: `0b11000000` + `0b11000000`
```



```

Q12: `0b01111111` + `0b00000001`
```



```

## Extra practice
Q13: _Convert `512` to unsigned binary._
```


```

Q14: _Convert `-42` to 8-bit signed binary._
```


```

Q15: _Convert `0xFAB` to unsigned binary._
```


```


Turn page
<div style="page-break-after:always;"></div>



Q16: _Write a function called `valid_hex` that takes a string and returns 1 if it is a valid hexadecimal number; otherwise return 0. A valid hexadecimal number must start with `0x` and only contain the digits `0`-`9` and letters `A`-`F` (in upper or lower case)._
```



















```

_Worksheet created by Professor Aaron Gember-Jacobson_