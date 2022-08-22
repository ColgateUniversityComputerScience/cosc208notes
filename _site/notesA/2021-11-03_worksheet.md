# Efficiency: caching (continued); Multiprocessing: operating systems; limited direct execution; system calls
_COSC 208, Introduction to Computer Systems, 2021-11-03_

## Announcements
* Project 2 Part B due date extended to Tues, Nov 9

## Outline
* Warm-up
* Cache replacement
* OS overview
* Accessing hardware
* Limited direct execution
* System calls

## Warm-up
Q1: _For each of the following instances of caching, indicate whether the caching is motivated by temporal or spatial locality._
* A CPU caches the first 32 instructions of a function when the function is called
* A CPU caches all of the instructions for a frequently called function
* A web browser caches the Moodle pages for your courses, which you view multiple times per week
* A content distribution network (CDN) caches a video that has gone viral
* A content distribution network (CDN) caches "recommended videos" related to a popular video

🛑 **STOP HERE** after completing the above question; if you have extra time take a few deep breaths to help reduce stress.

## Cache replacement
_Assume a cache can hold 3 entries and the following 15 data accesses occur: 3, 4, 4, 5, 3, 2, 3, 4, 1, 4, 4, 2, 5, 2, 4. Assuming the cache is initially empty, what is the hit ratio for each of the following algorithms?_
* _Optimal_
    ```




    ```
* Q2: _FIFO_
    ```




    ```
* Q3: _LRU_
    ```




    ```
* Q4: _LFU_