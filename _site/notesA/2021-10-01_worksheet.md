# Architecture: von Neumann; logic gates
_COSC 208, Introduction to Computer Systems, 2021-10-01_

## Announcements
* First DEI reflection due Thursday at 11pm 

## Outline
* Warm-up
* von Neumann Architecture
* Hardware building blocks
* Logic gates

## Warm-up
Assume you are given the following code:
```C
struct account {
    int number; // Account number
    int balance; // Current account balance
};
int deposit(struct account *acct, int amount);
int transfer(struct account *from, struct amount *to, int amount);
```

Q1: _Write the `deposit` function, which adds `amount` to the balance of `acct`. The function should return the amount deposited._
```C













```

Q2: _Write the `transfer` function which moves `amount` from one account to another. The function should return the amount transferred if the transfer was successful or 0 otherwise._
```C














```

## Logic gates
Q3: _Fill-in the truth tables for all six types of gates_

| A | B | (A AND B) | (A OR B) | (NOT A) | (A NAND B) | (A NOR B) | (A XOR B) |
| - | - | --------- | -------- | ------- | ---------- | --------- | --------- |
| 0 | 0 |           |          |         |            |           |           | 
| 0 | 1 |           |          |         |            |           |           | 
| 1 | 0 |           |          |         |            |           |           | 
| 1 | 1 |           |          |         |            |           |           | 

## Building logic gates

Q4: _How do you use AND and NOT gates to create a NAND gate?_
```





```

Q5: _How do you use OR and NOT gates to create a NOR gate?_
```





```

Q6: _How do you use NAND gates to create a NOT gate?_
```





```

Q7: _How do you use NAND gates to create an AND gate?_
```





```