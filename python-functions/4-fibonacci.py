def fibonacci_sequence(n):
    num = [0, 1]
    while len(num) < n:
            snum = num[-1] + num[-2]
            num = num + [snum]
    return (num[:n])