import os
import sys

sys.path.append(os.path.join(sys.path[0], '..'))
import Utility

def selectProgram():
    filePath = Utility.getFilePath('./modules/*.py')
    
    if filePath == None:
        print('Invalid file entered...')
        return
        
    execStatement = 'python ' + filePath
    os.system(execStatement)
             
# Main method                        
def main():
    print('\n------ Main ------')
    while True:    
        selectProgram()
        input("Press Enter to continue...")
    
if __name__ == '__main__':
    main()