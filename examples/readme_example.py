#!/usr/bin/env python3

import rill


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


rill.inp().grep("rill").line_lengths().map_lines(fib).show()
