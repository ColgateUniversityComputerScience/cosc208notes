# Program memory: malloc
_COSC 208, Introduction to Computer Systems, 2021-09-27_

## Announcements
* Project 1 Part B (and revisions to Part A) due Thursday at 11pm

## No warm-up — Happy Monday!

## Pointers as return values
```C
int *one() {
    int x = 1;
    int *p = &x;
    return p;
}
int main() {
    int *q = one();
    printf("%d\n", *q);
}
```  

## malloc
Q2: _Write a function called `duplicate` that takes a string (i.e., an array of `char`) as a parameter and returns a copy of that string stored on the heap._
```C













```

Q3: _Write a function called `range` that behaves similar to the `range` function in Python. Your function should take an unsigned integer (`length`) as a parameter, and return a dynamically allocated array with `length` unsigned integers. The array should be populated with the values 0 through `length-1`._
```C














```

Q4: _Write a function called `generate_password` that takes an unsigned integer (`length`) as a parameter, and returns a dynamically allocated array of with `length` randomly selected characters (e.g., uppercase letters, lowercase letters, digits, symbols). Your function should use the `rand()` function from the C standard library, which returns a pseudo-random integer in the range 0 to `RAND_MAX`._
```C














```

## Extra practice
Q5: _Write a function called `substring` that takes a string, a starting index, and a length, and returns a substring. If the starting index is too large, the function should return `NULL`. If the length is too large, the function should return a shorter substring._
```C

















```

Q6: _Write a function called `lengths` that takes an array of strings and the number of elements in the array and returns an array of integers containing the length of each string._