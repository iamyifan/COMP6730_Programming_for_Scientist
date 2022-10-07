row1 = ['H', 'He']
row2 = ['Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ar']
row3 = ['Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ne']
ptable = [row1]
ptable.append(row2)
ptable.append(row3)

print(ptable[1][5], ptable[2][1])

row2[-1] = 'Ne'
print(ptable)
ptable[-1][-1] = 'Ar'
print(row3)

print(id(row1), id(row2), id(row3), id(ptable))
print(id(ptable[0]), id(row1))
print(id(ptable[1]), id(row2))
print(id(ptable[2]), id(row3))
