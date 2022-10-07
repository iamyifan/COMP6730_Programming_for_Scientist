
## Algorithm (a): search unsorted list for largest element <= x

def unsorted_find(x, ulist):
    best = min(ulist)
    for elem in ulist:
        if elem == x:
            return elem
        elif elem <= x:
            if elem > best:
                best = elem
    return best


## Algorithm (b): sort the list, then search the sorted list for the
## largest element <= x.

def sorted_find(x, slist):
    if slist[-1] <= x:
        return slist[-1]
    lower = 0
    upper = len(slist) - 1
    while (upper - lower) > 1:
        middle = (lower + upper) // 2
        if slist[middle] <= x:
            lower = middle
        else:
            upper = middle
    return slist[lower]


## A simple recursive algorithm for the subset sum problem:

def subset_sum(w, C):
    if len(w) == 0:
        return C == 0, []
    # including w[0]
    if w[0] <= C:
        can_do, subset = subset_sum(w[1:], C - w[0])
        if can_do:
            return True, [w[0]] + subset
    # excluding w[0]
    can_do, subset = subset_sum(w[1:], C)
    if can_do:
        return True, subset
    return False, None

## generate random lists of integers

import random
alist = [ random.randint(1,1000000) for i in range(200000*10) ]
alist = sorted(alist)

import time
start_time = time.time()
unsorted_find(500000, alist)
end_time = time.time()
print("Runtime for unsorted_find:", end_time - start_time, "seconds")

#slist = sorted(alist)
start_time = time.time()
sorted_find(500000, alist)
end_time = time.time()
print("Runtime for sorted_find:", end_time - start_time, "seconds")


#alist = random.sample(range(1,21), 10)

# Example from the lecture notes:
blist = [5, 2, 9, 1]
print("C = 16:", subset_sum(blist, 16))
print("C = 13:", subset_sum(blist, 13))
