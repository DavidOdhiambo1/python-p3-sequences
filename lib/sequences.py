#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_list = []
    for i in range(length):
        if i == 0:
            fibonacci_list.append(0)
        elif i == 1:
            fibonacci_list.append(1)
        else:
            fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2])
    print(fibonacci_list)
   