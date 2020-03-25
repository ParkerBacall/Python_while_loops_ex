is_game_over= False
p_x_pos = 0
e_x_pos = 3
end_x_pos = 10

while not is_game_over:
    if p_x_pos == e_x_pos:
        is_game_over = True
        print("you lose!")
    elif p_x_pos >= end_x_pos:
        is_game_over = False
        print("you win!")
    else:
        p_x_pos += 2
        e_x_pos += 1
