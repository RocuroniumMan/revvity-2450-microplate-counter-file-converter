import os
import singlePlate as sp
import multiPlate as mp
"""
    Written for the revvity 2450 microplate counter data device, converts txt file output to xlsx.

    Dependencies: 
    pip install pandas openpyxl xlwt
        #2.2.2
    pip install openpyxl
        #3.1.5
    pip install XlsxWriter
        #3.2.0

    TODO: Currrently only works for 1 plate, make it work for infinite

"""

def previewTxt(filePath):
    print("Preview of txt file:")
    with open(filePath, 'r') as file:
        content = file.read()
        print(content)
        
def findTotalPlates(filePath):
    with open(filePath, 'r') as file:
        lines = file.readlines()
        numberOfPlates = []
        for line in lines: 
            line = line.strip()

            if line.startswith("End of plate "):
                number = ''
                for char in line: 
                    if char.isdigit():
                        number += char
                if number:
                    numberOfPlates.append(int(number))
    
    totalNumberOfPlates = max(numberOfPlates)
    return totalNumberOfPlates
                
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
            fileName = fileName.rstrip(".txt")
            print(f"Creating {fileName}.xlsx")
            #previewTxt(filePath)
            totalNumberOfPlates = findTotalPlates(filePath)
            if totalNumberOfPlates == 1:
                posData = mp.getPosData(totalNumberOfPlates,filePath)
                mp.convert2xls(posData,fileName)
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
