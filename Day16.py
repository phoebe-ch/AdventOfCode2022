"""
AoC 2022, Day 16

Phoebe Cheung
Jan 2, 2023
"""
# %% Part 1
file = "inputs\Day16_InputSample.txt"
lines = open(file).readlines()

class Valve:
    def __init__(self, name, rate, goesTo):
        self.name = name
        self.rate = int(rate)
        self.goesTo = goesTo.split(",")
        self.isOpen = False

def findValveObj(name):
    for valve in valves:
        if valve.name == name:
            return valve

valves = []
for row in lines:
    row = row[:-1]

    valveName,row = row.split(" has flow rate=")
    valveName = valveName[-2:]

    flowRate,row = row.split("; ")
    
    if "valves" in row:
        _,goesTo = row.split("valves ")
    elif "valve" in row:
        _,goesTo = row.split("valve ")

    valves.append(Valve(valveName,flowRate,goesTo))

maxTime = 30
timer = 1
pressureReleased = 0
while timer <= 30:
    

    timer += 1

