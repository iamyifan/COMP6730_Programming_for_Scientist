def count_negative(sequence):
    count = 0
    for i in range(len(sequence)):
        if sequence[i] < 0:
            count += 1
    return count


print(count_negative([-1, 2, -3, 5]))    
