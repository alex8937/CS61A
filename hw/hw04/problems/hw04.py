HW_SOURCE_FILE = 'hw04.py'

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    if n <= 3:
        return n
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    if n <= 3:
        return n
    gn_3, gn_2, gn_1 = 1, 2, 3
    for _ in range(4, n + 1):
        gn_1, gn_2, gn_3 = gn_1 + 2 * gn_2 + 3 * gn_3, gn_1, gn_2
    return gn_1


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """

    def help(index, cur, plus):
        if index == n:
            return cur + plus
        else:
            return help(index + 1, cur + plus, -plus if has_seven(index) or index % 7 == 0 else plus)

    return help(1, 0, 1)



def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    def count_change_upto(amount, max_value):
        if max_value == 1:
            return 1
        elif amount == 0:
            return 1
        elif amount < max_value:
            return count_change_upto(amount, max_value // 2)
        else:
            with_max_value = count_change_upto(amount - max_value, max_value)
            without_max_value = count_change_upto(amount, max_value // 2)
            return with_max_value + without_max_value
    return count_change_upto(amount, find_largest_beneath_pow_2(amount))

def find_largest_beneath_pow_2(n):
    ans = 1
    while ans * 2 <= n:
        ans *= 2
    return ans
###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return lambda: ((lambda fun, n : fun(fun, n))(lambda f , x: 1 if x == 0 else f(f, x - 1)))
