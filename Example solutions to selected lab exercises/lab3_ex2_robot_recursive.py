# comp1730, lab3.
# An example answer to exercise 2.2
# Malcolm M, 18/3/2022.

import robot

def find_recursive(colour):
    '''
    base cases:
        return -1 if not found,
        return 0 if found at this level
    else:
        go up and try at the next level
        on the way home:
            put the lift down one level
            if -1 was returned (box not found)
                propagate that all the way home
            else
                return the (returned) level number plus one for this level.
    '''
    if robot.sense_color() == '':
        return -1
    elif robot.sense_color() == colour:
        return 0
    else:
        robot.lift_up()
        level = find_recursive(colour)
        robot.lift_down()
        if level == -1: # box not found
            return -1
        else:
            return level + 1


# A little interface to exercise the find_recursive function.
def find_box_recursive(colour):
    if colour == '':
        print("find() needs a box colour to look for")
    else:
        level = find_recursive(colour)
        if level == -1:
            print("There is no",colour,"box here")
        else:
            print("The",colour,"box is at level",level+1)


# Some testing ...
robot.init(height = 5, boxes = [["black", "blue", "white", "red"]])

find_box_recursive("black")
find_box_recursive("blue")
find_box_recursive("red")
find_box_recursive("green")
find_box_recursive("") # why test this case?
