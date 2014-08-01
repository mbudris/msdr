#!/usr/bin/python

import serial
import time
import sys

gps_set_success = False

#ser = serial.Serial("/dev/ttyAMA0", 9600) #ACM gps AMA gpio
ser = serial.Serial(20, 9600)

#rising edge
setTM2 = bytearray.fromhex("B5 62 06 19 0C 00 00 00 00 00 E8 03 00 00 15 01 00 00 2C 2B")
setTM2_2 = bytearray.fromhex("B5 62 06 19 01 00 00 20 85")
#falling edge
#setTM2 = bytearray.fromhex("B5 62 06 19 0C 00 00 00 00 00 E8 03 00 00 25 01 00 00 3C 6B")
#setTM2_2 = bytearray.fromhex("B5 62 06 19 01 00 00 20 85")
setTmMagRate = bytearray.fromhex("B5 62 06 01 03 00 0D 03 01 1B 6D")

#57600
setBaudrate = bytearray.fromhex("B5 62 06 00 14 00 01 00 00 00 D0 08 00 00 00 E1 00 00 07 00 07 00 00 00 00 00 E2 E1")

#config for raw data
line01 = bytearray.fromhex("B5 62 06 01 03 00 02 30 01 3D A6")
line02 = bytearray.fromhex("B5 62 06 01 03 00 02 31 01 3E A8")
line03 = bytearray.fromhex("B5 62 06 01 03 00 02 10 01 1D 66")
line04 = bytearray.fromhex("B5 62 06 01 03 00 02 11 01 1E 68")
line05 = bytearray.fromhex("B5 62 06 01 03 00 02 13 01 20 6C")
line06 = bytearray.fromhex("B5 62 06 01 03 00 02 20 01 2D 86")


def sendUBX(MSG):
        print "Sending UBX Command: "
        ubxcmds = ""
        for i in range(0, len(MSG)):
                ser.write(chr(MSG[i])) #write each byte of ubx cmd to serial port
                ubxcmds = ubxcmds + str(MSG[i]) + " " # build up sent message debug output string
        ser.write("\r\n") #send newline to ublox
        print ubxcmds #print debug message
        print "UBX Command Sent..."




#actual program code below:
print "Setting uBlox nav mode: "
sendUBX(setTM2)
time.sleep(.2)
sendUBX(setTM2_2)
time.sleep(.2)
sendUBX(setTmMagRate)
time.sleep(.2)
sendUBX(line01)
time.sleep(.2)
sendUBX(line02)
time.sleep(.2)
sendUBX(line03)
time.sleep(.2)
sendUBX(line04)
time.sleep(.2)
sendUBX(line05)
time.sleep(.2)
sendUBX(line06)
time.sleep(.2)
sendUBX(setBaudrate)


##
##while not gps_set_success:
##        sendUBX(setNav, len(setTM2))
##        gps_set_success = getUBX_ACK(setNav);
##
##while 1:
##        break
