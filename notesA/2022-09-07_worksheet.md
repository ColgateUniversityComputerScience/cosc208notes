# Number representation: number bases; base converstion
_COSC 208, Introduction to Computer Systems, 2022-02-07_

## Announcements
* DEI assignment 1 due tomorrow @ 11pm
* Programming project 1 due Thurs, Sept 15 @ 11pm

## Outline
* Warm-up
* Binary
* Hexadecimal
* Binary <-> hex conversion

## Warm-up
Q1: _What is the output of this program?_
```C
int main() {
    char first[] = "Colgate";
    char second[10] = "Univ";
    printf("%lu %lu\n", strlen(first));
    printf("%lu %lu\n", strlen(second));
    first[strlen(first)] = '-';
    second[strlen(second)-1] = '.';
    printf("%s%s\n", first, second);
    first[3] = '.';
    first[4] = '\0';
    printf("%s %s\n", first, second);
}
```

Q2: _Write a program that asks the user for a string and prints the string backwards._
```C












```

🛑 Stop here after completing the warm-up; if you have extra time please **skip ahead** to the extra practice.

## Binary (i.e., base 2)
_Convert these binary numbers to decimal (i.e., base 10):_

Q3: `0b11`
```


```

Q4: `0b1010`
```


```

Q5: `0b11001100`
```


```

🛑 Stop here after completing the above conversions; if you have extra time please **skip ahead** to the extra practice.

## Hexadecimal (i.e., base 16)
_Convert these hexadecimal numbers to decimal (i.e., base 10):_

Q6: `0xF`
```


```

Q7: `0x11`
```


```

Q8: `0x248`
```


```

🛑 Stop here after completing the above conversions; if you have extra time please **skip ahead** to the extra practice.

## Binary <-> Hex Conversion
_Convert these binary numbers to hexadecimal:_ 

Q9: `0b1010`
```


```

Q10: `0b1111`
```


```

Q11: `0b11100111`
```


```

_Convert these hexadecimal numbers to binary:_

Q12: `0x5`
```


```

Q13: `0xB`
```


```

Q14: `0x37`
```


```

🛑 Stop here after completing the above conversions; if you have extra time please **skip ahead** to the extra practice.

## Extra practice
Q15: _Write a function called `count_words` that takes a string and counts the number of words in the string. Assume each word is separated by a single space, and the string will contain at least one word. For example, `"Today is Wednesday."` contains 3 words._
```C













```

_Convert these binary numbers to decimal (i.e., base 10):_
* Q16: `0b10`
    ```


    ```
* Q17: `0b1111`
    ```


    ```
_Convert these hexadecimal numbers to decimal (i.e., base 10):_
* Q18: `0x9`
    ```

    
    ```
* Q19: `0xB`
    ```


    ```
* Q20: `0xC`
    ```


    ```
* Q21: `0x18`
    ```


    ```
* Q22: `0x30`
    ```


    ```

_Convert these binary numbers to hexadecimal:_ 
* Q23: `0b11001100`
    ```


    ```
* Q24: `0b101111111111`
    ```


    ```

_Convert these hexadecimal numbers to binary:_
* Q25: `0x8`
    ```


    ```
* Q26: `0xBEE`
    ```


    ```

Q27: _Write a function called `abbreviate` that takes a string and modifies the string in place to include only the first letter of each word. For example, `"Talk To You Later"` is converted to `TTYL`._