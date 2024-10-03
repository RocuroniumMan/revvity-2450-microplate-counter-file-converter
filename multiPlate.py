import pandas as pd
#TODO remove singleplate, do everything in a single file
#Seems that doing this with arrays is a bad idea, so move this into an object

#returns 2d array containing the data per plate
def getPosData(numberPlates, filePath):
    allPosData = []
    with open(filePath, 'r') as file:
        lines = file.readlines()
        for i in range(numberPlates):
            storePosData = []
            for line in lines: 
                line = line.strip()
                if line.startswith(f"Unk_{i+1}"):
                    segment = line.split('\t')
                    position = segment[1]
                    value = segment[2]
                    posData = [[position, value]]  
                    storePosData.append(posData)
            allPosData.append(storePosData) 
    return allPosData


def convert2xls(allPosData, fileName):
    for plate in allPosData:
        plateData = []
        for vec in plate:
            position = vec[0][0]
            data = vec[0][1]
            alpha = ""
            number = ""

            for char in position:
                if char.isalpha():
                    alpha += char
                elif char.isdigit():
                    number += char
                
            data = {
                'data': data,
                'y' : alpha,
                'x' :number
            }   

            plateData.append(data)
        
        df = pd.DataFrame(plateData)
        df['data'] = pd.to_numeric(df['data']) #make sure that excel recognizes the data as a number not a string
        pivotdf = df.pivot(index='y', columns='x', values='data') #had to rearrange to get proper format
        pivotdf.to_excel(f'{fileName}.xlsx', index=False)  #can only be xlsx, xls engine is missing?