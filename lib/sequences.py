#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = [0, 1]
    index = 2
    if length == 0:
        fibonacci.clear()
    elif length == 1:
        fibonacci.pop(1)
    else:
        while index < length:
            next_value = fibonacci[index - 2] + fibonacci[index - 1]
            fibonacci.append(next_value)
            index += 1
    print(fibonacci)
    return fibonacci