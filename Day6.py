"""
AoC 2022, Day 6

Phoebe Cheung
Dec 5, 2022
"""
# %% Part 1
file = "Day6_Input.txt"
with open(file) as f:
    lines = f.readlines()

str = lines[0]
numThreshold = 4
counter = numThreshold

while counter < len(str):
    strCheck = str[counter-numThreshold:counter]
    
    # check if string is unique
    unique = True
    for char in strCheck:
        if strCheck.count(char) > 1:
            unique = False
            break
        elif char == strCheck[-1]:
            print(counter)
            counter = len(str)
                
    counter += 1

# %% Part 2
file = "Day6_Input.txt"
with open(file) as f:
    lines = f.readlines()
    
str = lines[0]
numThreshold = 14
counter = numThreshold

while counter < len(str):
    strCheck = str[counter-numThreshold:counter]
    
    # check if string is unique
    unique = True
    for char in strCheck:
        if strCheck.count(char) > 1:
            unique = False
            break
        elif char == strCheck[-1]:
            print(counter)
            counter = len(str)
                
    counter += 1