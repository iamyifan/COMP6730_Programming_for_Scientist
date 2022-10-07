# coding: utf-8
## COMP1730/6730 S2 2022 - Homework 5
# Submission is due 09:00am, Monday the 3rd of October, 2022.

## YOUR ANU ID: u7351505
## YOUR NAME: Yifan Luo

## You should implement one function stock_trade; you may define
## more functions if this will help you to achieve the functional
## correctness, and to improve the code quality of you program

from math import dist, cos, sin, atan2


def advance_position(r, v):
    '''from the current position r advance to the position
    at the next iteration: r -> r + v
    (maybe I do not need this function?)
    '''
    return (r[0] + v[0], r[1] + v[1]) 


def check_contact(r1, r2, tol):
    ''' returns True if points r1 and r2 are withing tol distance from each other'''
    return dist(r1, r2) < tol


def get_chaser_direction(chaser_pos, target_pos):
    """
    return direction of next chaser move based on its current position,
    and position of the target (all positions are x, y tuples)
    """
    chaser_x, chaser_y = chaser_pos
    target_x, target_y = target_pos
    delta_x = target_x - chaser_x
    delta_y = target_y - chaser_y
    angle = atan2(delta_y, delta_x)
    return (cos(angle), sin(angle))

def chaser_crossed_target(chaser_pos, next_chaser_pos,
                          target_pos, next_target_pos):
    '''
    return True if chaser and target paths cross
    Assumes the target will only travel in a horizontal direction
    '''
    Ax1, Ay1 = chaser_pos
    Ax2, Ay2 = next_chaser_pos
    Bx1, By1 = target_pos
    Bx2, By2 = next_target_pos    

    assert By1 == By2, \
            "chaser_crossed_target: target must travel in a horizontal direction"
            
    if Ax1 == Ax2: #vertical
        if Bx1 > Bx2:  Bx1, Bx2 = Bx2, Bx1
        return Bx1 <= Ax1 <= Bx2

    if Ay1 == Ay2: #horizontal
        if Ay1 != By1:
            return False
        else:
            if Ax1 > Ax2:  Ax1, Ax2 = Ax2, Ax1
            if Bx1 > Bx2:  Bx1, Bx2 = Bx2, Bx1
            return min(Ax2, Bx2) >= max(Ax1, Bx1)

    m = (Ay2 - Ay1) / (Ax2 - Ax1)
    c = Ay1 - m * Ax1
    x = (By1 - c) / m       
    if Ax1 > Ax2:  Ax1, Ax2 = Ax2, Ax1
    if Bx1 > Bx2:  Bx1, Bx2 = Bx2, Bx1
    return (Ax1 <= x <= Ax2) and (Bx1 <= x <= Bx2)


def chase(target_speed, chaser_speed, chaser_pos, max_steps, catching_dist=1e-5):
    '''
    Given the direction and speed of the hare, the distance between it and the hound,
    and the speed of the hound, check whether the hound will be able to catch the hare
    in a specified amount of time.

    Parameters:
        target_speed (float): the target's speed in metres per time step
        chaser_speed (float): the chaser's speed in metres per time step
        chaser_pos (tuple): the (x, y) position of the chaser at the start of the chase
        max_steps (int): the maximum number of time steps during which the chaser is able to
            pursue the target; the pursuit may terminate earlier if the target is captured
        catching_dist (float): the distance which determines whether the chaser has caught the
            target - if the separation between the two becomes smaller than catching_dist, then
            the chase is successful

    Return:
        A boolean value indicating success (True) or failure (False) of the chase with the max_steps.
    '''
    assert type(target_speed) in [int, float], "target's speed must be numeric"
    assert type(chaser_speed) in [int, float], "chaser's speed must be numeric"
    assert type(chaser_pos) == tuple, "chaser's initial position must be a tuple"
    assert len(chaser_pos) == 2, "chaser's position has the form (x, y)"
    assert type(chaser_pos[0]) in [int, float] and type(chaser_pos[1]) in [int, float], \
        "(x, y) must be a valid numeric tuple"
    assert type(max_steps) == int, "the number of max steps must be numeric"
    assert max_steps >= 0, "the number of max steps must be non-negative"
    assert type(catching_dist) in [int, float], "the catching distance must be numeric"
    assert catching_dist >= 0, "the catching distance must be non-negative"

    # only the absolute speed values matter
    target_speed = abs(target_speed)
    chaser_speed = abs(chaser_speed)

    target_pos = (0, 0)  # start position of the target
    # check whether the chaser and the target are close enough at the beginning
    if check_contact(target_pos, chaser_pos, catching_dist):
        return True

    # check whether the chaser will catch the target during the chasing within max_steps
    for _ in range(max_steps):
        # calculate the target's and the chaser's next positions after one time step
        target_next_pos = advance_position(target_pos, (target_speed, 0))  # only calculate x-axis speed for the target
        chaser_next_dir = get_chaser_direction(chaser_pos, target_next_pos)
        chaser_speed_x = chaser_next_dir[0] * chaser_speed  # x-axis speed for the chaser
        chaser_speed_y = chaser_next_dir[1] * chaser_speed  # y-axis speed for the chaser
        chaser_next_pos = advance_position(chaser_pos, (chaser_speed_x, chaser_speed_y))
        target_next_pos = (round(target_next_pos[0]), round(target_next_pos[1]))
        chaser_next_pos = (round(chaser_next_pos[0]), round(chaser_next_pos[1]))
        # check whether the target are caught during the "on-the-fly" catch
        if chaser_crossed_target(chaser_pos, chaser_next_pos, target_pos, target_next_pos):
            return True
        # check whether the target and the chaser are close enough after one time step
        if check_contact(target_next_pos, chaser_next_pos, catching_dist):
            return True
        # update the target's and the chaser's positions after one time step
        target_pos = target_next_pos
        chaser_pos = chaser_next_pos
    return False  # the chaser can't catch the target during the chasing within max_steps


# print(chase(target_speed=3, chaser_speed=5, chaser_pos=(0, 4), max_steps=1000, catching_dist=0))

def test_chase_1():
    # generic cases (low precision, should work even if no "catch-on-the-fly" check is used)
    assert not chase(100,10,(10,10),100)
    assert chase(10,11,(10,10),20, catching_dist=0.5)
    assert chase(1.0,1.1,(10,10),50, catching_dist=0.1)
    assert not chase(100,10,(10,10),100)
    print('All tests 1 passed')


def test_chase_2():
    # degenerate (boundary, corner) cases
    assert not chase(10, 5, (5,5), 100) # slow chaser too far from the line -- never catches
    assert chase(5, 10, (-10,0), 20) # fast chaser behind target -- will catch given enough steps
    assert not chase(5, 6, (-10,0), 4) # fast chaser behind target -- won't catch since not enough steps
    assert chase(5, 6, (-10,0), 10) # fast chaser behind target -- will catch at the very end
    print('All tests 2 passed')

