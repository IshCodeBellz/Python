def move_jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def turn_right():
    for right in range(1,4):
        turn_left()

def race():
    for jump in range(1,7):
        move_jump()

race()