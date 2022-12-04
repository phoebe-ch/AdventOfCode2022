"""
AoC 2022, Day 4

Phoebe Cheung
Dec 4, 2022
"""
# %% Part 1
import numpy as np

file = "Day4_Input.txt"

counter = 0

with open(file) as f:
    lines = f.readlines()
    for row in lines:
        firstElf,secondElf = row.split(",")

        firstStart,firstEnd = [int(x) for x in firstElf.split("-")]
        secondStart,secondEnd = [int(x) for x in secondElf.split("-")]
    
        firstRange = np.linspace(firstStart,firstEnd,firstEnd-firstStart+1)
        secondRange = np.linspace(secondStart,secondEnd,secondEnd-secondStart+1)

        overlap = True

        if len(firstRange) <= len(secondRange):
            for num1 in firstRange:
                if num1 not in secondRange:
                    overlap = False
                    break
        else:
            for num2 in secondRange:
                if num2 not in firstRange:
                    overlap = False
                    break
            
        if overlap:
            counter += 1

print(counter)

# %% Part 2
import numpy as np

file = "Day4_Input.txt"

counter = 0

with open(file) as f:
    lines = f.readlines()
    for row in lines:
        firstElf,secondElf = row.split(",")

        firstStart,firstEnd = [int(x) for x in firstElf.split("-")]
        secondStart,secondEnd = [int(x) for x in secondElf.split("-")]
    
        firstRange = np.linspace(firstStart,firstEnd,firstEnd-firstStart+1)
        secondRange = np.linspace(secondStart,secondEnd,secondEnd-secondStart+1)

        overlap = False

        for num1 in firstRange:
            if num1 in secondRange:
                overlap = True
                break

        if overlap:
            counter += 1

print(counter)
