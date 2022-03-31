import glob

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
        print('Input a valid integer...')
        exit()
    
    if menuSelect < 0 or menuSelect > dirCount:
        print('Invalid selection...')
        return None 
    elif menuSelect == 0:
        print('Exiting...')
        exit()
    else:
        return listOfFiles[menuSelect - 1]

# Return new filePath with _output appended
def createOutputFilePath(filePath):
    return filePath.replace('.csv', '_output.csv')