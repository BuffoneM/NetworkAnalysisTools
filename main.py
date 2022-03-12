import os
#from modules.NetworkControllerAnalyzer import runNetworkControllerAnalyzer
#import modules

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
                    
    exec(open('modules/NetworkControllerAnalyzer.py').read())
                   
    # Menu system for only integers                                   
    menuSelect = input('Enter program number: ')
    try:
        menuSelect = int(menuSelect)
    except ValueError:
        print('Input a valid integer...')
    
    if menuSelect < 0 or menuSelect > listOfFiles.count:
        print('Invalid selection...') 
    elif menuSelect == 0:
        print('Exiting...')
        exit()
        
    

                

# Main method                        
def main():
    print('\n------ Main ------')
    src = 'modules'
    selectProgram(src)   
    
    
if __name__ == '__main__':
    main()