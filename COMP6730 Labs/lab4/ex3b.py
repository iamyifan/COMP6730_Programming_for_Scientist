def is_increasing(a_list):
    if len(a_list) == 0:
        return True
    i = 0
    while i < len(a_list) - 1 and a_list[i] <= a_list[i + 1]:
        i += 1

    return i == len(a_list) - 1


print(is_increasing([]))
