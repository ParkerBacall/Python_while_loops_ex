is_game_over: false
p_x_pos = 0
e_x_pos = 3
end_x_pos = 10

while not is_game_over:
    if p_x_pos == e_x_pos
        is_game_over = True
    elif p_x_pos >= end_x_pos
        is_game_over = False
    else:
        p_x_pos += 2
        e_x_pos += 1