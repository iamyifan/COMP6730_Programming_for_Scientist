
distance_AB = 40

# All angles are in degrees:
alpha = 30
beta = 60
gamma = 60
delta = 60
epsilon = 70
phi = 40

# Import math module because we need sine and square root functions,
# and also the constant pi.

import math

def deg_to_rad(angle):
    '''Argument `angle` is an angle in degrees.
    Returns the angle in radians.'''
    return (angle / 180) * math.pi

def sin_of_deg(angle):
    '''Returns the sine of an angle given in degrees.'''
    return math.sin(deg_to_rad(angle))

def triangulate(baseline, adj_angle, opp_angle):
    '''Calculate the length of one side of a triangle using the
    triangulation formula. The arguments are:
    baseline : the length of the baseline
    adj_angle : the angle between the side being calculated and the baseline
    opp_angle : angle between the third side and the baseline.
    The function returns the length of the side.
    '''
    return baseline * (sin_of_deg(opp_angle) /
                       sin_of_deg(adj_angle + opp_angle))

# Use triangulation formula to compute distance B-C
distance_BC = triangulate(distance_AB, beta, alpha)

print("the distance between B and C is", distance_BC)

# The B-C-D triangle is equilateral, so distance C-D is the same
# as distance B-C; we give it a new name to make the code easier
# to read.
distance_CD = distance_BC

# Use triangulation formula to compute distance C-E, using C-D as the
# baseline
distance_CE = triangulate(distance_CD, epsilon, phi)

print("the distance between C and E is", distance_CE)

# To test the accuracy of our calculation, we can use a different
# method to compute a known quantity - in this case, the length of
# the original baseline, A-B.

# Use triangulation to compute distance A-C
distance_AC = triangulate(distance_AB, alpha, beta)

# Use Pythagoras' formula to compute the length of A-B:
calc_AB = math.sqrt((distance_AC ** 2) + (distance_BC ** 2))

# If the calculated distance is (nearly) the same as the original
# A-B distance, we can have more confidence that our calculations
# are correct.
print("the calculated distance AB is", calc_AB)
