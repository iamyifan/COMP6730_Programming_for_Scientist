def any_one_is_sum_1(a, b, c):
    sum_c = a + b
    sum_b = a + c
    sum_a = b + c
    if sum_c == c:
        return True
    if sum_b == b:
        return True
    if sum_a == a:
        return True
    return False


def any_one_is_sum_2(a, b, c):
    if b + c == a:
        return True
    if c + a == b:
        return True
    if a + b == c:
        return True
    return False


def any_one_is_sum_3(a, b, c):
    if a + b == c or a + c == b or b + c == a:
        return True
    return False
