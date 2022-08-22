# Architecture: von Neumann; logic gates
_COSC 208, Introduction to Computer Systems, 2022-03-04_

## Announcements
* 2nd DEI in CS activity due Thursday at 11pm

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
struct account *open_account(int starting);
int close_account(struct account *acct);
```

Q1: _Write the `open_account` function, which creates a new account with a random account number and the specified `starting` balance._
```C












```

Q2: _Write the `close_account` function, which eliminates the account `acct` and returns the remaining balance._ 
```C












```
🛑 **STOP HERE** after completing the warm-up; if you have extra time take a few deep breaths to help reduce stress. 

<div style="page-break-after:always;"></div>

## Logic gates
Q3: _Fill-in the truth tables for all six types of gates_

| A | B | (A AND B) | (A OR B) | (NOT A) | (A NAND B) | (A NOR B) | (A XOR B) |
| - | - | --------- | -------- | ------- | ---------- | --------- | --------- |
| 0 | 0 |           |          |         |            |           |           | 
| 0 | 1 |           |          |         |            |           |           | 
| 1 | 0 |           |          |         |            |           |           | 
| 1 | 1 |           |          |         |            |           |           | 

🛑 **STOP HERE** after completing the above questions; if you have extra time take a few deep breaths to help reduce stress. 

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