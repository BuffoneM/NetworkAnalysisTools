####
#
# Written by: Michael Buffone
# Specifications: Justin Poett
# Date: March 30th, 2022
#
# This script attempts an SSH connection to a given device.
#
# Dependencies:
# -Paramiko@2.10.3
#
##

import os
import re
import csv
import sys
import time
import paramiko
import multiprocessing as mp

sys.path.append(os.path.join(sys.path[0], '..'))
import Utility

# [header = "IP"]
# Read the CSV file -> open automatically closes file connection
def loadConnections(fileName):
    controllerList = []
    with open(fileName, newline = '') as csvfile:
        controllerReader = csv.DictReader(csvfile, delimiter = ',')
        for row in controllerReader:
            currController = row['IP']
            controllerList.append(currController)
    return controllerList

# Accept an IP address and attempt to SSH
def attemptSSH(currIP):
    success = False
    findMount = [None] * 5
    
    port = 22
    username = "pi"
    password = "blah"
    command = "df /foobar"
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    start = time.time()
    try:
        ssh.connect(currIP, port, username, password)
        stdin, stdout, stderr = ssh.exec_command(command)
        
        for line in stdout.readlines():
            if '/dev/' in line:
                findMount = re.split(' +', line)
                break
        
        #print('-', currIP, 'successful SSH') 
        success = True
    except Exception as e:
        print('X', currIP, 'failed SSH')
        pass
    end = time.time()

    # ['IP', 'Success', fileSystem, oneKBlocks, used, available, mountedOn 'Time']
    return currIP, success, findMount[0], findMount[1], findMount[2], findMount[3], findMount[4], (end - start)

# Main method                        
def main():
    
    # ------ Main Variables ------ #
    filePath = Utility.getFilePath('./files/*.csv')
    numThreads = 25
    # ---------------------------- #
    
    if filePath == None:
        print('Invalid file entered...')
        exit()

    print('Intializing attemptSSH()...')
    connections = loadConnections(filePath)
    pool = mp.Pool(numThreads)
    connectionsInfo = pool.map(attemptSSH, connections)

    columns = ['IP', 'Success', 'FileSystem', 'oneKBlocks', 'Used', 'Available', 'MountedOn', 'Time']
    Utility.generateDataFrame('sshconnect', filePath, connectionsInfo, columns)


if __name__ == '__main__':
    main()