f = open("C:/Users/chanc/OneDrive/Documents/nums.txt")
lines = f.readlines()
f.close()

nums = []
for pos in range(len(lines)):
    line = lines[pos]
    strippedLine = line.strip()
    if strippedLine != "" and strippedLine[0] != "#":
        numStrings = line.split(",")
        for i in range(len(numStrings)):
            ns = numStrings[i]
            nsNoCrap = ns.split()
            if nsNoCrap != "":
                n = eval(ns)
                nums.append(n)
print(nums)

# f = open("C:/Users/chanc/OneDrive/Documents/nums.txt")
# lines = f.readlines()
# f.close()
# print(lines)
#
# num = []
# for pos in range(len(lines)):
#     s = lines[pos]
#     n = eval(s)
#     num.append(n)
# print(num)
#
