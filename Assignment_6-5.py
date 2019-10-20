S = input("Input a string ")
T = ""
pos = 0
b = -1
while pos < len(S):
    T = T + S[b]
    b = b - 1
    pos = pos + 1
if T == S:
    print("Yes")
else:
    print("No")