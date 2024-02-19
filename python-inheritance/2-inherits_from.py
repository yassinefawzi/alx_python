"""defining our function"""
def inherits_from(obj, a_class):
    """return true of obj inherit directly or indirectly from a_class"""
    return isinstance(obj, a_class) and type(obj) != a_class