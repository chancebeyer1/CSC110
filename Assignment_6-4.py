S = input("Input a string ")
T = ""
i = ""
pos = 0
i = S[pos]
upper = ord(i) - 32
i = chr(upper)
T = T + i
pos = 1
while pos < len(S):
    if S[pos] == chr(32):
        T = T + S[pos]
        pos = pos + 1
        i = S[pos]
        upper = ord(i) - 32
        i = chr(upper)
        T = T + i
        pos = pos + 1
    else:
        T = T + S[pos]
        pos = pos + 1
print(T)