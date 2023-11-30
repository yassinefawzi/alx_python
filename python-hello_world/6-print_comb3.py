for num in range(10):
    for snum in range(num + 1, 10):
        if num < 8:
            print('{:02}'.format(num * 10 + snum), end=", ")
        else:
            print('{:02}'.format(num * 10 + snum))