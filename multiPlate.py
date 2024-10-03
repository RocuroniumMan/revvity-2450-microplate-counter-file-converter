import pandas as pd
#TODO remove singleplate, do everything in a single file
#Seems that doing this with arrays is a bad idea, so move this into an object

#returns 2d array containing the data per plate
def getPosData(numberPlates, filePath):
    allPosData = []
    i = 1
    with open(filePath, 'r') as file:
        lines = file.readlines()
        for i in range(numberPlates):
            storePosData = []
            for line in lines: 
                line = line.strip()
                if line.startswith(f"Unk_{i}"):
                    segment = line.split('\t')
                    position = segment[1]
                    value = segment[2]
                    posData = [[position, value]]  
                    storePosData.append(posData)
            allPosData.append(storePosData) 
    return allPosData


def convert2xls(allPosData, fileName):
    pass