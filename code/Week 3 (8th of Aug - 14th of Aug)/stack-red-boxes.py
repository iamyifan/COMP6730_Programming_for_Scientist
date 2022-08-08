"""
A program to demonstrate branching - will stack 2 red boxes out of 3 - regardless of position
"""

import robot
import random


def drive_right_twice():
    """
    Moves the robot two spaces to the right.
    Assumes nothing is in the way or the gripper is folder.
    """

    robot.drive_right()
    robot.drive_right()


def drive_left_twice():
    """
    Moves the robot two spaces to the left
    Assumes nothing is in the way or the gripper is folder.
    """

    robot.drive_left()
    robot.drive_left()


def pickup_box():
    """
    Gets the robot to pick up a box in front of it.
    Assumes gripper is open or gripper is folded and nothing is right or left.
    """

    robot.lift_up()
    robot.gripper_to_open()
    robot.lift_down()
    robot.gripper_to_closed()
    robot.lift_up()


def finish():
    """
    Sets gripper to folder and returns robot to ground level.
    """
    robot.gripper_to_folded()
    robot.lift_down()


def stack_red_boxes():
    """
    Stacks two red boxes on top of each other.
    Assumes the boxes are evenly spaced on a width 5 bench.
    Assumes two boxes are red and the third is not.
    Assumes robot is in the starting position.
    """

    # Check the first box
    if robot.sense_color() == "red":
        drive_right_twice()

        # Check the second box
        if robot.sense_color() == "red":
            # stack middle box on left
            robot.drive_right()
            pickup_box()
            drive_left_twice()
            finish()

        # If the second box was not red, we want 1st and 3rd box
        else:
            # stack left box on right
            robot.drive_left()
            pickup_box()
            drive_right_twice()
            drive_right_twice()
            finish()

    # If the first box was not red, we want 2nd and 3rd box
    else:
        # stack middle box on right
        robot.drive_right()
        drive_right_twice()
        pickup_box()
        drive_right_twice()
        finish()


# Randomise the arrangement of the boxes
box_colours = ["red", "red", "black"]
random.shuffle(box_colours)

# Setup the robot
robot.init(height=3, boxes=[[box_colours[0]], [], [box_colours[1]], [], [box_colours[2]]])

# Check it works
stack_red_boxes()
