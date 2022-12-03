"""
AoC 2022, Day 1

Phoebe Cheung
Dec 3, 2022
"""
# %% Part 1
import numpy as np
import csv

file = "Day1_Input.csv"

maxSum = 0
currentSum = 0

with open(file, 'rU') as csvfile:
    csvreader = csv.reader(csvfile)
    
    for row in csvreader:
        if row == []:
            if maxSum < currentSum:
                maxSum = currentSum
            currentSum = 0
        else:
            currentNum = int(row[0])
            currentSum = currentSum + currentNum

print(maxSum)

# %% Part 2
import numpy as np
import csv

file = "Day1_Input.csv"

maxSums = [0,0,0]
currentSum = 0
sum = 0

with open(file, 'rU') as csvfile:
    csvreader = csv.reader(csvfile)
    
    for row in csvreader:
        if row == []:
            if min(maxSums) < currentSum:
                maxSums[maxSums.index(min(maxSums))] = currentSum
            currentSum = 0
        else:
            currentNum = int(row[0])
            currentSum = currentSum + currentNum

for i in maxSums:
    sum = sum + i

print(sum) 