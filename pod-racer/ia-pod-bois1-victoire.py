import sys
import math

# To debug: print("Debug messages...", file=sys.stderr, flush=True)

cruise_speed = 100
mininal_turn_speed = 10
overturn_angle = 45

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


def calculate_speed(distance, angle):
    if distance <= 4000 and abs(angle) > 45:
        return int(cruise_speed * 0.60)

    # if distance <= 2500:
    #     return int(((distance/2500) * (100 - mininal_turn_speed)) + mininal_turn_speed)
    else:
        return cruise_speed


# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [
        int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    speed = calculate_speed(next_checkpoint_dist, next_checkpoint_angle)
    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    print(str(next_checkpoint_x) + " " +
          str(next_checkpoint_y) + " " + str(speed))
