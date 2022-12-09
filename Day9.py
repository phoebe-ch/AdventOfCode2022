"""
AoC 2022, Day 9

Phoebe Cheung
Dec 9, 2022
"""
# %% Part 1
import numpy as np

file = "inputs\Day9_Input.txt"
lines = open(file).readlines()

def moveT(tCurrent,dir,prevHx,prevHy):
    diffX = abs(hCurrent[0]-tCurrent[0])
    diffY = abs(hCurrent[1]-tCurrent[1])

    if diffX == 0 and diffY == 0 and i == 1 : # overlap
        tCurrent = tCurrent # don't move
    elif diffX * diffY == 0 and (diffX == 1 or diffY == 1): # adjacent
        tCurrent = tCurrent # don't move
    elif diffX * diffY == 0 and (diffX == 2 or diffY == 2): # same row/column but not adjacent
        tCurrent = move(dir,tCurrent) # move like H
    elif diffX == 2 or diffY == 2: # not diagonal
        tCurrent = [prevHx,prevHy] # move towards H
    elif diffX == 1 and diffY == 1: # diagonal
        tCurrent = tCurrent  # don't move
    return tCurrent

def move(dir,current):
    if dir == "U":
        current[1] += 1
    elif dir == "D":
        current[1] -= 1
    elif dir == "L":
        current[0] -= 1
    elif dir == "R":
        current[0] += 1
    
    return current

tLocations = []

hCurrent = [0,0]
tCurrent = [0,0]

for row in lines:
    dir,num = [x for x in row.split(" ")]
    num = int(num)
    i = 1
    while i <= num:
        prevHx = hCurrent[0]
        prevHy = hCurrent[1]
        hCurrent = move(dir,hCurrent)
        tCurrent = moveT(tCurrent,dir,prevHx,prevHy)
        tLocations.append(str([tCurrent[0],tCurrent[1]]))
        
        i += 1

print(len(np.unique(tLocations)))


# %% Part 2
import numpy as np

file = "inputs\Day9_Input.txt"
lines = open(file).readlines()

def moveT(hCurrent,tCurrent):
    diffX = abs(hCurrent[0]-tCurrent[0])
    diffY = abs(hCurrent[1]-tCurrent[1])
    if diffX == 0 and diffY == 0: # overlap
        tCurrent = tCurrent # don't move
    elif diffX == 1 and diffY == 1: # diagonal
        tCurrent = tCurrent  # don't move
    elif diffX * diffY == 0 and (diffX == 1 or diffY == 1): # adjacent
        tCurrent = tCurrent # don't move
    elif diffX * diffY == 0 and (diffX == 2 or diffY == 2): # same row/column but not adjacent
        tCurrent = moveNext(tCurrent,hCurrent) # move like H
    elif (diffX == 1 or diffY == 1) and (diffX == 2 or diffY == 2): # diagonal but not adjacent
        tCurrent = diag(tCurrent,hCurrent) # move diagonal
    elif diffX == 2 and diffY == 2: # diagonal but not adjacent
        tCurrent = diag(tCurrent,hCurrent) # move diagonal
    else:
        print("something's wrong")
    return tCurrent

def move(dir,current):
    if dir == "U":
        current[1] += 1
    elif dir == "D":
        current[1] -= 1
    elif dir == "L":
        current[0] -= 1
    elif dir == "R":
        current[0] += 1
    return current

def diag(current,compare):
    diffX = compare[0]-current[0]
    diffY = compare[1]-current[1]
    if diffX > 0 and diffY > 0:
        current = move("U",current)
        current = move("R",current)
    elif diffX < 0 and diffY > 0:
        current = move("U",current)
        current = move("L",current)    
    elif diffX > 0 and diffY < 0:
        current = move("D",current)
        current = move("R",current)
    elif diffX < 0 and diffY < 0:
        current = move("D",current)
        current = move("L",current)
    return current

def moveNext(current,compare):
    diffX = compare[0]-current[0]
    diffY = compare[1]-current[1]
    if diffX > 0:
        current = move("R",current)
    elif diffY > 0:
        current = move("U",current)    
    elif diffY < 0:
        current = move("D",current)
    elif diffX < 0:
        current = move("L",current)
    return current


tLocations = []
ropeCurrent = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

for row in lines:
    dir,num = [x for x in row.split(" ")]
    num = int(num)
    i = 1
    while i <= num:
        ropeCurrent[0] = move(dir,ropeCurrent[0])
        j = 1
        while j < len(ropeCurrent):
            ropeCurrent[j] = moveT(ropeCurrent[j-1],ropeCurrent[j])
            j += 1      
        
        tLocations.append(str([ropeCurrent[9][0],ropeCurrent[9][1]]))
        i += 1

print(len(np.unique(tLocations)))