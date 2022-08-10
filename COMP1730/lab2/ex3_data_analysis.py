canberra_population = 196037
canberra_families = 50352  
# 22850 are a couple with one or more children
# 7243 are a single parent with one or more children
# the rest are without children, which consist of two (adult) people
# the average number of children is 1.8 / family, this is the average
# over the families that have children only

# how many single adults (not children) there are in canberra
families_couple = 22850
families_single = 7243
families_without_children = canberra_families - families_couple - families_single
families_have_children = families_couple + families_single

n_children_in_families = 1.8 * families_have_children
n_adults_in_families = families_couple * 2 + families_single * 1 + families_without_children * 2
n_families = n_children_in_families + n_adults_in_families

n_single_adults = canberra_population - n_families
print("there are {} single adults (not children) in Canberra".format(int(n_single_adults)))
