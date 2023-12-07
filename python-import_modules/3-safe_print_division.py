def safe_print_division(a, b):
    try:
        out = a / b
    except ZeroDivisionError:
        out = None
    finally:
        print("Inside result: {}".format(out))
        print("{} / {} = {}".format(a, b, out))
        return out