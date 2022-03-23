import csv
from fileinput import filename
import matplotlib.pyplot as plt
import serial
import time
import queue as q
from datetime import datetime
import PySimpleGUI as sg
import os
import socket

fileName = ""
temperatura = "temperatura.csv"
umiditate = "umiditate.csv"
prezenta = "prezenta.csv"
viteza = "viteza.csv"

def fileCreate():

    files = [temperatura, umiditate, prezenta, viteza]
    for file in files:
        makeEmpty = csv.writer(open(file, 'wb'))

    with open(fileName, 'r', newline='') as csvfile:
        catalog_read = csv.reader(csvfile, delimiter=',',quotechar='|')
        for row in catalog_read:
            try:
                for i in range(0,3):
                    if float(row[i]) <- 5:
                        row[i] = -5
                    elif float(row[i]) > 5:
                        row[i] = 5
            except:
                pass
            try:
                for i in range(3,6):
                    if float(row[i]) > 80:
                        row[i] = 80
            except Exception as e:
                pass

            for i in range(0,4):
                with open(files[i], 'a', newline='') as csvfile:
                    csv_write = csv.writer(csvfile, delimiter=',' ,quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    if i == 0:
                        csv_write.writerow([row[0],row[1],row[2],row[9]])
                    elif i == 1:
                        csv_write.writerow([row[3],row[4],row[5],row[9]])
                    elif i == 2:
                        csv_write.writerow([row[7],row[8],row[9]])
                    else:
                        csv_write.writerow([row[6],row[9]])

def displayData(choice):
    if(choice == 1):
        with open(fileName, 'r', newline='') as csvfile:
            catalog_read = csv.reader(csvfile, delimiter=',',quotechar='|')
            for row in catalog_read:
                print("Temperaturi: ", row[0], "," ,row[1], "," ,row[2], " la ora ", row[9])

    elif(choice == 2):
        with open(fileName, 'r', newline='') as csvfile:
            catalog_read = csv.reader(csvfile, delimiter=',',quotechar='|')
            for row in catalog_read:
                print("Umiditate : ", row[3], "," ,row[4], "," ,row[5], " la ora ", row[9])

    elif(choice == 3):
        with open(fileName, 'r', newline='') as csvfile:
            catalog_read = csv.reader(csvfile, delimiter=',',quotechar='|')
            for row in catalog_read:
                print("Viteza  : ", row[6], "la ora ", row[9])

    elif(choice == 4):
         with open(fileName, 'r', newline='') as csvfile:
            catalog_read = csv.reader(csvfile, delimiter=',',quotechar='|')
            for row in catalog_read:
                print("Prezenta  : ", row[7], "," ,row[8])

    elif(choice == 5):
        with open(fileName, 'r', newline='') as csvfile:
            catalog_read = csv.reader(csvfile, delimiter=',',quotechar='|')
            for row in catalog_read:
                print(row)

    elif(choice == 6):
       graphDisplay=displayGraphs()
       graphDisplay.runGraphs()

    elif(choice == 7):
        RS232Conncetion()

    elif(choice == 8):
        RS232DataLog(RS232Conncetion())

    elif(choice == 9):
       TcpTransmisson()
    
class displayGraphs():
    def runGraphs(self):
        x=[]
        y=[]
        z=[]
        w=[]
        with open('temperatura.csv', 'r') as csvfile:
            date = csv.reader(csvfile, delimiter=',')
            for row in date:
                try:
                    y.append(float(row[0]))
                    z.append(float(row[1]))
                    w.append(float(row[2]))
                    x.append(row[3])
                except Exception as e:
                    pass

        plt.figure(1)

        plt.plot(x,z, label='Temperatura 2!')
        plt.plot(x,y, label='Temperatura 1!')
        plt.plot(x,w, label='Temperatura 3!')

        plt.xlabel('Timp')
        plt.ylabel('Temperatura')
        plt.title('Temperatura(Timp)')
        plt.legend()

        plt.xticks([0,50,99])


        a=[]
        b=[]
        c=[]
        d=[]

        with open('umiditate.csv', 'r') as csvfile:
            date = csv.reader(csvfile, delimiter=',')
            for row in date:
                try:
                    b.append(float(row[0]))
                    c.append(float(row[1]))
                    d.append(float(row[2]))
                    a.append(row[3])
                except Exception as e:
                    pass
        
        plt.figure(2)
        plt.plot(a,c, label='Umididitate 1!')
        plt.plot(a,b, label='Umididitate 2!')
        plt.plot(a,d, label='Umididitate 3!')
        plt.xlabel('Timp')
        plt.ylabel('Umiditate %')
        plt.title('Umiditate(Timp)')
        plt.legend()
        plt.xticks([0,50,99])

        e=[]
        f=[]
        g=[]


        with open('umiditate.csv', 'r') as csvfile:
            date = csv.reader(csvfile, delimiter=',')
            for row in date:
                try:
                    f.append(float(row[0]))
                    g.append(float(row[1]))
                    e.append(row[2])
                except Exception as error:
                    pass

        fig, (ax1, ax2) = plt.subplots(2)
        fig.suptitle('Stacked plots')
        ax1.plot(e,g, label='Pozitia 1!')
        ax2.plot(e,f, label='Pozitia 2!')
        plt.xlabel('Timp')
        plt.ylabel('Pozitie')
        plt.title('Pozitie(Timp)')
        plt.legend()
        ax1.set_xticks([0,50,99])
        ax2.set_xticks([0,50,99])


        plt.figure(4)
        i=[]
        j=[]
        with open('viteza.csv', 'r') as csvfile:
            date = csv.reader(csvfile, delimiter=',')
            for row in date:
                try:
                    i.append(float(row[0]))
                    j.append(row[1])
                except Exception as e:
                    pass


        plt.plot(j,i, label='Viteza 1!')
        plt.xlabel('Timp')
        plt.ylabel('Viteza')
        plt.title('Viteza(Timp)')
        plt.legend()
        plt.xticks([0,50,99])

        plt.show()

def TcpTransmisson():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    host = "localhost"                     
    port = 9999                                         
    serversocket.bind((host, port))
    serversocket.listen(5)
    while True:
        clientsocket,addr = serversocket.accept()
        with open("RS232Data.csv", 'r', newline='') as csvfile:
            catalog_read = csv.reader(csvfile, delimiter=',',quotechar='|')
            clientHead = "RS232 Data \n"
            clientsocket.send(str(clientHead).encode('utf-8'))
            for row in catalog_read:
                    formatedPrint =row[0] + " la ora " + row[1] + "\n"
                    clientsocket.send(str(formatedPrint).encode('utf-8'))
        break

def RS232Conncetion():
    serialPort=serial.Serial('COM7', baudrate=115200)
    print("Connected on port: ", serialPort.name)
    return serialPort

def RS232DataLog(serialPort):
    print("Ready to recive data!")
    serialPort.write("Ready to send data!".encode())
    time.sleep(1)
    recievedData=""
    timeNow = datetime.now()
    currentTime = timeNow.strftime("%H:%M:%S")

    emptyCsvFile = csv.writer(open("RS232Data.csv", 'wb'))

    with open("RS232Data.csv", 'a', newline='') as csvfile_data:
            catalog_write_data = csv.writer(csvfile_data, delimiter=',',quotechar='|')
            catalog_write_data.writerow(["Data", "Ora"])

    while "~" not in str(recievedData):
        with open("RS232Data.csv", 'a', newline='') as csvfile_data:
            catalog_write_data = csv.writer(csvfile_data, delimiter=',',quotechar='|')
            recievedData=serialPort.read()
            catalog_write_data.writerow([recievedData.decode('utf-8'), currentTime])
            print("New data:  \t",recievedData.decode('ascii'))  

def tryAndCatchError(fileNumber):
    try:
        displayData(fileNumber)
    except Exception as  e:
        print("Warning!!! " + str(e))
        print("Make sure the Create button is pressed first to create the files")
        pass


sg.theme('Material1')
layout = [  [sg.Text('Filename')], [sg.Input(), sg.FileBrowse()],
            [sg.Text('Create csv files from the main file'), sg.Button("Create")],
            [sg.Text('Print Data: ')],
            [sg.Button('Temperature'), sg.Button('Humidity'),sg.Button('Speed'), sg.Button('Present')],
            [sg.Button('Print All Data'), sg.Button("Create Graphs"), sg.Button("Create RS232"),sg.Button("RS232 Read Sent Data")],
            [sg.Button("Send Data TCP")],
            [sg.Text('Output')],
            [sg.Output(size=(60,20))]]

window = sg.Window('Python Proiect', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Create":
        fileName = values[0]
        tempFile = os.path.isfile('./' + temperatura)
        umidFile = os.path.isfile('./' + umiditate)
        prezFile = os.path.isfile('./' + prezenta)
        vitFile = os.path.isfile('./' + viteza)
        print("Creating files", end="")
        fileCreate()
        for i in range(0,3):
            time.sleep(1)
            print(".", end="")

        if(tempFile == True and umidFile == True and prezFile == True and vitFile == True):
           print("Files: \n" + temperatura + " \n" + umiditate + "\n" + prezenta + "\n" + viteza + "\n Are created")

    elif event == "Temperatura":   
        tryAndCatchError(1)
    elif event == "Umiditate":      
       tryAndCatchError(2)
    elif event == "Viteza":      
       tryAndCatchError(3)
    elif event == "Prezenta": 
        tryAndCatchError(4)     
    elif event == "Print All Data":      
        tryAndCatchError(5)
    elif event == "Create Graphs":      
        tryAndCatchError(6)
    elif event == "Create RS232":      
        tryAndCatchError(7)
    elif event == "RS232 Read Sent Data":      
        tryAndCatchError(8)
    elif event == "Send Data TCP":      
        tryAndCatchError(9)

window.close()