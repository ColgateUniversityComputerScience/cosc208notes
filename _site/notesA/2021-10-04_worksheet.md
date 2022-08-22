# Architecture: circuits 
_COSC 208, Introduction to Computer Systems, 2021-10-04_

## Announcements
* First DEI reflection due Thursday at 11pm 

## Outline
* Warm-up
* 1-bit circuits
* n-bit circuits

## Warm-up
Q1: _Fill-in the truth tables for the following logical operations_

| A | B | (A != B) | (A > B) | (A >= B) |
| - | - | -------- | ------- | -------- |
| 0 | 0 |          |         |          |
| 0 | 1 |          |         |          |
| 1 | 0 |          |         |          |
| 1 | 1 |          |         |          |

🛑 **STOP HERE** after completing the warm-up; if you have extra time take a few deep breaths to help reduce stress.

## 1-bit circuits

Q2: _Create a circuit for `A > B` using `AND`, `OR`, `NOT` gates_
```







```

Q3: _Create a circuit for `A >= B` using `AND`, `OR`, `NOT` gates_
```







```

Q4: _Your goal is to create a 1-bit circuit to perform addition. The circuit will take 3 input bits (`A`, `B`, and `carry_in`) and produce 2 output bits (`sum` and `carry_out`)._

Q4a: _Complete the truth table for this operation_

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

Q4b: _What is the boolean expression for `sum`?_
```





```

Q4c: _Draw the circuit for `sum`_
```





```

Q4d: _What is the boolean expression for `carry_out`?_
```





```

Q4e: _Draw the circuit for `carry_out`_
```





```
🛑 **STOP HERE** after completing the above questions; if you have extra time take a few deep breaths to help reduce stress.

## N-bit circuits
Q5: _Fill-in the truth-table for `A > B` when A and B are two bits_

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