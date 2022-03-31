####
#
# Written by: Michael Buffone
# Specifications: Justin Poett
# Date: March 31st, 2022
#
# This script creates a map given IP addresses.
#
# Dependencies:
# -ip2geotools@0.1.6
#
##

import os
import sys
import multiprocessing as mp

from ip2geotools.databases.noncommercial import DbIpCity

sys.path.append(os.path.join(sys.path[0], '..'))
import Utility

def parseIPData(currIP):
    response = DbIpCity.get(currIP, api_key='free')
    # ['IP', 'City', 'Region', 'Country', 'Latitude', 'Longitude' ]
    return response.to_json()

# Main method                        
def main():
     
    # ------ Main Variables ------ #
    filePath = Utility.getFilePath('./files/*.csv')
    numThreads = 1
    # ---------------------------- #
    
    if filePath == None:
        print('Invalid file entered...')
        return

    print('Intializing parseIPData()...')
    connections = Utility.loadConnections_IP_Header(filePath)
    connections = connections[:1]
    pool = mp.Pool(numThreads)
    ipGeoData = pool.map(parseIPData, connections)
    print(ipGeoData)


if __name__ == '__main__':
    main()