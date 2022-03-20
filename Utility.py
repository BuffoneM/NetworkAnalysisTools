
import os
import glob

# Return filePath if it exists
def getFilePath():
    print('\n--- File List---')
    for file in glob.glob('./files/*.csv'):
        print(file)
        
    fileName = input('\nInput file name: ')
    
    filePath = './files/' + fileName
    if (not os.path.exists(filePath)):
        return None
        
    return filePath

# Return new filePath with _output appended
def createOutputFilePath(filePath):
    return filePath.replace('.csv', '_output.csv')