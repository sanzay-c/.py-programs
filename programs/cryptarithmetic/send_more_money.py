def solve_send_more_money():
    for S in range(10):
        for E in range(10):
            for N in range(10):
                for D in range(10):
                    for M in range(10):
                        for O in range(10):
                            for R in range(10):
                                for Y in range(10):
                                    # Ensure all digits are distinct
                                    if len(set([S, E, N, D, M, O, R, Y])) == 8:
                                        # Calculate SEND, MORE, and MONEY
                                        SEND = S * 1000 + E * 100 + N * 10 + D
                                        MORE = M * 1000 + O * 100 + R * 10 + E
                                        MONEY = M * 10000 + O * 1000 + N * 100 + E * 10 + Y
                                        
                                        # Check if the equation SEND + MORE = MONEY holds
                                        if SEND + MORE == MONEY:
                                            # Print the solution if the equation holds
                                            print(f"Solution found: SEND = {SEND}, MORE = {MORE}, MONEY = {MONEY}")
                                            print(f"Letter to digit mapping: S={S}, E={E}, N={N}, D={D}, M={M}, O={O}, R={R}, Y={Y}")
                                            return
                  
# Call the function to solve the puzzle
solve_send_more_money()
