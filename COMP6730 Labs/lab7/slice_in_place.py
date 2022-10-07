def slice_in_place(a_list, start, end):
    if end < start < 0:
        start, end = len(a_list) - abs(end) + 1, len(a_list) - abs(start) + 1
    print(start, end)
    del a_list[:start]
    del a_list[end-start:]
    


my_list = [1, 2, 3, 4]
slice_in_place(my_list, -2, -3)
print(my_list)
