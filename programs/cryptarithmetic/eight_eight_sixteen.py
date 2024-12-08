# EIGHT, EIGHT, SIXTEEN
# E, I, G, H, T, S, X, N

def solve_eight_eight_sixteen():
    for E in range(10):
        for I in range(10):
            for G in range(10):
                for H in range(10):
                    for T in range(10):
                        for S in range(10):
                            for X in range(10):
                                for N in range(10):
                                    if len(set([E, I, G, H, T, S, X, N])) == 8:
                                        EIGHT = 10000 * E + 1000 * I + 100 * G + 10 * H + T
                                        EIGHT = 10000 * E + 1000 * I + 100 * G + 10 * H + T
                                        SIXTEN = 100000 * S + 10000 * I + 1000 * X + 100 * T + 10 * E + N
                                        
                                        if EIGHT + EIGHT == SIXTEN:
                                            print(f"Solution found: EIGHT = {EIGHT}, EIGHT = {EIGHT}, SIXTEEN = {SIXTEN}")
                                            print(f"Letter to digit mapping: E={E}, I={I}, G={G}, H={H}, T={T}, S={S}, X={X}, N={N}")
                                            return
                                        
solve_eight_eight_sixteen()                                