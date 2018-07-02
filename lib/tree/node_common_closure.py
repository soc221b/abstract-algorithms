def self_closure(value):
    return value


def left_setter_closure(n, x):
    n.left = x


def left_closure(n):
    return n.left


def right_setter_closure(n, x):
    n.right = x


def right_closure(n):
    return n.right


def less_closure(a, b):
    return a.value < b.value
