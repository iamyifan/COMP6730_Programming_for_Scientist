row1 = ['H', 'He']
row2 = ['Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ar']
row3 = ['Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ne']
ptable = row1
ptable.extend(row2)
ptable.extend(row3)

print(ptable)
print(row1)

row2[-1] = 'Ne'
print(row2)
ptable[-1] = 'Ar'
print(row3)

print(id(row1), id(row2), id(row3), id(ptable))
