# C: compilation; types; operators; output
_COSC 208, Introduction to Computer Systems, 2022-01-26_

## Announcements
* Masks are required in class, lab, and office hours
* Before next class: Read Dive Into Systems 1.3-1.4.0 and answer pre-class questions
* First lab today/tomorrow

## Outline
* Warm-up
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
Q5: _Assume the variables `year`, `month` and `day` contain the parts of a date. Use `printf` to output the data (e.g., `2022-1-26`)_

<div style="height:5em;"></div>

Q6: _Assume the variables `length` and `width` contain the dimensions of a sports field/court. Use `printf` to output the dimensions (`94ft x 50ft`)_

<div style="height:5em;"></div>

Q7: _Assume the variables `first` and `last` contain a patient's first and last initial, and the variables `systolic` and `diastolic` contain the patient's blood pressure readings. Use `printf` to output the patient's initials and blood pressure (e.g., `A.G. 115/70`)_

<div style="height:5em;"></div>

## Extra practice
Q8: _Write a program that computes and displays the number of minutes in a year._