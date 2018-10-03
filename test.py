"""
Active serial porl List

import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())
for p in ports:
   print (p)

"""

import serial
import time

s_p = serial.Serial('/dev/tty.usbmodem1421', baudrate=1000000, timeout=0.05)

sid = 14

inst = bytearray([0x03,0x1E,0x00,0x08,0x2C,0x01])
length = len(inst) + 1

csum = 0
for _ in inst:
    csum += _
csum += (sid + length)
#print(csum)
#csum = 255 - csum

#packet = bytearray([0xFF,0xFF,sid,length]) + inst + bytearray([csum])

t = 0.7

time.sleep(15*t)
#print(packet)
#s_p.write(packet)
  
for j in range (10):
    
    inst = bytearray([0x03,0x1E,0xC4,0x09,0x61,0x00])
    csum = 0
    for _ in inst:
        csum += _
    csum += (sid + length)
    print (csum)
    csum = 255 - (csum - 256)
    
    
    packet = bytearray([0xFF,0xFF,sid,length]) + inst + bytearray([csum])
    
    s_p.write(packet)
    
    response = s_p.read(6)
    print(response)
    
    time.sleep(t)
    
    inst = bytearray([0x03,0x1E,0x00,0x08,0x61,0x00])
    csum = 0
    for _ in inst:
        csum += _
    csum += (sid + length)
 
    csum = 255 - csum
    packet = bytearray([0xFF,0xFF,sid,length]) + inst + bytearray([csum])

    s_p.write(packet)
    
    response = s_p.read(6)
    print(response)
    time.sleep(t)