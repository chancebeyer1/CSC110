import diamonds

f = open("C:/Users/chanc/OneDrive/College/CSC-110/smalldiamonds.csv")
lines = f.readlines()
f.close()

def makeDiamond(line):
    num = eval(line[0].strip())
    caret = eval(line[1].strip())
    cut = line[2].strip()
    color = line[3].strip()
    clarity = line[4].strip()
    depth = eval(line[5].strip())
    table = eval(line[6].strip())
    price = eval(line[7].strip())
    x = eval(line[8].strip())
    y = eval(line[9].strip())
    z = eval(line[10].strip())
    return diamonds.Diamonds(num, caret, cut, color, clarity, depth, table, price, x, y, z)

def readDiamonds(fileName):
    f = open(fileName)
    lines = f.readlines()
    f.close()
    diamonds = []
    for pos in range(1, len(lines)):
        line = lines[pos]
        i = line.split(",")
        v = makeDiamond(i)
        diamonds.append(v)
    return diamonds

L = readDiamonds("C:/Users/chanc/OneDrive/College/CSC-110/smalldiamonds.csv")
print(L)

L2 = readDiamonds("C:/Users/chanc/OneDrive/College/CSC-110/diamonds.csv")
print(len(L2))


def findCaret(diamonds, W):
    caretWeight = []
    for pos in range(len(diamonds)):
        weight = diamonds[pos]
        if weight.caret >= W:
            caretWeight.append(weight)
    return caretWeight

C = findCaret(L, .23)
print(C)

def findIdealCut(diamonds):
    idealCut = []
    for pos in range(len(diamonds)):
        cut = diamonds[pos]
        if cut.cut == "Ideal":
            idealCut.append(cut)
    return idealCut

j = findIdealCut(L)
print(j)

def findCut(diamonds, C):
    c_cut = []
    for pos in range(len(diamonds)):
        cut = diamonds[pos]
        if cut.cut == C:
            c_cut.append(cut)
    return c_cut

i = findCut(L, "Ideal")
print(i)

def cuts(diamonds):
    possibleCuts = []
    for pos in range(len(diamonds)):
        cut = diamonds[pos].cut
        if cut not in possibleCuts:
            possibleCuts.append(cut)
    return possibleCuts

p = cuts(L)
print(p)

def avgPricePerWeight(diamonds):
    import functions3
    avgCostPerWeight = []
    sum = []
    possibleCut = cuts(L)
    for pos in range(len(possibleCut)):
        cts = findCut(diamonds, possibleCut[pos])
        for i in range(len(cts)):
            PricePerWeight = cts[i].price/cts[i].caret
            sum.append(PricePerWeight)
            avg = functions3.average(sum)
        avgCostPerWeight.append(avg)
        sum = []
    return avgCostPerWeight

q = avgPricePerWeight(L)
print(q)