
# Example from Lecture 1 in week 3: robot to count how many boxes
# are in a stack. This is the recursive solution.

import robot

def count_boxes():
    if robot.sense_color() == '':
        # If there is no box in front of the sensor, the number is zero
        print("There is no box here: returning 0")
        return 0
    else:
        # otherwise, the number is 1 + the number returned by counting
        # the boxes from one level up.
        color = robot.sense_color()
        print("I'm looking at a", color, "box")
        robot.lift_up()
        num_above = count_boxes()
        robot.lift_down()
        print("There are", num_above, "boxes above the", color, "box")
        return 1 + num_above

# Try with different stack sizes:

robot.init(height = 5, boxes = [["blue", "green", "yellow", "red"]])
#robot.init(height = 6, boxes = [["black", "yellow", "red", "white", "blue"]])
#robot.init(height = 7, boxes = "random")

print("There are", count_boxes(), "boxes")
