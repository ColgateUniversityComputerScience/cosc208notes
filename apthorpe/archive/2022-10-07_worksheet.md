# Architecture: circuits (continued)
_COSC 208, Introduction to Computer Systems, 2022-10-07_

## Announcements
* Programming project 3 due Thursday, October 20 @ 11pm

## Outline
* Warm-up
* Arithmetic circuits
* n-bit circuits
* Multiplexer circuit
* Arithmetic Logic Unit (ALU)


## Warm-up: logic gates
Q1: _Create a 1-bit circuit for `A <= B` using `AND`, `OR`, `NOT` gates_
```











```

🛑 **STOP HERE** after completing the warm-up; if you have extra time take a few deep breaths to reduce stress.


## N-bit circuits
Q3: _Fill-in the truth-table for `A > B` when A and B are two bits_

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

🛑 **STOP HERE** after completing the above questions; if you have extra time take a few deep breaths to reduce stress.

<div style="page-break-after:always;"></div>

## Arithmetic circuits
Q2: _Your goal is to create a 1-bit circuit to perform addition. The circuit will take 3 input bits (`A`, `B`, and `carry_in`) and produce 2 output bits (`sum` and `carry_out`)._

Q2a: _Truth table for this operation_

| `A` | `B` | `carry_in` | `sum` | `carry_out` |
|-----|-----|------------|-------|-------------|
|  0  |  0  |     0      |   0   |      0      |
|  0  |  0  |     1      |   1   |      0      |
|  0  |  1  |     0      |   1   |      0      |
|  0  |  1  |     1      |   0   |      1      |
|  1  |  0  |     0      |   1   |      0      |
|  1  |  0  |     1      |   0   |      1      |
|  1  |  1  |     0      |   0   |      1      |
|  1  |  1  |     1      |   1   |      1      |

Q2b: _What is the boolean expression for `sum`?_
```







```

Q2c: _Draw the circuit for `sum`_
```







```

Q2d: _What is the boolean expression for `carry_out`?_
```







```

Q2e: _Draw the circuit for `carry_out`_
```







```

🛑 **STOP HERE** after completing the above questions; if you have extra time take a few deep breaths to reduce stress.