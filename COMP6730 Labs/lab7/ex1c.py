row2 = ['Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ar']
ptable1 = ['H', 'Xe', row2]
ptable2 = ptable1[:]  # shallow copy, different id at 

print(ptable1, ptable2)
print(id(ptable1), id(ptable2))
