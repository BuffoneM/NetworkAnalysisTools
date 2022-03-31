####
#
# Written by: Michael Buffone
# Specifications: Justin Poett
# Date: March 3rd, 2022
#
# This script accepts a .CSV file and returns a dataframe containing success
# or failed connections to units given an ip address.
#
##

import os
import csv
import sys
import time
import numpy as np
import pandas as pd
import multiprocessing as mp

sys.path.append(os.path.join(sys.path[0], '..'))
import Utility

# [header = 'Live Unit', 'Calculated IP']
# Read the CSV file -> open automatically closes file connection
def loadConnections(fileName):
    controllerList = []
    with open(fileName, newline = '') as csvfile:
        controllerReader = csv.DictReader(csvfile, delimiter = ',')
        for row in controllerReader:
            currController = row['Live Unit'], row['Calculated IP']
            controllerList.append(currController)
    return controllerList

# Given a controller, test it, and return
def testConnection(currController):
        success = False
        
        hostname = currController[1]
        start = time.time()
        response = os.system('ping -n 1 ' + hostname)
        end = time.time()
    
        if response == 0: 
            #print('-', hostname, 'successful connection')
            success = True
        else:
            print('X', hostname, 'failed connection')
            
        # ['Live Unit', 'Calculated IP', 'Success', 'Time']
        return currController[0], currController[1], success, (end - start)

# Main method                        
def main():
    
    # ------ Main Variables ------ #
    filePath = Utility.getFilePath('./files/*.csv')
    outputToCSV = True
    numThreads = 25
    # ---------------------------- #
    
    if filePath == None:
        print('Invalid file entered...')
        exit()

    print('Intializing loadControllers()...')
    connections = loadConnections(filePath)
    pool = mp.Pool(numThreads)
    connectionsInfo = pool.map(testConnection, connections)

    # Successful datagram print
    if connectionsInfo != []:
        dataframe = pd.DataFrame(
            data = connectionsInfo,
            columns = ['Live Unit', 'Calculated IP', 'Success', 'Time']
        )
        print('-----------------------------')
        print('----- Summary Dataframe -----')
        print('-----------------------------')
        print(dataframe)
        
        if (outputToCSV):
            newFilePath = Utility.createOutputFilePath(filePath)
            dataframe.to_csv(newFilePath)
            print('Successfully wrote to file...')

if __name__ == '__main__':
    main()