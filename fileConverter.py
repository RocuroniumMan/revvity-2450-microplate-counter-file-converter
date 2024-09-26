import re
import os
import pandas as pd
"""
    Written for the revvity 2450 microplate counter data device, converts txt file output to xls.

    Dependencies: 
    pip install pandas openpyxl xlwt
        #2.2.2
    TODO: Currrently only works for 1 plate, make it work for infinite

"""

def previewTxt(filePath):
    print("Preview of txt file:")
    with open(filePath, 'r') as file:
        content = file.read()
        print(content)
        
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
def convert2xls(posData):
    print("Creating xlsx.")
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
    pivotdf = df.pivot(index='y', columns='x', values='data') #had to rearrange to get proper format
    pivotdf.to_excel('output.xlsx', index=False)  #can only be xlsx, xls engine is missing?

def main():
    wDir = os.getcwd()
    filePath = os.path.join(wDir, 'data')
    dataFolderPath = os.path.join(wDir, 'data')

    if not os.path.isdir(dataFolderPath):
        os.makedirs(dataFolderPath)
        print(f"The 'data' folder has been created at: {dataFolderPath}")

    if os.path.isdir(dataFolderPath):
        fileName = input(str("Enter the name of the file you want to convert (ex: name.txt): "))
        filePath = os.path.join(dataFolderPath, fileName)
        if os.path.isfile(filePath):
            print(f"The file '{fileName}' exists in the 'data' folder.")
            posData = getPosData(filePath)
            previewTxt(filePath)
            convert2xls(posData)
            print("Completed.")
        else:
            print(f"The file '{fileName}' does not exist in the 'data' folder.")
            # contents = os.listdir(dataFolderPath)
            # print("Contents of the 'data' folder:")
            # for item in contents:
            #     print(item)
    else:
        print("The 'data' folder does not exist in the current directory.")

if __name__ == "__main__":
    main()
