
## Example solution to the three box swapping problems in Lab 1.
## This is for the simpler version of the problem, where we assume
## that we can move a stack with more than one box at a time.
## To test all three swaps, just run the function test_swaps().

import robot

def swap_left_and_middle():
    '''Swap left and middle boxes. The robot is assumed to start in
    the left-most position.'''
    robot.drive_right() # move gripper to first stack
    position_to_grasp()
    swap_to_the_right()

def swap_middle_and_right():
    '''Swap middle and right boxes. The robot is assumed to start in
    the left-most position.'''
    robot.drive_right() # move gripper to first stack
    next_stack_right()
    position_to_grasp()
    swap_to_the_right()

def swap_left_and_right():
    '''Swap left and right boxes. The robot is assumed to start in
    the left-most position.'''
    robot.drive_right() # move gripper to first stack
    position_to_grasp()
    swap_to_the_right()
    swap_to_the_right()
    robot.lift_up()
    next_stack_left()
    next_stack_left()
    robot.lift_down()
    swap_to_the_right()

def test_swaps():
    '''Testing function for all three swaps.'''
    print("testing swap left and middle...")
    robot.init(boxes = [['red'], [], ['white'], [], ['blue']])
    swap_left_and_middle()
    print("testing swap middle and right...")
    robot.init(boxes = [['green'], [], ['yellow'], [], ['red']])
    swap_middle_and_right()
    print("testing swap left and right...")
    robot.init(boxes = [['brown'], [], ['green'], [], ['black']])
    swap_left_and_right()


def next_stack_right():
    robot.drive_right()
    robot.drive_right()

def next_stack_left():
    robot.drive_left()
    robot.drive_left()

def swap_to_the_right():
    '''Swap one box with the one next to it on the right.
    Assumption: The gripper is in front of the box to be moved right,
    in open position, and the lift is down; there is a box to the
    right to swap with.
    Note that the robot ends in the same config (lift down, gripper
    open) in front of the box that was moved right in its new position.
    '''
    # the swap is done by picking up the box
    robot.gripper_to_closed()
    robot.lift_up()
    # ...moving it on top of the box to the right
    next_stack_right()
    # ...grasping the tower of both boxes and moving it to the left
    robot.gripper_to_open()
    robot.lift_down()
    robot.gripper_to_closed()
    next_stack_left()
    # ...then picking up the box on top and moving it right
    robot.gripper_to_open()
    robot.lift_up()
    robot.gripper_to_closed()
    next_stack_right()
    robot.lift_down()
    robot.gripper_to_open()

def position_to_grasp():
    '''Position the gripper to grasp a box on the table.
    Assumption: The gripper is in front of the box and folded, and
    the lift is down. Surrounding stacks have no more than one box.'''
    robot.lift_up()
    robot.gripper_to_open()
    robot.lift_down()
