"""
AoC 2022, Day 13

Phoebe Cheung
Dec 12, 2022
"""
# %% Part 1
file = "inputs\Day13_InputSample.txt"
lines = open(file).readlines()

def compare(first,second):
    print(second[0])
    result = True
    if len(first) < len(right):
        return False
    else:
        i = 0
        while i < len(first):
            print(first[i])
            print(second[i])
            if type(first[i]) == int and type(second[i]) == int:
                print("both int")
                result = compareInt(first[i],second[i])
                if not result:
                    print("break1")
                    return result
            elif type(first[i]) == list and type(second[i]) == list:
                print("both list")
                result = compare(first[i],second[i])
                if not result:
                    print("break2")
                    return result
            else:
                print(first[i])
                print(second[i])
                if type(first[i]) == int and type(second[i]) == list:
                    print("first int")
                    firstTest = [first[i]]
                    secondTest = second[i]
                elif type(first[i]) == list and type(second[i]) == int:
                    print("second int")
                    firstTest = first[i]
                    secondTest = [second[i]]
                else:
                    print("yikes")
                result = compare(firstTest,secondTest)
                if not result:
                    print("break3")
                    return result
            i += 1
    print(i)
    print("next")
    return result

def compareInt(intL,intR):
    if intL <= intR:
        return True
    else:
        return False

row = 0
index = 1
sum = 0
while row < 5:
    # store first row
    left = eval(lines[row])
    row += 1
    # store second row
    right = eval(lines[row])
    row += 2
    # compare
    isRightOrder = compare(left,right)
    
    if isRightOrder:
        sum += index

    index += 1


# %% scrap code
# def compareInt(first,second):
#     if first <= second:
#         return True
#     else:
#         return False

# def compareList3(first,second):
#     result = True
#     print("first")
#     print(first[1])
#     print("second")
#     print(second[1])
#     print("hi")
#     if len(first) <= len(second):
#         i = 0
#         while i < len(first):
#             if type(first[i]) == int and type(second[i]) == int: # both are integers
#                 result = compareInt(first[i],second[i])
#                 if ~result:
#                     break
#             elif type(first[i]) == list and type(second[i]) == list: # both are lists
#                 # result = compareList4(first[i],second[i])
#                 if ~result:
#                     break
#             else:
#                 print("one list, one int")
#             i += 1
#         return result
#     else:
#         return False

# def compareList2(first,second):
#     result = True
#     print("first")
#     # print(first[1])
#     print("second")
#     # print(second[1])
#     print("")
#     if len(first) <= len(second):
#         i = 0
#         while i < len(first):
#             if type(first) == int and type(second) == int: # both are integers
#                 result = compareInt(first,second)
#                 if ~result:
#                     break
#             elif type(first) == list and type(second) == list: # both are lists
#                 result = compareList3(first,second)
#                 if ~result:
#                     break
#             else:
#                 print("one list, one int")
#             i += 1
#         return result
#     else:
#         return False

# def compareList1(first,second):
#     result = True
#     if len(first) <= len(second):
#         i = 0
#         while i < len(first):
#             if type(first[i]) == int and type(second[i]) == int: # both are integers
#                 result = compareInt(first[i],second[i])
#                 if ~result:
#                     break
#             elif type(first[i]) == list and type(second[i]) == list: # both are lists
#                 result = compareList2(first[i],second[i])
#                 if ~result:
#                     break
#             else:
#                 print("one list, one int")
#             i += 1
#         return result
#     else:
#         return False

# def compare(first,second):
#     result = True
#     if len(first) <= len(second):
#         i = 0
#         while i < len(first):
#             if type(first[i]) == int and type(second[i]) == int: # both are integers
#                 result = compareInt(first[i],second[i])
#                 if ~result:
#                     break
#             elif type(first[i]) == list and type(second[i]) == list: # both are lists
#                 result = compareList1(first,second)
#                 if ~result:
#                     break
#             else:
#                 print("one list, one int")
#             i += 1
#         return result
#     else:
#         return False