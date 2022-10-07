def find_element(sequence, element):
    i = 0
    while i < len(sequence) and sequence[i] != element:
        i = i + 1
    return i


print(find_element([3, 2, 1, 4], 5))
