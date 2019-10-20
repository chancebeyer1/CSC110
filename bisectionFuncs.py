#   functions related to computing roots of function using the bisection method

#   choose an L with f(L) > 0
#   -rnge < L < rnge

def guessL(f, rnge):
    import random
    L = random.random() * rnge - rnge/2
    while f(L) < 0:
        L = random.random() * rnge - rnge/2
    return L

#   choose an R with f(R) < 0
#   -rnge < L < rnge

def guessR(f, rnge):
    import random
    R = random.random() * rnge - rnge/2
    while f(R) > 0:
        R = random.random() * rnge - rnge/2
    return R

#   find a root of a function f using the bisection method
#   i.e find an x value where abs(f(x)) <= tolerance
#   provide initial guesses for L and R

def roots(f, tolerance, L, R):
    import math

    while math.fabs(f(L)) > tolerance:
        M = (L + R) / 2
        y = f(M)
        #   if f(M) > 0 change L to M and keep R the same
        if y > 0:
            L = M
        #   else change R to M and keep L the same
        else:
            R = M

    return L
