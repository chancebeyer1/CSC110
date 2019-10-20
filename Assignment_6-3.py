S = input("Input a string ")
T = ""

for pos in range(len(S)):
    if S[pos] == " ":
        T = T + ":"
    else:
        T = T + S[pos]
print("Here is your string without spaces:", T)