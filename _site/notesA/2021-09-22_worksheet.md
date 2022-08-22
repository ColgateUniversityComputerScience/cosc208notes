# Program memory: pointers
_COSC 208, Introduction to Computer Systems, 2021-09-22_

## Announcements
* DEI reflection due Thurs, Oct 7
    * Core SP lecture tomorrow @ 4:30pm in Ho 101
* Project 1 Part B due next Thursday (September 30)

## Warm-up

Q1: _What words can you spell with only hex digits? (You are allowed to use digits for letters that look alike: 0 = O, 1 = I or l, 2 = Z, 5 = S.)_
```





```
🛑 **STOP HERE** after completing the warm-up; if you have extra time **take a few deep breaths** to help reduce stress.

## Pointers

Q2: _Write a snippet of code that:_
1. _Declares a `char` variable called `orig` and initializes it with the value `'A'`_
2. _Declares and initializes a pointer called `ptr` that points to `orig`_
3. _Uses the pointer to update the value stored in `orig` to `'B'`_

```C



```

Q3: _What is the output of this program?_ — draw a memory diagram to help
```C
int main() {
    int a = 1;
    int b = 2;
    char c = 'C';
    int *x = &a;
    int *y = &b;
    char *z = &c;
    printf("%d %d %c\n", *x, *y, *z);
    *x += 1;
    b += 2;
    *z = 'D';
    printf("%d %d %c\n", *x, *y, *z);
    printf("%d %d %c\n", a, b, c);
    x = y;
    *x += 10;
    a += 20;
    printf("%d %d\n", *x, *y);
    printf("%d %d\n", a, b);
}
```
```




```

Q4: _What is the output of this program?_
```C
int main() {
    int a = 1; // Assume at 0x4
    int *x = &a; // Assume at 0x8
    int **y = &x; // Assume at 0xC
    printf("%p %p %p\n", a, x ,y);
    printf("%p %p\n", *x , *y);
}
```
```
```
🛑 **STOP HERE** after completing the warm-up; if you have extra time please **skip ahead** to the extra practice.

## Pointers as parameters

_Example_
```C
void value(int a) {
    a = 2;
}
void pointer(int *b) {
    *b = 3;
}
int main() {
    int v = 1;
    int *p = &v;
    value(v);
    printf("%d\n", v);
    pointer(p);
    printf("%d\n", v);
}
```

Q5: _What is the output of this program?_
```C
void copy1(int a, int b) {
    a = b;
}
void copy2(int *c, int *d) {
    c = d;
}
void copy3(int *e, int *f) {
    *e = *f;
}
int main() {
    int q = 1;
    int r = 2;
    copy1(q, r);
    int s = 3;
    int t = 4;
    copy2(&s, &t);
    int u = 5;
    int v = 6;
    copy3(&u, &v);
    printf("%d %d %d %d %d %d\n", q, r, s, t, u, v);
}
```

## Extra practice
Q6: _Write a function called `transfer` that takes two integer pointers and an amount to transfer and moves the specified amount from one integer to the other._