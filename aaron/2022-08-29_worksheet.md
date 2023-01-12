# C: compilation; types; operators; output
_COSC 208, Introduction to Computer Systems, 2022-01-28_

## Announcements
* Before next class: Read Dive Into Systems 1.3-1.4.0 and answer pre-class questions
* Welcome Back CS Dept Tea: Tuesday at 11:30am in McGregory 319

## Outline
* Warm-up
* Learning community guidelines
* Hello, C
* Types
* Operators
* Output

## Warm-up
Q1: _What are the main components of a computer system?_

<div style="height:10em;"></div>

🛑 Stop here after completing the warm-up; please **do not** work ahead

## Operators
Q2: _What is the output of this program?_
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

Q3: _What is the output of this program?_
```C
int main() {
    int x = 5;
        int y = x/2;
        int z = x%2;
        printf("%d %d\n", y, z);
}
```

<div style="page-break-after:always;"></div>

Q4: _What is the output of this program?_
```C
int main() {
    int x = 5;
    char y = 'A';
    y = y + 5;
    printf("%c %d\n", y, y);
}
```

🛑 Stop here after completing the above questions; if you have extra time please **skip ahead** to the extra practice.

## Output
Postponed to next class

## Extra practice
Q8: _Write a program that computes and displays the number of minutes in a year._