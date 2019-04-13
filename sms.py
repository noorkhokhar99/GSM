
import serial   

import os, time


# Enable Serial Communication
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)


# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key
port.write('AT'+'\r\n')
rcv = port.read(10)
print rcv


port.write('AT+CMGF=1'+'\r\n')
rcv = port.read(10)
print rcv

port.write('AT+CNMI=2,1,0,0,0'+'\r\n')
rcv = port.read(10)
print rcv
time.sleep(1)

port.write('AT+CMGS=""'+'\r\n')
rcv = port.read(10)
print rcv
time.sleep(1)

port.write('HELLO User'+'\r\n')
rcv = port.read(10)
print rcv
#time.sleep(1)

port.write("\x1A")
for i in range(10):
    rcv = port.read(10)
    print rcv
#time.sleep(1)






