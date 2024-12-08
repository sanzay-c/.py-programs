def solve_cross_road_danger():
    for C in range(10):
        for R in range(10):
            for O in range(10):
                for S in range(10):
                    for A in range(10):
                        for D in range(1, 10): 
                            for N in range(10):
                                for G in range(10):
                                    for E in range(10):
                                        if len(set([C, R, O, S, A, D, N, G, E])) == 9:
                                            CROSS = 10000 * C + 1000 * R + 100 * O + 10 * S + S
                                            ROADS = 10000 * R + 1000 * O + 100 * A + 10 * D + S
                                            DANGER = 100000 * D + 10000 * A + 1000 * N + 100 * G + 10 * E + R
                                            
                                            if CROSS + ROADS == DANGER:
                                                print(f"Solution found: CROSS = {CROSS}, ROADS = {ROADS}, DANGER = {DANGER}")
                                                print(f"Letter to digit mapping: C={C}, R={R}, O={O}, S={S}, A={A}, D={D}, N={N}, G={G}, E={E}")
                                                return

solve_cross_road_danger()
