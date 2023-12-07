def common_elements(set_1, set_2):
    set = set()
    for element in set_1:
        if element in set_2:
            set.add(element)
    return set