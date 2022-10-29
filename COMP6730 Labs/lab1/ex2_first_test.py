# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 14:19:01 2022

@author: yifan luo
@uid: u7351505
"""


import robot


def get_drive_pos():
    """ Get the current drive position.
    @param: none
    @return: the current drive position
    """
    if robot._robot is None:
        raise robot.RobotError("The robot has not been initialised.")
    return robot._robot.drive_pos


def update_sense_pos():
    """ Update the sence position after each move.
    @param: none
    @return: none
    """
    if robot._robot is None:
        raise robot.RobotError("The robot has not been initialised.")
    robot._robot.sense_pos = robot._robot.drive_pos + 1


def get_sense_pos():
    """ Get the current sense postion.
    @param: none
    @return: the current sense position
    """
    if robot._robot is None:
        raise robot.RobotError("The robot has not been initialised.")
    return robot._robot.drive_pos + 1  # the sense is on the right side of the drive


def get_lift_pos():
    """ Get the current lift position. 0 = ground, 1 = level 1, 2 = level 2, etc.
    @param: none
    @return: the current lift position
    """
    if robot._robot is None:
        raise robot.RobotError("The robot has not been initialised.")
    return robot._robot.lift_pos


def get_gripper_state():
    """ Get the current gripper state. < 0 = folded, 0 = open, > 0 = closed
    @param: none
    @return: the current gripper state
    """
    if robot._robot is None:
        raise robot.RobotError("The robot has not been initialised.")
    return robot._robot.gripper_state


def drive_n_right(n=1):
    """ Drive the robot n steps right.
    @param n: int, drive n steps right
    @return: none
    """
    if robot._robot is None:
        raise robot.RobotError("The robot has not been initialised.")
    if n <= 0:
        raise robot.RobotError("The n must be a positive integer.")
    for i in range(n):
        robot.drive_right()
    update_sense_pos()  # update the sense position after each n steps move


def drive_n_left(n=1):
    """ Drive the robot n steps left.
    @param n: int, drive n steps left
    @return: none
    """
    if robot._robot is None:
        raise robot.RobotError("The robot has not been initialised.")
    if n <= 0:
        raise robot.RobotError("The n must be a positive integer.")
    for i in range(n):
        robot.drive_left()
    update_sense_pos()  # update the sense position after each n steps move


def pick_up_and_lift_up():
    """ Pick up a box and lift it up.
    @param: none
    @return: none
    """
    if robot._robot is None:
        raise robot.RobotError("The robot has not been initialised.")
    if get_lift_pos() == 0:  # if the robot is on the groud
        robot._robot.lift_up()  # lift up first in case the gripper hits other boxes
    # pick a box up
    robot._robot.gripper_to_open()
    robot._robot.lift_down()
    # lift a box up
    robot._robot.gripper_to_closed()
    robot._robot.lift_up()


def swap_left_and_middle(left_pos=0, mid_pos=2, right_pos=4):
    """ Swap the left box and the middle box. (only one box can be carried each time)
    @param left_pos: int, the position of the left box, default position is 0
    @param mid_pos: int, the position of the middle box, default position is 2
    @param right_pos: int, the position of the right box, default position is 4
    @return: none
    """
    if robot._robot is None:
        raise robot.RobotError("The robot has not been initialised.")
    drive_pos = get_drive_pos()
    # move to the left box
    if drive_pos < left_pos:
        drive_n_right(left_pos - drive_pos)
    elif drive_pos > left_pos:
        drive_n_left(drive_pos - left_pos)
    #  put the left box on the top of the right box
    pick_up_and_lift_up()
    drive_n_right(right_pos - get_drive_pos())
    robot.gripper_to_folded()
    #  move to the middle box
    drive_n_left(get_drive_pos() - mid_pos + 1)
    robot.gripper_to_open()
    drive_n_right(1)
    #  put the middle box to the left
    pick_up_and_lift_up()
    drive_n_left(get_drive_pos() - left_pos)
    robot.lift_down()
    robot.gripper_to_folded()
    # move to the left box (on the top of the right box)
    robot.lift_up()
    drive_n_right(right_pos - get_drive_pos())
    #  put the left box to the middle
    robot.gripper_to_closed()
    drive_n_left(get_drive_pos() - mid_pos)
    robot.lift_down()
    robot.gripper_to_open()
    robot.lift_up()


def swap_middle_and_right(left_pos=0, mid_pos=2, right_pos=4):
    """ Swap the middle box and the right box. (only one box can be carried each time)
    @param left_pos: int, the position of the left box, default position is 0
    @param mid_pos: int, the position of the middle box, default position is 2
    @param right_pos: int, the position of the right box, default position is 4
    @return: none
    """
    if robot._robot is None:
        raise robot.RobotError("The robot has not been initialised.")
    drive_pos = get_drive_pos()
    # move to the middle box
    if drive_pos < mid_pos:
        drive_n_right(mid_pos - drive_pos)
    elif drive_pos > mid_pos:
        drive_n_left(drive_pos - mid_pos)
    #  put the middle box on the top of the left box
    pick_up_and_lift_up()
    drive_n_left(get_drive_pos() - left_pos)
    robot.gripper_to_folded()
    #  move to the right box
    drive_n_right(right_pos - get_drive_pos())
    robot.gripper_to_open()
    #  put the right box to the middle
    pick_up_and_lift_up()
    drive_n_left(get_drive_pos() - mid_pos)
    robot.lift_down()
    robot.gripper_to_open()
    # move to the right box (on the top of the left box)
    robot.lift_up()
    drive_n_right(1)
    robot.gripper_to_folded()
    drive_n_left(get_drive_pos() - left_pos)
    #  put the right box to the right
    robot.gripper_to_closed()
    drive_n_right(right_pos - get_drive_pos())
    robot.lift_down()
    robot.gripper_to_open()
    robot.lift_up()


def swap_left_and_right(left_pos=0, mid_pos=2, right_pos=4):
    """ Swap the left box and the right box. (only one box can be carried each time)
    @param left_pos: int, the position of the left box, default position is 0
    @param mid_pos: int, the position of the middle box, default position is 2
    @param right_pos: int, the position of the right box, default position is 4
    @return: none
    """
    if robot._robot is None:
        raise robot.RobotError("The robot has not been initialised.")
    swap_left_and_middle()
    swap_middle_and_right()
    swap_left_and_middle()
