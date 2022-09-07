# Number representation: base conversion; signed integers
_COSC 208, Introduction to Computer Systems, 2022-02-09_

## Warm-up
_Convert these hexadecimal numbers to decimal (i.e., base 10):_

Q1: `0x9`
```


```

Q2: `0xB`
```


```

Q3: `0xF`
```


```

Q4: `0x11`
```


```

Q5: `0x248`
```


```

🛑 Stop here after completing the warm-up; if you have extra time please **skip ahead** to the extra practice.

## Binary <-> Hex Conversion
_Convert these binary numbers to hexadecimal:_ 

Q6: `0b1010`
```

```

Q7: `0b1111`
```

```

Q8: `0b11001100`
```

```

Q9: `0b11100111`
```

```


_Convert these hexadecimal numbers to binary:_

Q10: `0x5`
```

```

Q11: `0x8`
```

```

Q12: `0xB`
```

```

Q13: `0x37`
```

```
🛑 Stop here after completing the above conversions; if you have extra time please **skip ahead** to the extra practice.

## Decimal -> Binary Conversion
_Convert these decimal numbers to binary:_

Q14: `10`
```

```

Q15: `15`
```

```

Q16: `42`
```

```

Q17: `192`
```

```
🛑 Stop here after completing the above conversions; if you have extra time please **skip ahead** to the extra practice.

## Signed integers
_Express these decimal numbers using 8-bit two's complement:_

Q18: `13`
```

```

Q19: `-128`
```

```

Q20: `-64`
```

```

Q21: `-1`
```

```

Q22: `-13`
```

```

Q23: `127`
```

```

## Extra practice
_Convert these binary numbers to decimal:_

Q24: `0b1111`
```

```

Q25: `0b10100`
```

```

Q26: `0b101000`
```

```

_Convert these hexadecimal numbers to decimal:_

Q27: `0xC`
```

```

Q28: `0x18`
```

```

Q29: `0x30`
```

```

_Write the following functions:_

Q30: _`abbreviate`: takes a string and modifies the string in place to include only the first letter of each word. For example, `"Talk To You Later"` is converted to `TTYL`._
```
















```

Q31: _`check_password`: takes a string and returns 1 if the string is at least 8 characters long and contains at least one uppercase letter, at least one lowercase letter, and at least one digit. Otherwise, the function returns 0. You may want to use the functions `isupper`, `islower`, and `isdigit`. They take a character as a parameter and return 1 if the character is an uppercase letter, lowercase letter, or digit, respectively; otherwise, they return 0._