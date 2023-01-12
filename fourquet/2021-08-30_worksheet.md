# Hello, systems; Hello, C
_COSC 208, Introduction to Computer Systems, 2021-08-30_

## Announcements
* Before next class: read DiS sections and answer _individually_ pre-class questions
* Is there any volunteer to switch from 208LC to LB?

## Outline

* Syllabus
* Warm-up: Hello, system
* Hello, C 

## Warm-up: Hello, system 

* _Q1: What are the main components of a computer system? What is the role of each of them?_  

    1.
    2.
    3.
    4.
    5.

* _Q2: What do you think of when you hear the term “Computer Systems”?_

    +
    +
    +
    +
    + ..

* _Q3: Why is it important to learn about computer systems?_



<div style="page-break-after: always;"></div>

## Hello, C: 

_Q4: What is the output of this program?_
```C
int main() {
    int x = 1;
    int y = 2;
    x = x+5;
    printf("%d ", x);
    x = y*2;
    printf("%d ", x);
    x *= 5;
    printf("%d ", x);
    printf("%d ", x--);
    printf("%d ", x);
    printf("%d ", --x);
    printf("%d", x);
}
```

## Demo

In Visual Studio Code: A C program that prints `"Hello, C!"`. How to compile and run it?

## More practice 

_Q5: What is the output of this program?_
```C
int main() {
    int x = 5;
    int y = x/2;
    int z = x%2;
    printf("%d %d\n", y, z);
}
```
_Q6: What is the output of this program?_
```C
int main() {
    int x = 5;
    char y = 'F';
    y = y - x;
    printf("%c %d\n", y, y);
}
```

<!--
## Output

Syntax of `printf`
## Q5: Extra practice
* _Write a program that computes and displays the number of minutes in a year._
-->
_Worksheet created by Professor Aaron Gember-Jacobson_