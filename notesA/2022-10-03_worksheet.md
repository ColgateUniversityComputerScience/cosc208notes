# Architecture: von Neumann; logic gates
_COSC 208, Introduction to Computer Systems, 2022-10-03_

## Announcements
* Programming project 2 due Thurs @ 11pm

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
struct account *open_account(int starting);
int close_account(struct account *acct);
```

Q1: _Write the `deposit` function, which adds `amount` to the balance of `acct`. The function should return the amount deposited._
```C










```

Q2: _Write the `transfer` function which moves `amount` from one account to another. The function should return the amount transferred if the transfer was successful or 0 otherwise._
```C











```

Q3: _Write the `open_account` function, which creates a new account with a random account number and the specified `starting` balance._
```C












```

Q4: _Write the `close_account` function, which eliminates the account `acct` and returns the remaining balance._ 
```C












```
🛑 **STOP HERE** after completing the warm-up; if you have extra time take a few deep breaths to help reduce stress. 

<div style="page-break-after:always;"></div>

## Logic gates
Q5: _Fill-in the truth tables for all six types of gates_

| A | B | (A AND B) | (A OR B) | (NOT A) | (A NAND B) | (A NOR B) | (A XOR B) |
| - | - | --------- | -------- | ------- | ---------- | --------- | --------- |
| 0 | 0 |           |          |         |            |           |           | 
| 0 | 1 |           |          |         |            |           |           | 
| 1 | 0 |           |          |         |            |           |           | 
| 1 | 1 |           |          |         |            |           |           | 

🛑 **STOP HERE** after completing the above questions; if you have extra time **skip ahead** to the extra practice. 

## Building logic gates

Q6: _How do you use AND and NOT gates to create a NAND gate?_
```





```

Q7: _How do you use OR and NOT gates to create a NOR gate?_
```





```

## Extra practice
Q8: _How do you use NAND gates to create a NOT gate?_
```





```

Q9: _How do you use NAND gates to create an AND gate?_
```





```