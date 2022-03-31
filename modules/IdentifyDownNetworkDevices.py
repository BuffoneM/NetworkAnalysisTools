####
#
# Written by: Michael Buffone
# Specifications: Justin Poett
# Date: March 19th, 2022
#
# This script accepts a .CSV file and returns a dataframe containing success
# or failed connections to units given a file of ip addresses.
#
##

import os
import sys
import time
import multiprocessing as mp

sys.path.append(os.path.join(sys.path[0], '..'))
import Utility

# Accept an IP address and attempt to ping it
def testModemConnectivity(currIP):
    success = False
    
    start = time.time()
    response = os.system('ping -n 1 ' + currIP)
    end = time.time()

    if response == 0: 
        #print('-', currIP, 'successful connection')
        success = True
    else:
        print('X', currIP, 'failed connection')
        
    # ['Calculated IP', 'Success', 'Time']
    return currIP, success, (end - start) 

# Main method                        
def main():
     
    # ------ Main Variables ------ #
    filePath = Utility.getFilePath('./files/*.csv')
    numThreads = 25
    # ---------------------------- #
    
    if filePath == None:
        print('Invalid file entered...')
        return

    print('Intializing loadConnections()...')
    # -Testing purposes-
    #connections = loadConnections(filePath)[:50]
    connections = Utility.loadConnections_IP_Header(filePath)
    pool = mp.Pool(numThreads)
    connectionsInfo = pool.map(testModemConnectivity, connections)
    
    columns = ['Calculated IP', 'Success', 'Time']
    dataframe = Utility.generateDataFrame('identifydownnetworkdevices', filePath, connectionsInfo, columns)
    
    print('Ping summary:')
    print(dataframe.Success.value_counts(), '\n')
    print(dataframe)

if __name__ == '__main__':
    main()