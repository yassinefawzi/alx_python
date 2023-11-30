def is_prime(number):
    if number <= 1:
        print(False)
    for i in range(2, number):
        if number % i == 0:
            print(False)
    print(True)