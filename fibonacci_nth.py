def fibonacci_nth(n):
    a, b, c, j = 1, 1, 0, 2
    while j < n:
        c = a
        a = a + b
        b = c
        j += 1
    return a