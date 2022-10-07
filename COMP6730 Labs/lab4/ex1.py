def sum_odd_digits(number):
    dsum = 0
    while number != 0:
        if number % 2 == 1:
            dsum += number - (number // 10) * 10
        number //= 10
    return dsum


def sum_even_digits(number):
    m = 1
    dsum = 0
    while number % (10 ** m) != number:
        digit = (number % (10 ** m)) // (10 ** (m - 1))
        if digit % 2 == 0:
            dsum += digit
        m += 1
    return dsum


print(sum_odd_digits(1282736))
print(sum_even_digits(1282736))
