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

while at_goal() != True: # while not at_goal():
    move_jump()