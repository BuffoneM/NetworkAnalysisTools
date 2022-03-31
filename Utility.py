import csv
import glob
import numpy as np
import pandas as pd

# Return filePath if it exists, otherwise None
def getFilePath(src):
    dirCount = 0
    listOfFiles = []
    print('\n--- File List ---')
    print('( 0 ) - Exit program')
    for file in glob.glob(src):
        dirCount += 1
        listOfFiles.append(file)
        print('(', dirCount, ') -', file)                                        

    menuSelect = input('\nInput selection: ')
    
    try:
        menuSelect = int(menuSelect)
    except ValueError:
        return None
    
    if menuSelect < 0 or menuSelect > dirCount:
        print('Invalid selection...')
        return None 
    elif menuSelect == 0:
        print('Exiting...')
        exit()
    else:
        return listOfFiles[menuSelect - 1]

# Return new filePath with _output appended
def createOutputFilePath(filePath, programName):
    return filePath.replace('.csv', ('_' + programName + '_output.csv'))

# Output data to file
def generateDataFrame(programName, filePath, userData, userColumns):
    # Successful datagram print
    if userData != []:
        dataframe = pd.DataFrame(
            data = userData,
            columns = userColumns
        )
        print('-----------------------------')
        print('----- Summary Dataframe -----')
        print('-----------------------------')
        print(dataframe)
        
        newFilePath = createOutputFilePath(filePath, programName)
        dataframe.to_csv(newFilePath)
        print('Successfully wrote to file...')
        
        return dataframe
    
# Load connections given ['IP'] header file
# [header = "IP"]
# Read the CSV file -> open automatically closes file connection
def loadConnections_IP_Header(fileName):
    controllerList = []
    with open(fileName, newline = '') as csvfile:
        controllerReader = csv.DictReader(csvfile, delimiter = ',')
        for row in controllerReader:
            currController = row['IP']
            controllerList.append(currController)
    return controllerList