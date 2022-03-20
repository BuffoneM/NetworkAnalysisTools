# IdentifyDownNetworkDevices 🔧
 
A simple script that uses thread pooling to issue pings to a list of IP addresses (Plan to geo-graphed said IP's)

**main( )** -> the following can be specified:
- fileName = 'public_ip_address_varchar_45_.csv'
- outputToCSV = True
- numThreads = 25
    
**testModemConnectivity( )** -> the following can be specified:
- n for ping command is used in a Windows environment
- c for ping command is used in a UNIX environment

Results can be exported to public_ip_address_varchar_45_output.csv

# NetworkControllerAnalyzer 💻
 
A simple script that uses thread pooling to issue pings to a specified list of IP addresses (given in a .CSV file)

**main( )** -> the following can be specified:
- fileName = 'edge_controllers_down.csv'
- outputToCSV = True
- numThreads = 25
    
**testConnection( )** -> the following can be specified:
- n for ping command is used in a Windows environment
- c for ping command is used in a UNIX environment

Results can be exported to edge_controllers_down_output.csv
