"""
AoC 2022, Day 13

Phoebe Cheung
Dec 25, 2022
"""
# %% Part 1
file = "inputs\Day13_InputSample.txt"
lines = open(file).readlines()

def checkInts(left,right):
    if left < right:
        return True
    elif left > right:
        return False
    elif left == right:
        return 2

def checkLists(left,right):   
    k = 0
    while k < len(left):
        if k == len(right) and k < len(left):
            return False
        if k == len(right) and k == len(left):
            return 2

        if type(left[k]) == int and type(right[k]) == int: # they are integers
            condition = checkInts(left[k],right[k])
            if condition == True:
                return True
            elif condition == 2:
                k += 1
            else:
                return False
        elif type(left[k]) == list and type(right[k]) == list: # they are lists
            condition = checkLists(left[k],right[k])
            if condition == True:
                return True
            elif condition == 2:
                k += 1
            else:
                return False
        else:
            if type(left[k]) == int:
                condition = checkLists([left[k]],right[k])
                if condition == True:
                    return True
                elif condition == 2:
                    k += 1
                else:
                    return False
            elif type(right[k]) == int:
                condition = checkLists(left[k],[right[k]])
                if condition == True:
                    return True
                elif condition == 2:
                    k += 1
                else:
                    return False

def checkOrder(left,right):
    j = 0
    while j < len(left):
        if j == len(right) and j < len(left):
            return False

        if type(left[j]) == int and type(right[j]) == int: # they are integers
            condition = checkInts(left[j],right[j])
            if condition == True:
                return True
            elif condition == 2:
                j += 1
            else:
                return False
        elif type(left[j]) == list and type(right[j]) == list: # they are lists
            condition = checkLists(left[j],right[j])
            if condition == True:
                return True
            elif condition == 2:
                j += 1
            else:
                return False
        elif type(left[j]) == list or type(right[j]) == list:
            if type(left[j]) == int:
                condition = checkLists([left[j]],right[j])
                if condition == True:
                    return True
                elif condition == 2:
                    j += 1
                else:
                    return False
            elif type(right[j]) == int:
                condition = checkLists(left[j],[right[j]])
                if condition == True:
                    return True
                elif condition == 2:
                    j += 1
                else:
                    return False
        else:
            print("yikes")

i = 0
counter = 0
while i < len(lines):
    # line 1
    left = eval(lines[i])
    i += 1

    # line 2
    right = eval(lines[i])

    if checkOrder(left,right):
        counter += i // 3 + 1

    i += 2

print(counter)