"""
AoC 2022, Day 3

Phoebe Cheung
Dec 3, 2022
"""
# %% Part 1

file = "Day3_Input.txt"

totalScore = 0

with open(file) as f:
    lines = f.readlines()

    for row in lines:
        firstHalf = row[:len(row)//2]
        secondHalf = row[len(row)//2:]

        commonChar = ''.join(set(firstHalf).intersection(secondHalf))
        ascii = ord(commonChar)
        
        if ascii < 91: # capital letters
            score = ascii - 38
        else:
            score = ascii - 96

        totalScore += score

print(totalScore)

# %% Part 2
import numpy as np

file = "Day3_Input.txt"

totalScore = 0

with open(file) as f:
    lines = f.readlines()
    
    i = 0
    while i < len(lines):
        commonChar = ''.join(set(lines[i]).intersection(lines[i+1],lines[i+2]))
        ascii = ord(max(commonChar))
        if ascii < 91: # capital letters
            score = ascii - 38
        else:
            score = ascii - 96

        totalScore += score

        i += 3

print(totalScore)