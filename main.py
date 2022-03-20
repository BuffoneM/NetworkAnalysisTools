import os

def selectProgram(src):
    dirCount = 0
    listOfFiles = []
    print('( 0 ) - Exit program')
    for (dirPath, dirNames, files) in os.walk(src):
        for fileName in files:
            if fileName.endswith('.py'):
                dirCount += 1
                listOfFiles.append(os.path.join(dirPath, fileName))
                print('(', dirCount, ') -', fileName)                                        
        
    # Menu system for only integers                                   
    menuSelect = input('Enter program number: ')
    try:
        menuSelect = int(menuSelect)
    except ValueError:
        print('Input a valid integer...')
        exit()
    
    if menuSelect < 0 or menuSelect > dirCount:
        print('Invalid selection...') 
    elif menuSelect == 0:
        print('Exiting...')
        exit()
    else:
        execStatement = 'python ' + listOfFiles[0 + 1]
        os.system(execStatement)
             
# Main method                        
def main():
    print('\n------ Main ------')    
    src = 'modules'
    selectProgram(src)
    
    
if __name__ == '__main__':
    main()