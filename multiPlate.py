import pandas as pd
#TODO remove singleplate, do everything in a single file

#returns 2d array containing the data per plate
def getPosData(numberPlates,filePath):
    allPosData = []
    i = 0
    with open(filePath, 'r') as file:
        lines = file.readlines()
        #print(lines)
        storePosData = []
        for line in lines: 
            line = line.strip()
            for i in range(i,numberPlates):
                if line.startswith(f"Unk_{i}"):
                    segment = line.split('\t')
                    position = segment[1]
                    value = segment[2]
                    posData = []
                    posData.append([position,value])
                    storePosData.append(posData)
                    #print(position,value)
                allPosData.append(storePosData)
        #print(lines)
    return allPosData


def convert2xls(numberPlates,fileName,filePath):
    allPosData = getPosData(numberPlates,filePath)
    