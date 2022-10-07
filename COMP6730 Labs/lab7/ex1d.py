row2 = ['Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ar']
ptable1 = ['H', 'Xe', row2]

import copy
ptable2 = copy.deepcopy(ptable1)

ptable2[-1][-1] = 'Ne'
print(ptable1, ptable2, row2)
