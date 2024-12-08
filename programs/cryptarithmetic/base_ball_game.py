def solve_base_ball_game():
    for B in range(10):
        for A in range(10):
            for S in range(10):
                for E in range(10):
                    for L in range(10):
                        for G in range(1, 10):
                            for M in range(10):        
                                if len(set([B, A, S, E, L, G, M])) == 7:
                                    BASE = 1000 * B + 100 * A + 10 * S + E            
                                    BALL = 1000 * B + 100 * A + 10 * L + L               
                                    GAMES = 10000 * G + 1000 * A + 100 * M + 10 * E +S            

                                    if BASE + BALL == GAMES:
                                        print(f"Solution found: BASE = {BASE}, BALL = {BALL}, GAMES = {GAMES}")
                                        print(f"Letter to digit mapping: B={B}, A={A}, S={S}, E={E}, L={L}, G={G}, M={M}")
                                        return

solve_base_ball_game()