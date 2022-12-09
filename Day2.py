"""
AoC 2022, Day 2

Phoebe Cheung
Dec 3, 2022
"""
# %% Part 1
import numpy as np
import csv

file = "inputs\Day2_Input.csv"
totalScore = 0

def calcScore(opponent,myChoice):
    # rock = 1, paper = 2, scissors = 3
    if opponent == 'A':
        opponentVal = 1 # rock
    elif opponent == 'B':
        opponentVal = 2 # paper
    else:
        opponentVal = 3 # scissors
    
    if myChoice == 'X':
        myChoiceVal = 1 # rock
    elif myChoice == 'Y':
        myChoiceVal = 2 # paper
    else:
        myChoiceVal = 3 # scissors
    
    if myChoiceVal == opponentVal: # draw
        score = myChoiceVal + 3
    elif myChoiceVal - opponentVal == 1 or myChoiceVal - opponentVal == -2: # win
        score = myChoiceVal + 6
    else: # lose
        score = myChoiceVal + 0

    return (score)

with open(file) as f:
    reader = csv.reader(f)
    for row in reader:
        res = row[0].split()
        opponent = res[0]
        myChoice = res[1]
        totalScore = totalScore + calcScore(opponent,myChoice)

print(totalScore)

# %% Part 2
import numpy as np
import csv

file = "inputs\Day2_Input.csv"
totalScore = 0

def calcScore(opponent,myChoice):
    # rock = 1, paper = 2, scissors = 3
    if opponent == 'A':
        opponentVal = 1 # rock
    elif opponent == 'B':
        opponentVal = 2 # paper
    else:
        opponentVal = 3 # scissors
    
    # X = lose, Y = draw, Z = win
    if myChoice == 'X':
        myChoiceVal = 0 # lose
    elif myChoice == 'Y':
        myChoiceVal = 3 # draw
    else:
        myChoiceVal = 6 # win
    
    if myChoiceVal == 3: # draw
        shapeVal = opponentVal
        
    elif myChoiceVal == 6: # win
        if opponentVal < 3:
            shapeVal = opponentVal + 1
        else:
            shapeVal = 1
    else: # lose
        if opponentVal > 1:
            shapeVal = opponentVal - 1
        else:
            shapeVal = 3

    score = myChoiceVal + shapeVal
    return (score)

with open(file) as f:
    reader = csv.reader(f)
    for row in reader:
        res = row[0].split()
        opponent = res[0]
        myChoice = res[1]
        totalScore = totalScore + calcScore(opponent,myChoice)

print(totalScore)
