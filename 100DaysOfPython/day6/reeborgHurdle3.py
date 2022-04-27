def hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


def turn_right():
    for right in range(1, 4):
        turn_left()


while not at_goal():
    if wall_in_front():
        hurdle()
    else:
        move()