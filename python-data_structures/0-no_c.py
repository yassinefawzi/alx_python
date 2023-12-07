def no_c(my_string):
    out = ""
    for i in my_string:
        if i not in {'c', 'C'}:
            out += i
    return out