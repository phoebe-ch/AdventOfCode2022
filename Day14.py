"""
AoC 2022, Day 14

Phoebe Cheung
Dec 29, 2022

Part 1 code modification to create gif below Part 2 code
Part 2 takes 1-2 hours to run!
"""
# %% Part 1
import matplotlib.pyplot as plt
import numpy as np

file = "inputs\Day14_Input.txt"
lines = open(file).readlines()

def rockLine(x,y,x0,y0):
    if y != y0:
        yVals = [y,y0]
        yVals.sort()
        yVals[1] += 1 
        yLine = np.arange(yVals[0],yVals[1],1)
        xLine = np.zeros(len(yLine))
        xLine.fill(x0)
    elif x != x0:
        xVals = [x,x0]
        xVals.sort()
        xVals[1] += 1 
        xLine = np.arange(xVals[0],xVals[1],1)
        yLine = np.zeros(len(xLine))
        yLine.fill(y0)
    else:
        print("yikes")

    return xLine, yLine*-1

rocks = []
xSandStart = 500
ySandStart = 0

for row in lines:
    row = row[:-1] # remove new line char at the end of row
    row = row.split(" -> ") # split by arrow

    i = 1
    while i < len(row):
        x0,y0 = row[i-1].split(",")
        x0,y0 = int(x0),int(y0)
        x,y = row[i].split(",")
        x,y = int(x),int(y)
        xLine, yLine = rockLine(x,y,x0,y0)
        for j,xVal in enumerate(xLine):
            rocks.append([xLine[j],yLine[j]])
        i += 1

plt.scatter(*zip(*rocks),marker=',',s=1)
plt.scatter(xSandStart,ySandStart,marker='+',s=100,linewidths=3)
plt.axis("equal")
plt.grid(True)
plt.show()

xRocks,yRocks = zip(*rocks)
bottom = min(yRocks)

ans = 0

sandRunning = True
sand = []
while sandRunning: # repeats when sand is at rest
    sandRun = [xSandStart,ySandStart]
    notRest = True
    while notRest:
        sandTry = [sandRun[0],sandRun[1]-1]
        if sandTry in rocks:
            sandTry = [sandRun[0]-1,sandRun[1]-1]
            if sandTry in rocks:
                sandTry = [sandRun[0]+1,sandRun[1]-1]
                if sandTry in rocks:
                    notRest = False
                else:
                    sandRun = sandTry
            else:
                sandRun = sandTry
        else:
            sandRun = sandTry

        if sandRun[1] < bottom:
            print(ans)
            notRest = False
            sandRunning = False

    rocks.append(sandRun)
    sand.append(sandRun)

    ans += 1

plt.scatter(*zip(*rocks),marker=',',s=1)
plt.scatter(*zip(*sand),marker=',',s=1)
plt.scatter(xSandStart,ySandStart,marker='+',s=100,linewidths=3)
plt.axis("equal")
plt.grid(True)
plt.show()


# %% Part 2
import matplotlib.pyplot as plt
import numpy as np

file = "inputs\Day14_Input.txt"
lines = open(file).readlines()

def rockLine(x,y,x0,y0):
    if y != y0:
        yVals = [y,y0]
        yVals.sort()
        yVals[1] += 1 
        yLine = np.arange(yVals[0],yVals[1],1)
        xLine = np.zeros(len(yLine))
        xLine.fill(x0)
    elif x != x0:
        xVals = [x,x0]
        xVals.sort()
        xVals[1] += 1 
        xLine = np.arange(xVals[0],xVals[1],1)
        yLine = np.zeros(len(xLine))
        yLine.fill(y0)
    else:
        print("yikes")

    return xLine, yLine*-1

rocks = []
xSandStart = 500
ySandStart = 0

for row in lines:
    row = row[:-1] # remove new line char at the end of row
    row = row.split(" -> ") # split by arrow

    i = 1
    while i < len(row):
        x0,y0 = row[i-1].split(",")
        x0,y0 = int(x0),int(y0)
        x,y = row[i].split(",")
        x,y = int(x),int(y)
        xLine, yLine = rockLine(x,y,x0,y0)
        for j,xVal in enumerate(xLine):
            rocks.append([xLine[j],yLine[j]])
        i += 1


plt.scatter(*zip(*rocks),marker='*')
plt.scatter(xSandStart,ySandStart,marker='+',s=100,linewidths=3)
plt.axis("equal")
plt.grid(True)
plt.show()

xRocks,yRocks = zip(*rocks)
bottom = min(yRocks)-1

ans = 0
sandRunning = True
sand = []
while sandRunning: # repeats when sand is at rest
    sandRun = [xSandStart,ySandStart]
    notRest = True
    while notRest:
        sandTry = [sandRun[0],sandRun[1]-1]
        if sandTry in rocks or sandTry[1] < bottom:
            sandTry = [sandRun[0]-1,sandRun[1]-1]
            if sandTry in rocks or sandTry[1] < bottom:
                sandTry = [sandRun[0]+1,sandRun[1]-1]
                if sandTry in rocks or sandTry[1] < bottom:
                    notRest = False
                else:
                    sandRun = sandTry
            else:
                sandRun = sandTry
        else:
            sandRun = sandTry

        if sandRun == [xSandStart,ySandStart]:
            print(ans+1)
            notRest = False
            sandRunning = False

    rocks.append(sandRun)
    sand.append(sandRun)

    if ans % 100 == 0:
        plt.scatter(*zip(*rocks),marker='*')
        plt.scatter(*zip(*sand),marker='o')
        plt.scatter(xSandStart,ySandStart,marker='+',s=100,linewidths=3)
        plt.axis("equal")
        plt.grid(True)
        plt.show()
    ans += 1

plt.scatter(*zip(*rocks),marker='*')
plt.scatter(*zip(*sand),marker='o')
plt.scatter(xSandStart,ySandStart,marker='+',s=100,linewidths=3)
plt.axis("equal")
plt.grid(True)
plt.show()


# %% Part 1 gif
import matplotlib.pyplot as plt
import imageio
import numpy as np

file = "inputs\Day14_Input.txt"
lines = open(file).readlines()

def rockLine(x,y,x0,y0):
    if y != y0:
        yVals = [y,y0]
        yVals.sort()
        yVals[1] += 1 
        yLine = np.arange(yVals[0],yVals[1],1)
        xLine = np.zeros(len(yLine))
        xLine.fill(x0)
    elif x != x0:
        xVals = [x,x0]
        xVals.sort()
        xVals[1] += 1 
        xLine = np.arange(xVals[0],xVals[1],1)
        yLine = np.zeros(len(xLine))
        yLine.fill(y0)
    else:
        print("yikes")

    return xLine, yLine*-1

rocks = []
frames = []
xSandStart = 500
ySandStart = 0

for row in lines:
    row = row[:-1] # remove new line char at the end of row
    row = row.split(" -> ") # split by arrow

    i = 1
    while i < len(row):
        x0,y0 = row[i-1].split(",")
        x0,y0 = int(x0),int(y0)
        x,y = row[i].split(",")
        x,y = int(x),int(y)
        xLine, yLine = rockLine(x,y,x0,y0)
        for j,xVal in enumerate(xLine):
            rocks.append([xLine[j],yLine[j]])
        i += 1

plt.figure(dpi=300)
plt.scatter(*zip(*rocks),marker=',',s=1)
plt.scatter(xSandStart,ySandStart,marker='+',s=100,linewidths=3)
plt.axis("equal")
plt.grid(True)
plt.ylim([-180,10])
plt.savefig(f'./Day14gif/img_0.png',transparent = False)
plt.show()
image = imageio.v2.imread(f'./Day14gif/img_0.png')
frames.append(image)

xRocks,yRocks = zip(*rocks)
bottom = min(yRocks)

ans = 0

sandRunning = True
sand = []
while sandRunning: # repeats when sand is at rest
    sandRun = [xSandStart,ySandStart]
    notRest = True
    while notRest:
        sandTry = [sandRun[0],sandRun[1]-1]
        if sandTry in rocks:
            sandTry = [sandRun[0]-1,sandRun[1]-1]
            if sandTry in rocks:
                sandTry = [sandRun[0]+1,sandRun[1]-1]
                if sandTry in rocks:
                    notRest = False
                else:
                    sandRun = sandTry
            else:
                sandRun = sandTry
        else:
            sandRun = sandTry

        if sandRun[1] < bottom:
            print(ans)
            notRest = False
            sandRunning = False

    rocks.append(sandRun)
    sand.append(sandRun)

    ans += 1

    if ans % 25 == 0:
        plt.figure(dpi=300)
        plt.scatter(*zip(*rocks),marker=',',s=1)
        plt.scatter(*zip(*sand),marker=',',s=1)
        plt.scatter(xSandStart,ySandStart,marker='+',s=100,linewidths=3)
        plt.axis("equal")
        plt.grid(True)
        plt.ylim([-180,10])
        plt.savefig(f'./Day14gif/img_{ans}.png',transparent = False)
        image = imageio.v2.imread(f'./Day14gif/img_{ans}.png')
        frames.append(image)
        plt.close()

plt.figure(dpi=300)
plt.scatter(*zip(*rocks),marker=',',s=1)
plt.scatter(*zip(*sand),marker=',',s=1)
plt.scatter(xSandStart,ySandStart,marker='+',s=100,linewidths=3)
plt.axis("equal")
plt.grid(True)
plt.ylim([-180,10])
plt.savefig(f'./Day14gif/img_{ans}.png',transparent = False)
plt.show()
image = imageio.v2.imread(f'./Day14gif/img_{ans}.png')
frames.append(image)

imageio.mimsave('./Day14pt1.gif',frames)