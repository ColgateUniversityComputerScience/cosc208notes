# C: structs
_COSC 208, Introduction to Computer Systems, 2022-09-30_

## Announcements
* Programming project 2 due Thurs @ 11pm

## Outline
* Warm-up
* Command-line arguments
* Structs
* Pointers to structs

## Warm-up
Q1: _Draw a memory diagram depicting the contents of the stack and heap immediately before the function `elongate("dog")` returns._
```C
char **elongate(char *str) {
    char **result = malloc(sizeof(char *) * strlen(str));
    for (int i = 0; i < strlen(str); i++) {
        result[i] = malloc(sizeof(char) * (i + 2));
        for (int j = 0; j < i+1; j++) {
            result[i][j] = str[j];
        }
        result[i][i+1] = '\0';
    }
    return result;
}
```
```C





















```
🛑 Stop here after completing the warm-up; if you have extra time please **skip ahead** to the extra practice.

<div style="page-break-after:always;"></div>

## Structs
Q2: _What is the output of this program?_
```C
struct one {
    char x;
    char y;
};
struct two {
    int m;
    int n[10];
};
int main() {
    struct one a;
    struct two b;
    printf("%d %d\n", sizeof(struct one), sizeof(a.y));
    printf("%d %d\n", sizeof(b), sizeof(b.n));
}
```
```





```

Q3: _What is the output of this program?_
```C
struct alpha {
    char x[10];
    int y;
};
struct beta {
    int b;
    int c;
};
int main() {
    struct alpha a = { "Colgate", 13 };
    struct beta b = { 1, 2 };
    struct beta c = { 3, 4 };
    a.y += -13;
    b.b = 5;
    c = b;
    b.c = 6;
    printf("a %s %d\n", a.x, a.y);
    printf("b %d %d\n", b.b, b.c);
    printf("c %d %d\n", c.b, c.c);
}
```
```






```
🛑 Stop here after completing the above questions; if you have extra time please **skip ahead** to the extra practice.

<div style="page-break-after:always;"></div>

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

Q4: _Write the `deposit` function, which adds `amount` to the balance of `acct`. The function should return the amount deposited._
```C










```

Q5: _Write the `transfer` function which moves `amount` from one account to another. The function should return the amount transferred if the transfer was successful or 0 otherwise._
```C











```

## Extra practice
Q6: _Write a struct definition to represent a date (year, month number, and day)._
```C






```

Q7: _Write a function called `compare` that takes two date structs and returns -1 if the first date occurs before the second, 0 if the dates are equal, and 1 if the first date occurs after the second._

<div style="page-break-after:always;"></div>

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

Q8: _Write a function called `enqueue` that adds a new value at the end of the queue._
```













```

Q9: _Write a function called `dequeue` that removes and returns the value at the head of the queue. The function should return -1 if the queue is empty._
```













```

Q10: _Write a function called `free_queue` that empties and frees a queue._