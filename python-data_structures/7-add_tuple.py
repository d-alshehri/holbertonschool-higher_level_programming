#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    a = list(tuple_a)
    b = list(tuple_b)

    if len(a) < 2:
        a.extend([0]*(2-len(a)))
    if len(b) < 2:
        b.extend([0]*(2-len(b))

    sumA = a[0] + b[0]
    sumB = a[1] + b[1]

    return (sumA, sumB)
