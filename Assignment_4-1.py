P = eval(input("Input the principal of investment "))
N = eval(input("Input the term of investment "))
R = eval(input("Input the rate of return for investment "))
year = 0
while N > 0:
    print("Value of investment at the beginning of year", year, "is", P)
    interest = P * (R * (1 / 100))
    P = P + interest
    year = year + 1
    print("Interest for year", year, "is", interest)
    print("Value of investment at the end of year", year, "is", P)
# The print below this line is to separate the years
    print(""
          "")
    N = N - 1