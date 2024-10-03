import pandas as pd

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
    try:
        with pd.ExcelWriter(f'{fileName}.xlsx') as writer:
            for index, plate in enumerate(allPosData):
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

                    data_entry = {
                        'data': data,
                        'y': alpha,
                        'x': number
                    }   

                    plateData.append(data_entry)

                df = pd.DataFrame(plateData)
                df['data'] = pd.to_numeric(df['data']) #make sure that excel recognizes the data as a number not a string
                pivotdf = df.pivot(index='y', columns='x', values='data')  #had to rearrange to get proper format
                pivotdf.to_excel(writer, sheet_name=f'Plate{index + 1}', index=False) #can only be xlsx, xls engine is missing?
    except Exception as e:
        print(f"Failed to write xlsx file: {e}")