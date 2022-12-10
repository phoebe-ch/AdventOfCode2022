"""
AoC 2022, Day 5

Phoebe Cheung
Dec 4, 2022
"""
# %% Part 1
file = "inputs\Day5_Input.txt"
with open(file) as f:
    lines = f.readlines()

crates = lines[:9]
instructions = lines[10:]
cratesArray = []

# initiate arrays to store items
col = 1
row = 8
while col < len(crates[0]):
    row = 8
    rowArray = []
    while row >= 0:
        item = crates[row][col] 
        if item != " ":
            rowArray += item
        row -= 1
    cratesArray.append(rowArray)
    col += 4

# move boxes
for row in instructions:    
    stack,move = row.split("from")
    stack = int(stack[5:])
    moveFrom,moveTo = [int(x) for x in move.split(" to ")]

    stackCounter = 0
    while stackCounter < stack:
        
        cratesArray[moveTo-1] += cratesArray[moveFrom-1][len(cratesArray[moveFrom-1])-1]
        cratesArray[moveFrom-1].pop()
        stackCounter += 1

# report top crate
ans = []
counter = 0
while counter < 9:
    ans += cratesArray[counter][len(cratesArray[counter])-1]
    counter += 1

print(ans)

# %% Part 2
file = "inputs\Day5_Input.txt"
with open(file) as f:
    lines = f.readlines()

crates = lines[:9]
instructions = lines[10:]
cratesArray = []

# initiate arrays to store items
col = 1
row = 8
while col < len(crates[0]):
    row = 8
    rowArray = []
    while row >= 0:
        item = crates[row][col] 
        if item != " ":
            rowArray += item
        row -= 1
    cratesArray.append(rowArray)
    col += 4

# move boxes
for row in instructions:    
    stack,move = row.split("from")
    stack = int(stack[5:])
    moveFrom,moveTo = [int(x) for x in move.split(" to ")]

    cratesArray[moveTo-1] += cratesArray[moveFrom-1][len(cratesArray[moveFrom-1])-stack:]
    cratesArray[moveFrom-1] = cratesArray[moveFrom-1][:len(cratesArray[moveFrom-1])-stack]

# report top crate
ans = []
counter = 0
while counter < 9:
    ans += cratesArray[counter][len(cratesArray[counter])-1]
    counter += 1

print(ans)