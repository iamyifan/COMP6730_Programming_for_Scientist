
## Exercise 3 in Lab 2: Analysis of the Canberra census data.

# The total population is 196,037 people (adults and children):
total_pop = 196037

# There are 50,352 families:
total_families = 50352

# Of the families, 22,850 are a couple with one or more children
couples_with_children = 22850

# and 7,243 are a single parent with one or more children.
single_parents = 7243

# The remaining families are couples without children:
couples_no_children = total_families - (couples_with_children + single_parents)

adults_in_families = (2 * couples_with_children) \
                     + (2 * couples_no_children) \
                     + single_parents

# The families that have children have on average 1.8 of them:
total_children = (couples_with_children + single_parents) * 1.8
print("total children:", total_children)

# The answer below is the number of single adults who do not have
# children; is that really what the question was asking for? Should
# we also count single adults with children? (if yes, how would you
# modify the output to get that answer?)

single_adults = total_pop - (adults_in_families + total_children)
print("single adults:", single_adults)
