# Architecture: circuits 
_COSC 208, Introduction to Computer Systems, 2022-10-05_

## Announcements
* Programming project 2 due tomorrow @ 11pm

## Outline
* Warm-up: logic gates
* Hardware building blocks
* 1-bit circuits
* n-bit circuits

## Warm-up: logic gates
Q1: _Fill-in the truth tables for all six types of gates_

| A | B | (A AND B) | (A OR B) | (NOT A) | (A NAND B) | (A NOR B) | (A XOR B) |
| - | - | --------- | -------- | ------- | ---------- | --------- | --------- |
| 0 | 0 |           |          |         |            |           |           | 
| 0 | 1 |           |          |         |            |           |           | 
| 1 | 0 |           |          |         |            |           |           | 
| 1 | 1 |           |          |         |            |           |           | 

🛑 **STOP HERE** after completing the above questions; if you have extra time **skip ahead** to the extra practice. 

## Building logic gates

Q2: _How do you use AND and NOT gates to create a NAND gate?_
```





```

Q3: _How do you use OR and NOT gates to create a NOR gate?_
```





```

## 1-bit operations
Q4: _Fill-in the truth tables for the following logical operations_

| A | B | (A != B) | (A > B) | (A >= B) |
| - | - | -------- | ------- | -------- |
| 0 | 0 |          |         |          |
| 0 | 1 |          |         |          |
| 1 | 0 |          |         |          |
| 1 | 1 |          |         |          |

🛑 **STOP HERE** after completing the above questions; if you have extra time **skip ahead** to the extra practice. 

## 1-bit circuits

Q5: _Create a circuit for `A > B` using `AND`, `OR`, `NOT` gates_
```







```

Q6: _Create a circuit for `A >= B` using `AND`, `OR`, `NOT` gates_
```







```

<div style="page-break-after:always;"></div>

Q7: _Your goal is to create a 1-bit circuit to perform addition. The circuit will take 3 input bits (`A`, `B`, and `carry_in`) and produce 2 output bits (`sum` and `carry_out`)._

Q7a: _Complete the truth table for this operation_

| `A` | `B` | `carry_in` | `sum` | `carry_out` |
|-----|-----|------------|-------|-------------|
|  0  |  0  |     0      |       |             |
|  0  |  0  |     1      |       |             |
|  0  |  1  |     0      |       |             |
|  0  |  1  |     1      |       |             |
|  1  |  0  |     0      |       |             |
|  1  |  0  |     1      |       |             |
|  1  |  1  |     0      |   0   |      1      |
|  1  |  1  |     1      |   1   |      1      |

Q7b: _What is the boolean expression for `sum`?_
```





```

Q7c: _Draw the circuit for `sum`_
```





```

Q7d: _What is the boolean expression for `carry_out`?_
```





```

Q7e: _Draw the circuit for `carry_out`_
```





```

🛑 **STOP HERE** after completing the above questions; if you have extra time **skip ahead** to the extra practice. 

## N-bit circuits
Q8: _Fill-in the truth-table for `A > B` when A and B are two bits_

| A1 A2 | B1 B2 | A > B |
| ----- | ----- | ----- |
| 0   0 | 0   0 |       |
| 0   1 | 0   0 |       |
| 1   0 | 0   0 |       |
| 1   1 | 0   0 |       |
| 0   0 | 0   1 |       |
| 0   1 | 0   1 |       |
| 1   0 | 0   1 |       |
| 1   1 | 0   1 |       |
| 0   0 | 1   0 |       |
| 0   1 | 1   0 |       |
| 1   0 | 1   0 |       |
| 1   1 | 1   0 |       |
| 0   0 | 1   1 |       |
| 0   1 | 1   1 |       |
| 1   0 | 1   1 |       |
| 1   1 | 1   1 |       |

## Extra practice
Q9: _How do you use NAND gates to create a NOT gate?_
```





```

Q10: _How do you use NAND gates to create an AND gate?_