from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    n = int(input())
    rooks = range(1, n + 1)
    domain = [(i, j) for i in range(n) for j in range(n)]

    problem.addVariables(rooks, domain)

    for rok1 in rooks:
        for rok2 in rooks:
            if rok1 < rok2:
                problem.addConstraint(
                    lambda r1, r2: r1[0] != r2[0] and r1[1] != r2[1] and abs(r1[0] - r2[0]) != abs(r1[1] - r2[1]),
                    (rok1, rok2))

    if n <= 6:
        print(len(problem.getSolutions()))
    else:
        print(problem.getSolution())

