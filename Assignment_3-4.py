M = eval(input("Input the first number "))
N = eval(input("Input the second number "))
total = 0
if M < N:
    while M <= N:
        if M % 2 != 0:
            total = total + M
        M = M + 1
else:
    while N <= M:
        if N % 2 != 0:
            total = total + N
        N = N + 1
print("Sum of the odd numbers between the two numbers is", total)