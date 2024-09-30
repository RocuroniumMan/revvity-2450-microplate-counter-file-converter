import pandas as pd

def getPosData(filePath):
    with open(filePath, 'r') as file:
        lines = file.readlines()
        #print(lines)
        storePosData = []
        for line in lines: 
            line = line.strip()

            if line.startswith("Unk_1"):
                segment = line.split('\t')
                position = segment[1]
                value = segment[2]
                posData = []
                posData.append([position,value])
                storePosData.append(posData)
                #print(position,value)

        #print(lines)
    return storePosData

#not perfect but the data is transposed correctly in xl
def convert2xls(posData,fileName):
    allData = []
    for vector in posData:
        position = vector[0][0]
        data = vector[0][1]

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

        allData.append(data)
    
    df = pd.DataFrame(allData)
    df['data'] = pd.to_numeric(df['data']) #make sure that excel recognizes the data as a number not a string
    pivotdf = df.pivot(index='y', columns='x', values='data') #had to rearrange to get proper format
    pivotdf.to_excel(f'{fileName}.xlsx', index=False)  #can only be xlsx, xls engine is missing?