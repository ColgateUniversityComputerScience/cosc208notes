# Architecture: circuits 
_COSC 208, Introduction to Computer Systems, 2022-03-07_

## Announcements
* 2nd DEI in CS activity due Thursday at 11pm

## Outline
* Warm-up
* Logic gates
* 1-bit circuits
* n-bit circuits

## Warm-up
Q1: _Fill-in the truth tables for all six types of gates_

| A | B | (A AND B) | (A OR B) | (NOT A) | (A NAND B) | (A NOR B) | (A XOR B) |
| - | - | --------- | -------- | ------- | ---------- | --------- | --------- |
| 0 | 0 |           |          |         |            |           |           | 
| 0 | 1 |           |          |         |            |           |           | 
| 1 | 0 |           |          |         |            |           |           | 
| 1 | 1 |           |          |         |            |           |           | 

🛑 **STOP HERE** after completing the warm-up; if you have extra time take a few deep breaths to help reduce stress. 

## Building logic gates

Q2: _How do you use AND and NOT gates to create a NAND gate?_
```





```

Q3: _How do you use OR and NOT gates to create a NOR gate?_
```





```

Q4: _How do you use NAND gates to create a NOT gate?_
```





```

Q5: _How do you use NAND gates to create an AND gate?_
```





```

🛑 **STOP HERE** after completing the above questions; if you have extra time take a few deep breaths to help reduce stress. 

## Logical operations
Q6: _Fill-in the truth tables for the following logical operations_

| A | B | (A != B) | (A > B) | (A >= B) |
| - | - | -------- | ------- | -------- |
| 0 | 0 |          |         |          |
| 0 | 1 |          |         |          |
| 1 | 0 |          |         |          |
| 1 | 1 |          |         |          |

🛑 **STOP HERE** after completing the above question; if you have extra time take a few deep breaths to reduce stress.

## 1-bit circuits

Q7: _Create a circuit for `A > B` using `AND`, `OR`, `NOT` gates_
```







```

Q8: _Create a circuit for `A >= B` using `AND`, `OR`, `NOT` gates_
```







```

Q9: _Your goal is to create a 1-bit circuit to perform addition. The circuit will take 3 input bits (`A`, `B`, and `carry_in`) and produce 2 output bits (`sum` and `carry_out`)._

Q9a: _Complete the truth table for this operation_

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

<div style="page-break-after:always;"></div>

Q9b: _What is the boolean expression for `sum`?_
```





```

Q9c: _Draw the circuit for `sum`_
```





```

Q9d: _What is the boolean expression for `carry_out`?_
```





```

Q9e: _Draw the circuit for `carry_out`_
```





```