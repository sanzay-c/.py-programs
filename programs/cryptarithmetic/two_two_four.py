# solve for T W O F U R
def solve_two_two_four():
    for T in range(10):
        for W in range(10):
            for O in range(10):
                for F in range(10):
                    for U in range(10):
                        for R in range(10):
                            if len(set([T, W, O, F, U, R])) == 6:
                                TWO = 100 * T + 10 * W + O
                                TWO = 100 * T + 10 * W + O
                                FOUR = 1000 * F + 100 * O + 10 * U + R

                                if TWO + TWO == FOUR:
                                    print(f"Solution found: TWO = {TWO}, TWO = {TWO}, FOUR= {FOUR}")
                                    print(f"Letter to digit mapping: T={T}, W={W}, O={O}, F={F}, U={U}, R={R}, R={R}")
                                    return
                                
solve_two_two_four()