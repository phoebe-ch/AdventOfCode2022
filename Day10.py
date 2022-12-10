"""
AoC 2022, Day 10

Phoebe Cheung
Dec 9, 2022
"""
# %% Part 1
file = "inputs\Day10_Input.txt"
lines = open(file).readlines()

x = 1
cycle = 1
xArray = [1]

for idx,row in enumerate(lines):
    if row == "noop\n":
        x = xArray[cycle-1]
        cycle += 1
        xArray.append(x)
    elif "addx " in row:
        val = int(row.split("addx ")[1])
        x = xArray[cycle-1]
        cycle += 1
        xArray.append(x)
        cycle += 1
        xArray.append(x+val)

i = 20
sum = 0
while i < len(xArray):
    sum += xArray[i-1]*(i)
    
    i += 40

print(sum)
        
# %% Part 2
file = "inputs\Day10_Input.txt"
lines = open(file).readlines()

CRT = [list(".")*40 for i in range(6)]

x = 1
cycle = 1
xArray = [1]

for idx,row in enumerate(lines):
    if row == "noop\n":
        x = xArray[cycle-1]
        cycle += 1
        xArray.append(x)
    elif "addx " in row:
        val = int(row.split("addx ")[1])
        x = xArray[cycle-1]
        cycle += 1
        xArray.append(x)
        cycle += 1
        xArray.append(x+val)

spriteLoc = [0,1,2]
pos = 0
for pos,val in enumerate(xArray):
    row = pos//40
    col = pos - row*40

    spriteLoc = [val-1,val,val+1]
    if col in spriteLoc:
        CRT[row][col] = "#"
    
    pos += 1

i = 0
while i < 6:
    print("".join(CRT[i]))
    i += 1
