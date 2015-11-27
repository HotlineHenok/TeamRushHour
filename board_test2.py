def _print_board(game_state):
    
    # headers   
    for i in range(len(game_state[0]) + 1):
        if i == 0:
            
            # column for row numbers
            print("   ", end="")
        else:
            
            # column headers
            print("{0:2d} ".format(i), end="")
    print()
    for i, row in enumerate(game_state, 1):
        
        # row number
        print("{0:2d} ".format(i), end="")
        for col in row:
            
            # row data
            if col == NONE:
                print(" {0} ".format("."), end="")
            else:
                print(" {0} ".format(col), end="")
        print()

_print_board(6, 6)