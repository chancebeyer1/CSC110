hours = eval(input("Type your weekly hours: "))
hourRate = eval(input("Type your hourly rate: "))
if hours > 40:
    hours = (hours - 40) * 1.5
    totalWages = ((40 * hourRate) + (hours * hourRate))
else:
    totalWages = hours * hourRate
print("Your total wages for the week is ", totalWages)
