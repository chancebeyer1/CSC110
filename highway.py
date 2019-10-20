#   Average
f = open("C:/Users/chanc/OneDrive/College/CSC-110/highway.txt")
lines = f.readlines()
f.close()

sum = 0
count = 0
for pos in range(1, len(lines)):
    line = lines[pos]
    cls = line[57:].strip()
    if cls == "compact":
        hwy = eval(line[50:54].strip())
        sum = sum + hwy
        count = count + 1
avg = sum / count
print(avg)