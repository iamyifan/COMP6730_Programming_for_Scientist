
distance_AB = 40

# All angles are in degrees:
alpha = 30
beta = 60
gamma = 60
delta = 60
epsilon = 70
phi = 40

# Import math module because we need sine and square root functions.

import math

# Use triangulation formula to compute distance B-C
distance_BC = distance_AB * (math.sin(math.radians(alpha)) /
                             math.sin(math.radians(alpha + beta)))

print("the distance between B and C is", distance_BC)

# The B-C-D triangle is equilateral, so distance C-D is the same
# as distance B-C; we give it a new name to make the code easier
# to read.
distance_CD = distance_BC

# Use triangulation formula to compute distance C-E, using C-D as the
# baseline
distance_CE = distance_CD * (math.sin(math.radians(phi)) /
                             math.sin(math.radians(epsilon + phi)))

print("the distance between C and E is", distance_CE)

# To test the accuracy of our calculation, we can use a different
# method to compute a known quantity - in this case, the length of
# the original baseline, A-B.

# Use triangulation to compute distance A-C
distance_AC = distance_AB * (math.sin(math.radians(beta)) /
                             math.sin(math.radians(alpha + beta)))

# Use Pythagoras' formula to compute the length of A-B:
calc_AB = math.sqrt((distance_AC ** 2) + (distance_BC ** 2))

# If the calculated distance is (nearly) the same as the original
# A-B distance, we can have more confidence that our calculations
# are correct.
print("the calculated distance A-B is", calc_AB)
