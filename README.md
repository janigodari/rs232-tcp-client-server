#### RS232 & TCP Client/Server

RS232 & TCP Client/Server is a university project with the scope of working with CSV files,creating graphs, serial ports & tcp. The purpose  of this app is to take Data.csv file and extract the date into different csv files containing specific data like Temperature, Speed etc. Creating graphs from the newly created csv files.  You can print the data inside all the csv files, including Data.csv.  Data can be received from a TCP server and be saved into RS232.csv & data can be sent back to the TCP client. The sent data is taken from a RS232.csv and then displayed on the TCP client 

To use all the features of this application it should be run on Windows. The RS232 & TCP Client/Server is designed to be used with Windows only software [ Hercules & HW VSP3]

It can also run on other system if an alternative is found for those 2 applications mentioned above.

##### Requirements

- Python

- [Hercules ](https://www.hw-group.com/software/hercules-setup-utility)

- [HW VSP3 - Virtual Serial Port](https://www.hw-group.com/software/hw-vsp3-virtual-serial-port)

###### Required Libraries

```python
pip install PySimpleGUI
pip install matplotlib
pip install pyserial
```

#### Setup

1. Open terminal and run `ipconfig` 

2. Look for IPv4 Address on Ethernet or Wireless & copy it

3. Open HW Virtual Serial Port and clink on the Login button and click Ok when prompted for admin access
   
   - Port Name should be the same as within the python application COM7  ` serialPort=serial.Serial('COM7', baudrate=115200) ` as seen here, but you can change if you want
   
   - IP Address should be the IPv4 Address that we got from the ipconfig command
   
   - Port should be 9999 , but it can be changed within the code
   
   - Then click Create COM

4. Open Hercules program
   
   - Go to TCP Server tab and enter port 9999 and click listen
   
   - Go to TCP Client tab and Modify Module IP and Port with IPv4 Address and port 9999
   
   - Click connect, and make sure that on your left it displays a message that is connected

5. Run main.py



If application is not connecting to the tcp client/server change `host = "localhost"` to ` host = "<IPv4 Address>"`  
