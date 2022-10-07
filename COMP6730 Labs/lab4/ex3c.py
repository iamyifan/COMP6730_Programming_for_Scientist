def most_average(numbers):
    avg = sum(numbers) / len(numbers)
    res = None
    diff = float("inf")
    for i in range(len(numbers)):
        diff_curr = abs(numbers[i] - avg)
        if diff_curr < diff:
            diff = diff_curr
            res = numbers[i]
    return res


print(most_average([3, 4, 3, 1]))
