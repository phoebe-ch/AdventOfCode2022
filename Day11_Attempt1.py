"""
AoC 2022, Day 11

Phoebe Cheung
Dec 10, 2022

Pt 1: Complete
Pt 2: Incomplete. Code rewritten to improve processing speed.
I can get the right answer for pt 1 with this new code, but can't seem to get it right for pt 2??
Using sample input, round 1 is correct, but round 20 is off. I get [99,97,10,103] rather than [99,97,8,103].
"""
# %% Part 1
file = "inputs\Day11_Input.txt"
lines = open(file).readlines()

monkeys = []

class Monkey:
    def __init__(self, items, operation, divTest, testTrue, testFalse):
        self.items = items
        self.operation = operation
        self.divTest = divTest
        self.testTrue = testTrue
        self.testFalse = testFalse
        self.inspected = 0

def throw(fromM,toM,item):
    toM.items.append(item)
    fromM.items.pop(0)
    return 0

def monkeyOp(operation,old):
    if "old" in operation:
        new = old * old
    elif operation[0] == "*":
        new = old * int(operation[2:])
    elif operation [0] == "+":
        new = old + int(operation[2:])
    else:
        print("add a new condition")
    return new

i = 0
while i < len(lines):
    i += 1
    _,items = lines[i].split("Starting items: ")
    items = [int(x) for x in items[:-1].split(", ")]
    i += 1
    _,operation = lines[i].split("Operation: new = old ")
    operation = operation[:-1]
    i += 1
    _,divTest = lines[i].split("Test: divisible by ")
    divTest = int(divTest[:-1])
    i += 1
    _,testTrue = lines[i].split("If true: throw to monkey ")
    testTrue = int(testTrue[:-1])
    i += 1
    _,testFalse = lines[i].split("If false: throw to monkey ")
    testFalse = int(testFalse[:-1])
    i += 2
    monkeys.append(Monkey(items,operation,divTest,testTrue,testFalse))

round = 1
rounds = 20
while round <= rounds: # loop for each round 
    for i,monkey in enumerate(monkeys): # loop for each monkey
        numItems = len(monkey.items)
        j = 0
        while j < numItems: # loop for each item
            monkey.inspected += 1
            monkey.items[0] = monkeyOp(monkey.operation,monkey.items[0])
            monkey.items[0] = monkey.items[0] // 3
            if monkey.items[0] % monkey.divTest == 0:
                throw(monkey,monkeys[monkey.testTrue],monkey.items[0])
            else:
                throw(monkey,monkeys[monkey.testFalse],monkey.items[0])
            j += 1
    round += 1

inspectedArr = []
for monkey in monkeys:
    inspectedArr.append(int(monkey.inspected))
inspectedArr.sort()
print(inspectedArr[-1]*inspectedArr[-2])


# %% Part 2
import numpy as np
file = "inputs\Day11_InputSample.txt"
lines = open(file).readlines()

monkeys = []

class Monkey:
    __slots__ = ('items','operationType','operationVal','divTest','testTrue','testFalse','inspected')
    def __init__(self, items, operationType, operationVal, divTest, testTrue, testFalse):
        self.items = np.array(items)
        self.operationType = operationType
        self.operationVal = operationVal
        self.divTest = divTest
        self.testTrue = testTrue
        self.testFalse = testFalse
        self.inspected = 0

def monkeyOp(operation):
    if operation[0] == "*":
        opType = '*'
        if "old" in operation:
            opVal = 'self'
        else:
            opVal = int(operation[2:])
    elif operation [0] == "+":
        opType = '+'
        if "old" in operation:
            opVal = 'self'
        else:
            opVal = int(operation[2:])
    return opType,opVal

i = 0
while i < len(lines):
    i += 1
    _,items = lines[i].split("Starting items: ")
    items = [int(x) for x in items[:-1].split(", ")]
    i += 1
    _,operation = lines[i].split("Operation: new = old ")
    operation = operation[:-1]
    operationType,operationVal = monkeyOp(operation)
    i += 1
    _,divTest = lines[i].split("Test: divisible by ")
    divTest = int(divTest[:-1])
    i += 1
    _,testTrue = lines[i].split("If true: throw to monkey ")
    testTrue = int(testTrue[:-1])
    i += 1
    _,testFalse = lines[i].split("If false: throw to monkey ")
    testFalse = int(testFalse[:-1])
    i += 2
    monkeys.append(Monkey(items,operationType,operationVal,divTest,testTrue,testFalse))

round = 1
rounds = 20
while round <= rounds: # loop for each round
    for monkey in monkeys: # loop for each monkey
        numItems = len(monkey.items)
        monkey.inspected += numItems
        if numItems > 0:
            if monkey.operationType == '+' and monkey.operationVal != 'self':
                monkey.items += monkey.operationVal                
            elif monkey.operationType == '*' and monkey.operationVal != 'self':
                monkey.items *= monkey.operationVal
            elif monkey.operationType == '*' and monkey.operationVal == 'self':
                monkey.items *= monkey.items
            else:
                print('yikes')
            monkeys[monkey.testTrue].items = np.append(monkeys[monkey.testTrue].items,monkey.items[monkey.items % monkey.divTest == 0])
            monkeys[monkey.testFalse].items = np.append(monkeys[monkey.testFalse].items,monkey.items[monkey.items % monkey.divTest != 0])
            monkey.items = np.empty(0)
    # print(round)
    round += 1

inspectedArr = []
for monkey in monkeys:
    # print(monkey.items)
    inspectedArr.append(int(monkey.inspected))
print(inspectedArr)
inspectedArr.sort()
print(inspectedArr[-1]*inspectedArr[-2])