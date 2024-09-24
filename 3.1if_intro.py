robot_location = 30
ball_location = 35
goal_location = 20
have_ball = False

# If the ball location is greater than robot location, then print the statement below
if robot_location < ball_location:
    print("Almost at the ball")
#If the robot location is greater than goal location, then print the statement below
if robot_location > goal_location:
    print("You are beyond the goal.")
#If the robot location is equal to goal location, then print the statement below
if robot_location == goal_location:
    print("The robot is at the goal.")

robot_location += 5

#If the robot location is equal to goal location, then print the statement below
if robot_location == goal_location:
    print("At the goal.")
#if robot location is equal to ball location, print the follow statements and change have_ball to "True"
if robot_location == ball_location:
    print("At the ball")
    print("Picking up the ball.")
    have_ball = True
    print("Now make your way to the goal.")

robot_location -= 15

#If goal location is greater than robot location, then print the statement bellow
if robot_location < goal_location:
    print("You went too far.")

#If the robot location is equal to goal location, and have_ball is true, then print the statement as well as change have_ball to false
if robot_location == goal_location and have_ball is True:
    print("You scored a goal!")
    have_ball = False
#2)
#Indentation in the if statement shows which code belongs to the if block.
#   Any code that is indented after the if condition is part of the block, and if the condition is true, 
#   that indented code will be executed.

#3)
# += adds a value to the variable and assigns the result back to the variable.
# -= subtracts the value to the variable and assigns the result back to the variable