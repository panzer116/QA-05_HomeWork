def sum_it(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def prod(x, y):
    return x * y


def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Don't division by 0!!!")


def my_calc(x, y, sign):
    if sign == '+':
        return sum_it(x, y)
    elif sign == '-':
        return subtraction(x, y)
    elif sign == '*':
        return prod(x, y)
    elif sign == '-':
        return div(x, y)
