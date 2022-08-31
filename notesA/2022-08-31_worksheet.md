# C: output; control structures; functions
_COSC 208, Introduction to Computer Systems, 2022-08-31_

## Announcements
* Before next class: read _Dive Into Systems_ 1.4.1, 2.9.5-2.9.6 and answer pre-class questions
* First lab today or tomorrow
* DEI assignment 1 due Thurs, Sept 8 @ 11pm

## Outline
* Warm-up
* Learning community guidelines
* Output
* Control structures
* Defining functions

## Warm-up
Q1: _Write a program that prints the number of days, hours, and minutes in a week._
```C






```

🛑 Stop here after completing the warm-up; if you have extra time please **skip ahead** to the extra practice.

## Learning community guidelines
1. We will attempt to overcome fears of exposing our preconceptions and misunderstandings by openly answering and asking questions.
2. We will not demean, devalue, or "put down" people for their questions or contributions.
3. We will be actively aware of our "airtime": if we tend to be quieter, we pledge to lean in and contribute more; if we tend to dominate conversations, we pledge to lean out and listen more.

## Output
Q2: _Assume the variables `year`, `month` and `day` contain the parts of a date. Use `printf` to output the data (e.g., `2022-1-26`)_

<div style="height:5em;"></div>

Q3: _Assume the variables `length` and `width` contain the dimensions of a sports field/court. Use `printf` to output the dimensions (`94ft x 50ft`)_

<div style="height:5em;"></div>

Q4: _Assume the variables `first` and `last` contain a patient's first and last initial, and the variables `systolic` and `diastolic` contain the patient's blood pressure readings. Use `printf` to output the patient's initials and blood pressure (e.g., `A.G. 115/70`)_

🛑 Stop here after completing the above questions; if you have extra time please **skip ahead** to the extra practice.

## Control structures
Q5: _Write a program that flips a coin: call `random()` to generate a random number, and print `heads` if the number is even and `tails` if the number is odd._
```C











```
Q6: _Write a program that prints all even numbers from 1 to 100 using a for loop._
```C







```
Q7: _Write the same program using a while loop._
```C








```

🛑 Stop here after completing the above questions; if you have extra time please **skip ahead** to the extra practice.

<div style="page-break-after:always;"></div>

## Functions
Q8: _Write a function called `isletter` that takes a character and returns `1` if the character is a letter, or `0` otherwise._
```C












```

## Extra practice
Q9: _Write a program that prints out the powers of 2 from 2 through 2048._
```C












```

<div style="page-break-after:always;"></div>

Q10: _Write a program that prints all numbers from 1 to 100, except:_
* _If the number is divisible by 3 then print `Three`_
* _If the number is divisible by 5 then print `Five`_
* _If the number is divisible by 3 and 5, print `Both`_

```C




















```

Q11: _Write a program that prints every letter of the alphabet in upper and lower case: `AaBbCcDd...YyZz`_
```C












```

Q12: _Write a function called `floorm` that takes two integers and rounds down the first integer to the closest multiple of the second integer._