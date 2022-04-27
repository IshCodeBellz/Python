def hurdle():
    turn_left()
    count = 0
    while not right_is_clear():
        count = count + 1
        move()

    turn_right()
    move()
    turn_right()
    for i in range(0, count):
        count = count - 1
        move()
    count = 0
    turn_left()


def turn_right():
    for right in range(1, 4):
        turn_left()


while not at_goal():
    if wall_in_front():
        hurdle()
    else:
        move()