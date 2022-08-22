# Program memory: free; structs
_COSC 208, Introduction to Computer Systems, 2022-03-02_

## Announcements
* Project 1 Part B due tomorrow at 11pm
* 2nd DEI in CS activity due Thursday, March 10

## Warm-up
_Assume you wanted to write a function that creates a copy of a string. What is wrong with each of the following attempts at writing such a function?_

Q1:
```C
char *copy1(char strA[]) {
    char strB[strlen(strA) + 1];
    strcpy(strB, strA);
    return strB;
}
```
```
```

Q2:
```C
char copy2(char strA[]) {
    char *strB = malloc(sizeof(char) * (strlen(strA) + 1));
    strcpy(strB, strA);
    return *strB;
}
```
```
```

Q3:
```C
char *copy3(char strA[]) {
    char *strB = malloc(sizeof(char *));
    strcpy(strB, strA);
    return strB;
}
```
```

```
🛑 **STOP HERE** after completing the warm-up; if you have extra time please **skip ahead** to the extra practice.

## free
_What memory deallocation mistake has been made in each of the following code snippets?_

Q4: 
```C
int *ptrA = malloc(sizeof(int) * 3);
int *ptrB = ptrA;
free(ptrA);
free(ptrB);
```
```
```

Q5:
```C
int *ptr = malloc(sizeof(int) * 3);
ptr[0] = 1;
free(ptr);
ptr[1] = 2;
```
```
```

Q6: 
```C
int *ptr = malloc(sizeof(int) * 3);
ptr++;
free(ptr);
```
```
```

Q7:
```C
int *ptrA = malloc(sizeof(int) * 3);
int *ptrB = ptrA;
ptrA[0] = 0;
ptrB[1] = 1;
free(ptrA);
ptrB[2] = 2;
```
```
```
🛑 **STOP HERE** after completing the above questions; if you have extra time please **skip ahead** to the extra practice.

## Pointers to structs
Assume you are given the following code:
```C
struct account {
    int number; // Account number
    int balance; // Current account balance
};
int deposit(struct account *acct, int amount);
int transfer(struct account *from, struct amount *to, int amount);
```

Q8: _Write the `deposit` function, which adds `amount` to the balance of `acct`. The function should return the amount deposited._
```C












```

Q9: _Write the `transfer` function which moves `amount` from one account to another. The function should return the amount transferred if the transfer was successful or 0 otherwise._
```C













```
<div style="page-break-after:always;"></div>

## Extra practice
_Two structs have been defined representing a queue and an item on a queue._
```C
struct item {
    int value;
    struct item *next;
};
struct queue {
    struct item *head;
    struct item *tail;
};
```

_The `new_queue` function creates a new, empty queue._
```C
struct queue *new_queue() {
    struct queue *q = malloc(sizeof(struct queue));
    q->head = NULL;
    q->tail = NULL;
    return q;
}
```

Q10: _Write a function called `enqueue` that adds a new value at the end of the queue._
```













```

Q11: _Write a function called `dequeue` that removes and returns the value at the head of the queue. The function should return -1 if the queue is empty._
```













```

Q12: _Write a function called `free_queue` that empties and frees a queue._