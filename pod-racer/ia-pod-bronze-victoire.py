import sys
import math

# To debug: print("Debug messages...", file=sys.stderr, flush=True)

update_counter = 0
checkpoint_counter = 0

cruise_speed = 100
mininal_turn_speed = 10
overturn_angle = 60
breaking_distance = 3000

last_checkpoint_x = 0
last_checkpoint_y = 0

boost_available = True

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def calculate_speed(distance, angle, boost):
    current_speed = cruise_speed

    if distance > 10000 and abs(angle) < 10 and boost:
        return 'BOOST'

    if distance <= 2000:
        current_speed *= 0.5

    if abs(angle) > overturn_angle:
        return int(current_speed * 0.5)
        
    # if distance <= breaking_distance:
    #     return int(((distance/breaking_distance) * (100 - mininal_turn_speed)) + mininal_turn_speed)
    else:
        return int(current_speed)


def is_checkpoint_new(checkpoint_x, checkpoint_y):
    if last_checkpoint_x != checkpoint_x or last_checkpoint_y != checkpoint_y:
        return True
    else:
        return False


# game loop
while True:
    print("START" + " " + str(update_counter), file=sys.stderr, flush=True)
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    if is_checkpoint_new(next_checkpoint_x, next_checkpoint_y):
        last_checkpoint_x = next_checkpoint_x
        last_checkpoint_y = next_checkpoint_y
        checkpoint_counter += 1
    
    print("CURRENT CHECKPOINT" + " " + str(checkpoint_counter), file=sys.stderr, flush=True)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    speed = calculate_speed(next_checkpoint_dist, next_checkpoint_angle, boost_available)

    if speed == 'BOOST':
        boost_available = False

    update_counter += 1

    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    # Once a round: "x y BOOST"
    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " +str(speed))
