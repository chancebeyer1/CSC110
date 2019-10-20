#   represent a lottery card as a list of rows
#   i.e. a list of lists of numbers
card = [
            [1, 4, 6],
            [2, 3, 7],
            [9, 8, 5]
         ]

#   count how many times num appears in the card
def count(num, card):
    count = 0
    for r in range(len(card)):
        row_r = card[r]
        for c in range(len(row_r)):
            numC = row_r[c]
            if num == numC:
                count = count + 1
    return count

def noRepeats(card):
    for num in range(1, 10):
        if count(num, card) != 1:
            return False
    return True

# def noRepeats(card):
#     #   for each row
#     for i in range(len(card)):
#         row = card[i]
#         #   for each num in the row
#         for j in range(len(row)):
#             num = row[j]
#             if count(num, card) != 1:
#                 return False
#     return True


def allOneToNine(card):
    for i in range(len(card)):
        row = card[i]
        for j in range(len(row)):
            num = row[j]
            if num < 1 or num > 9:
                return False
    #   all numbers were between 1 and 9
    return True

#   return true if and only if the card is a 3x3 grid
def isSquareGrid(card):
    if len(card) != 3:
        return False
    #   i know I have 3 rows
    for i in range(len(card)):
        row = card[i]
        if len(row) != 3:
            return False
    #   all rows length 3
    return True

#   return true only if all the numbers in an input card are integers
def allIntegers(card):
    #   for each row
    for i in range(len(card)):
        row = card[i]
        #   for each number in the row
        for j in range(len(row)):
            num = row[j]
            #   is the number and int or not
            if type(num) != int:
                return False
    #   all the numbers are integers
    return True


# card1 = [1, 4, 6, 2, 3, 7, 9, 8, 5]

def isValid(card):
    if not allIntegers(card) or not isSquareGrid(card) \
            or not allOneToNine(card) or not noRepeats(card):
        return False

    #   card must be valid
    return True

print(isValid(card))
#
# card2 = [
#             [1, 2, 9],
#             [4, 3, 8],
#             [6, 7, 5]
#        ]
