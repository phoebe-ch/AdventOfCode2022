"""
AoC 2022, Day 7 [Attempt 1: incomplete]

Phoebe Cheung
Dec 7, 2022

Pt 1: incomplete; 1502118 too low, 1667240 too high

Turns out the folder names are NOT unique. Need to find another way of doing this.
"""
# %% Part 1
file = "inputs\Day7_Input.txt"
with open(file) as f:
    lines = f.readlines()

class Folder:
    def __init__(self, name, level, folders, fileSize, allFileSize):
        self.name = name
        self.level = level
        self.folders = folders
        self.fileSize = fileSize
        self.allFileSize = allFileSize

def extractFileName(row):
    cmd, name = row.split("$ cd ")
    return name[:-1]

def extractContents(currentFolder):
    totalFileSize = 0
    totalFolders = []
    for list in currentFolder:
        if "dir" in list:
            cmd, folder = list.split(" ")
            folder = folder[:-1]
            totalFolders.append(folder)
        elif "$" not in list:
            fileSize, fileName = list.split(" ")
            totalFileSize += int(fileSize)
    return totalFileSize,totalFolders

def readCommands(row,level):
    if "/" in row:
        level = 0
    elif ".." in row:
        level -= 1
    else:
        level += 1
    return level

def strToObjName(str,allFolders):
    for idx,searchFolder in enumerate(allFolders):
        if allFolders[idx].name == str:
            folderObject = searchFolder
            break
    return folderObject

def flatten(A):
    rt = []
    for i in A:
        if isinstance(i,list): rt.extend(flatten(i))
        else: rt.append(i)
    return rt

def findSubFolders(current,allFolders):
    subFolders = []
    newSubFolders = []
    foldersToCheck = current.folders
    if len(foldersToCheck) > 0:
        for foldersStr in foldersToCheck:
            subFolders.append(strToObjName(foldersStr,allFolders))
        newSubFolders = subFolders
    while newSubFolders != []:
        newSubFolders = []
        for foldersObj in newSubFolders:
            newFoldersToCheck = foldersObj.folders
            if len(newFoldersToCheck) > 0:
                for newFoldersStr in newFoldersToCheck:
                    newSubFolders.append(strToObjName(newFoldersStr,allFolders))
                    subFolders.append(strToObjName(newFoldersStr,allFolders))
    
    return subFolders

threshold = 100000
idx = 0
level = 0
allFolders = []
folderName = "/"

while idx < len(lines):
    row = lines[idx]
    if "$ cd" in row:
        level = readCommands(row,level)
        if ".." not in row and "/" not in row:
            folderName = extractFileName(row)
        idx += 1
    elif "$ ls" in row and idx < len(lines):
        contentsList = []

        while True and idx < len(lines)-1:
            idx += 1
            row = lines[idx]            
            contentsList.append(row)
            if "$" in row:
                break
        folderFileSize,totalFolders = extractContents(contentsList)
        newFolder = Folder(name=folderName,level=level,folders=totalFolders,fileSize=folderFileSize,allFileSize=0)
        allFolders.append(newFolder)
    else:
        break

totalFileSize = 0
for currentFolder in allFolders:
    subFolders = findSubFolders(currentFolder,allFolders)
    print(currentFolder.name)
    currentFolderAllSize = currentFolder.fileSize
    print(currentFolder.fileSize)
    for folder in subFolders:
        print(folder.name)
        print(folder.fileSize)
        currentFolderAllSize += folder.fileSize
    currentFolder.allFileSize = currentFolderAllSize
    print(currentFolder.allFileSize)
    print("")
for currentFolder in allFolders:
    if currentFolder.fileSize < threshold:
        totalFileSize += currentFolder.fileSize

print(totalFileSize)