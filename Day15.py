"""
AoC 2022, Day 15

Phoebe Cheung
Dec 30, 2022 - Jan 2, 2023

Part 1: Completed.
Part 2: Completed. My code would be slow if it were to iterate through every possible
row that the beacon would be in. As a result, Attempt 2 plots the possible space, showing
the bounds of each sensor. By visually inspecting the plot, I was able to locate several
possible regions where the beacon might be (intersections, seemingly overlapping edges
since everything is very zoomed out). Knowing the approximate regions allowed me to 
run the slow code but only iterate through < 500 lines. Got it on the 8th suspected region!
"""
# %% Part 1
import matplotlib.pyplot as plt
import numpy as np

file = "inputs\Day15_Input.txt"
lines = open(file).readlines()

class Sensor:
    def __init__(self, sx, sy, bx, by):
        self.sx = sx
        self.sy = sy
        self.bx = bx
        self.by = by
        self.dist = abs(sx-bx)+abs(sy-by)

def calcNoBeacon(targetY,reading):
    noBeaconX = []
    yDiff = abs(targetY-reading.sy)
    noBeaconX = np.arange(reading.sx-(reading.dist-yDiff),reading.sx+(reading.dist-yDiff)+1,1)
    if targetY == reading.by:
        # if beacon in target row, remove from noBeaconX array
        noBeaconX = np.setdiff1d(noBeaconX,reading.bx)
    return noBeaconX

readings = []
for row in lines:
    sensorLoc,beaconLoc = row.split(": ")
    sensorX,sensorY = sensorLoc.split(", y=")
    _,sensorX = sensorX.split("=")
    sensorX,sensorY = int(sensorX),int(sensorY)
    beaconX,beaconY = beaconLoc.split(", y=")
    _,beaconX = beaconX.split("=")
    beaconX,beaconY = int(beaconX),int(beaconY)

    readings.append(Sensor(sensorX,sensorY,beaconX,beaconY))

noBeacon = np.empty(0)
targetY = 2000000
for reading in readings:
    plt.scatter(reading.sx,reading.sy,marker="*",c='r')
    plt.scatter(reading.bx,reading.by,marker=".",c='g')
    noBeacon = np.append(noBeacon,calcNoBeacon(targetY,reading))

plt.grid(True)
plt.axis("equal")
plt.show()

noBeacon = np.unique(noBeacon)
print(len(noBeacon))


# %% Part 2 Attempt 1 (slow)
import matplotlib.pyplot as plt
import numpy as np

file = "inputs\Day15_Input.txt"
lines = open(file).readlines()

class Sensor:
    def __init__(self, sx, sy, bx, by):
        self.sx = sx
        self.sy = sy
        self.bx = bx
        self.by = by
        self.dist = abs(sx-bx)+abs(sy-by)

def calcNoBeacon(targetY,reading):
    noBeaconX = []
    yDiff = abs(targetY-reading.sy)
    noBeaconX = np.arange(reading.sx-(reading.dist-yDiff),reading.sx+(reading.dist-yDiff)+1,1)
    noBeaconX = noBeaconX[np.where(noBeaconX>=0)]
    noBeaconX = noBeaconX[np.where(noBeaconX<=maxVal)]
    return noBeaconX

def calcBeacon(targetY,reading):
    beaconX = []
    yDiff = abs(targetY-reading.sy)
    beaconXLeft = np.arange(0,reading.sx-(reading.dist-yDiff),1)
    beaconXRight = np.arange(reading.sx+(reading.dist-yDiff)+1,maxVal+1,1)
    beaconX = np.append(beaconXLeft,beaconXRight)
    return beaconX

readings = []
for row in lines:
    sensorLoc,beaconLoc = row.split(": ")
    sensorX,sensorY = sensorLoc.split(", y=")
    _,sensorX = sensorX.split("=")
    sensorX,sensorY = int(sensorX),int(sensorY)
    beaconX,beaconY = beaconLoc.split(", y=")
    _,beaconX = beaconX.split("=")
    beaconX,beaconY = int(beaconX),int(beaconY)

    readings.append(Sensor(sensorX,sensorY,beaconX,beaconY))

maxVal = 4000000
freqMultiplier = 4000000

y = 0
xRange = np.arange(0,maxVal+1,1)
while y <= maxVal:

    beaconX = xRange
    subtract = np.empty(0)
    for reading in readings:
        subtract = np.append(subtract,calcNoBeacon(y,reading))

    subtract = np.unique(subtract)

    if len(subtract) == maxVal:
        x = int(np.setdiff1d(beaconX,subtract))
        print([x,y])
        print(int(x*freqMultiplier+y))
        y = maxVal+1

    # beaconX = np.empty(0)
    # for reading in readings:
    #     beaconX = np.append(beaconX,calcBeacon(y,reading))

    # noBeaconX = set(noBeaconX)
    # noBeaconX = np.array(list(noBeaconX))

    print(str(y)+ " of " + str(maxVal))

    y += 1 

# %% Part 2 Attempt 2 (still slow but completed visually)
import matplotlib.pyplot as plt
import numpy as np

file = "inputs\Day15_Input.txt"
lines = open(file).readlines()

class Sensor:
    def __init__(self, sx, sy, bx, by):
        self.sx = sx
        self.sy = sy
        self.bx = bx
        self.by = by
        self.dist = abs(sx-bx)+abs(sy-by)
        self.ytop = sy+self.dist
        self.ybottom = sy-self.dist
        self.xleft = sx-self.dist
        self.xright = sx+self.dist

def calcNoBeacon(targetY,reading):
    noBeaconX = []
    yDiff = abs(targetY-reading.sy)
    noBeaconX = np.arange(reading.sx-(reading.dist-yDiff),reading.sx+(reading.dist-yDiff)+1,1)
    noBeaconX = noBeaconX[np.where(noBeaconX>=0)]
    noBeaconX = noBeaconX[np.where(noBeaconX<=maxVal)]
    return noBeaconX

readings = []
for row in lines:
    sensorLoc,beaconLoc = row.split(": ")
    sensorX,sensorY = sensorLoc.split(", y=")
    _,sensorX = sensorX.split("=")
    sensorX,sensorY = int(sensorX),int(sensorY)
    beaconX,beaconY = beaconLoc.split(", y=")
    _,beaconX = beaconX.split("=")
    beaconX,beaconY = int(beaconX),int(beaconY)

    readings.append(Sensor(sensorX,sensorY,beaconX,beaconY))

plt.figure(dpi=1200)
colour = iter(plt.cm.rainbow(np.linspace(0, 1, 32)))
for j,reading in enumerate(readings):
    xVals = [reading.sx,reading.sx,reading.xleft,reading.sx,reading.xright,reading.sx,reading.xright,reading.sx,reading.xleft]
    yVals = [reading.sy,reading.ytop,reading.sy,reading.ybottom,reading.sy,reading.ytop,reading.sy,reading.ybottom,reading.sy]
    
    c = next(colour)
    i = 1
    while i < len(xVals)-1:
        plt.scatter(reading.sx,reading.sy,marker="*",c='r')
        plt.plot(xVals[i-1:i+1],yVals[i-1:i+1],c=c,linewidth=0.5)
        i += 1

plt.grid(True)
plt.axis("square")
plt.ylim([2.63645e6,2.6365e6])
plt.xlim([3.129e6,3.13e6])
plt.show()

maxVal = 4000000
freqMultiplier = 4000000

y = 2.636474e6
#checked 3.415e6 to 3415870
#checked 1.9097e6 to 1.909772e6
#checked 2.128e6 to 2128432
#checked 2.1447e6 to 2144783
#checked 2.3895e6 to 2.3896e6
#checked 2.4145e6 to 2.4146e6
#checked 3.521e6 to 3521136
#checked 2.63645e6 to 2.6365e6
xRange = np.arange(0,maxVal+1,1)
while y <= maxVal:

    beaconX = xRange
    subtract = np.empty(0)
    for reading in readings:
        subtract = np.append(subtract,calcNoBeacon(y,reading))

    subtract = np.unique(subtract)

    if len(subtract) == maxVal:
        x = int(np.setdiff1d(beaconX,subtract))
        print([x,y])
        print(int(x*freqMultiplier+y))
        y = maxVal+1

    print(str(y)+ " of " + str(maxVal))

    y += 1 

