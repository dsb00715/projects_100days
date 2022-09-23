# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()


# for n in range(6):
#     move()
#     jump()
#     turn_left()

# Hurdle 2
# while not at_goal():
#     move()
#     jump()

# Hurdle 3
# while not at_goal():
#     if wall_in_front():
#         jump()
#     elif front_is_clear():
#         move()

# Hurdle 4
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_right()
    move()
    turn_right()
    move()

while not at_goal():
    if wall_in_front():
        turn_left()
        if not wall_in_front():
            move()
        else:
            turn_left()
        while wall_on_right():
            if at_goal():
                exit()
            elif not wall_in_front():
                move()
            else:
                turn_left()
        jump()        
    else:
        move()"""

""" 
best answer for Hurdle 3

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def cycle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        cycle()
    elif front_is_clear():
        move() """

""" 


best answer for Hurdle4

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move() """
