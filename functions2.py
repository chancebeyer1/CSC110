


def Growth(P, R, N):
    for yr in range(N):
        increase = P * R/100
        P = P + increase

    return P

#   compute x^n for any integer n, including negative and zero n
def pow(x, n):
    if n >= 0:
        result = 1
        for i in range(n):
            result = result * x
        return result
    else:
        #   n < 0
        return 1 / pow(x, -n)

#   compute x^n, for positive or zero values of n

# def powPositive(x, n):
#     result = 1
#     for i in range(n):
#         result = result * x
#     return result
#
# #   compute x^n, e.g. pow(x, 2) I get x*x, pow(x, 3) I get x*x*x
# def pow(x, n):
#     if n >= 0:
#         return powPositive(x, n)
#     else:
#         #   n < 0
#         return 1 / powPositive(x, -n)

# def pow(x, n):
#     if n >= 0:
#         result = 1
#         for i in range(n):
#             result = result * x
#         return result
#     else:
#         #   n < 0
#         result = 1
#         for i in range(-n):
#             result = result * x
#         return 1 / result

def max(a, b):
    if a > b:
        return a
    else:
        return b

def min(a, b):
    if a < b:
        return a
    else:
        return b

