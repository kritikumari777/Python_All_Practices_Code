def add(x, y):
    return x + y


def do_twice(fun, x, y):
    return fun(fun(x, y), fun(x, y))


print(do_twice(add, 5, 10))