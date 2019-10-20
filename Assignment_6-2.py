M = int(input("Input a positive integer "))
N = int(input("Input a positive integer "))

c = ""
for M in range(M,N + 1):
    c = c + chr(M) + ", "

print(c)