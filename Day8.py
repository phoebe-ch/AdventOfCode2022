"""
AoC 2022, Day 8

Phoebe Cheung
Dec 8, 2022

"""
# %% Part 1
file = "Day8_Input.txt"
with open(file) as f:
    lines = f.readlines()

linesTranspose = [''.join(s) for s in zip(*lines)]

gridSizeX = len(lines[0])
gridSizeY = len(lines)

def checkSurroundings(x,y):
    isVisible = False

    # check left
    isVisible = all(int(i) < int(lines[x][y]) for i in lines[x][:y])
    if isVisible: return isVisible
    
    # check right
    isVisible = all(int(i) < int(lines[x][y]) for i in lines[x][y+1:-1])
    if isVisible: return isVisible

    # check above
    isVisible = all(int(i) < int(linesTranspose[y][x]) for i in linesTranspose[y][:x])
    if isVisible: return isVisible

    # check below
    isVisible = all(int(i) < int(linesTranspose[y][x]) for i in linesTranspose[y][x+1:])
    if isVisible: return isVisible

    return isVisible

numVisible = 0

# count edge trees
numVisible = (gridSizeX-1)*2 + (gridSizeY-2)*2

# check interior trees
x = 1
y = 1
while x < gridSizeX-2:
    y = 1
    while y < gridSizeY-1:
        isVisible = checkSurroundings(x,y)
        if isVisible:
            numVisible += 1
        y += 1
    x += 1

print(numVisible)

# %% Part 2
file = "Day8_Input.txt"
with open(file) as f:
    lines = f.readlines()

linesTranspose = [''.join(s) for s in zip(*lines)]

gridSizeX = len(lines[0])
gridSizeY = len(lines)

def scenicCounter(current,side,isReverse):
    counter = 0
    print("counter start")
    if isReverse:
        side = reversed(side)

    for tree in side:
        print("check " + tree + " and current " + current)
        if int(current) >= int(tree):
            counter += 1
            if int(current) == int(tree):
                break
        else:
            counter += 1
            break
    
    return counter


def checkSurroundings(x,y):
    # score = left*right*above*below
    scenicLeft = scenicCounter(lines[x][y],lines[x][:y],True)
    scenicRight = scenicCounter(lines[x][y],lines[x][y+1:-1],False)
    scenicAbove = scenicCounter(linesTranspose[y][x],linesTranspose[y][:x],True)
    scenicBelow = scenicCounter(linesTranspose[y][x],linesTranspose[y][x+1:],False)
    print([scenicLeft,scenicRight,scenicAbove,scenicBelow])
    scenicScore = scenicLeft*scenicRight*scenicAbove*scenicBelow
    print(scenicScore)
    return scenicScore

numVisible = 0

# count edge trees
numVisible = (gridSizeX-1)*2 + (gridSizeY-2)*2

# check interior trees
x = 1
y = 1
maxScore = 0
while x < gridSizeX-2:
    y = 1
    while y < gridSizeY-1:
        print(lines[x][y])
        currentScore = checkSurroundings(x,y)
        if currentScore > maxScore:
            maxScore = currentScore
        y += 1
        print("")
    x += 1

print(maxScore)