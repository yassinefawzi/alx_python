import random
number = random.randint(-10000, 10000)
neg = 1
if number < 0:
    neg = -1
last_digit = abs(number) % 10 * neg
if last_digit == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, last_digit))
else:
    if last_digit > 5:
        print("Last digit of {:d} is {:d} and is greater than 5".format(number, last_digit))
    else:
        print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, last_digit))