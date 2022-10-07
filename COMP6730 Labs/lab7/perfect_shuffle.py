def perfect_shuffle(a_list):
    # not modify the argument list
    res = [None for _ in range(len(a_list))]
    mid = len(a_list) // 2
    part_a = a_list[:mid]
    part_b = a_list[mid:]
    for i in range(mid):
        res[i * 2] = part_a[i]
        res[i * 2 + 1] = part_b[i]
    if len(part_b) > mid:
        res[-1] = part_b[-1]
    return res


my_list = [1, 2, 3, 4, 5, 6, 7]
print(perfect_shuffle(my_list))
print(my_list)
