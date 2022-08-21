import sys
import math

# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# CONSTANTS
CRUISE_SPEED = 100
MINIMAL_TURN_SPEED = 10
OVERTURN_ANGLE = 60
BREAKING_DISTANCE = 3000

# VARIABLES
update_counter = 0
checkpoint_counter = 0
last_checkpoint_x = 0
last_checkpoint_y = 0


def calculate_speed(distance, angle):
    """ Calcul de la vitesse du vaisseau en fonction de la distance
    et de l'angle.

    La distance est la distance en pixels qui sépare le vaisseau du prochain 
    checkpoint.
    L'angle est l'angle entre la trajectoire du vaisseau et la direction du 
    prochain checkpoint par rapport au vaisseau exprimé en degré.

    Elle renvoie la vitesse sous forme de integer.
    """
    current_speed = CRUISE_SPEED
    # if distance <= 4000 and abs(angle) > overturn_angle:
    if abs(angle) > OVERTURN_ANGLE:
        return int(current_speed * 0.40)

    # if distance <= breaking_distance:
    #     return int(((distance/breaking_distance) * (100 - mininal_turn_speed)) + mininal_turn_speed)
    else:
        return CRUISE_SPEED


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
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [
        int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    if is_checkpoint_new(next_checkpoint_x, next_checkpoint_y):
        last_checkpoint_x = next_checkpoint_x
        last_checkpoint_y = next_checkpoint_y
        checkpoint_counter += 1

    print("CURRENT CHECKPOINT" + " " +
          str(checkpoint_counter), file=sys.stderr, flush=True)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    speed = calculate_speed(next_checkpoint_dist, next_checkpoint_angle)

    update_counter += 1

    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    # Once a round: "x y BOOST"
    print(str(next_checkpoint_x) + " " +
          str(next_checkpoint_y) + " " + str(speed))
