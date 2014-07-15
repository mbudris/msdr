#uBlox flight mode code

import serial
import time
import sys

gps_set_success = False

#ser = serial.Serial("/dev/ttyACM0", 9600) #ACM gps AMA gpio
ser = serial.Serial(20, 9600)

setTM2 = bytearray.fromhex("B5 62 06 19 0C 00 00 00 00 00 E8 03 00 00 25 01 00 00 3C 6B")
setTM2_2 = bytearray.fromhex("B5 62 06 19 01 00 00 20 85")
setTmMagRate = bytearray.fromhex("B5 62 06 01 03 00 0D 03 01 1B 6D")

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
time.sleep(1)
sendUBX(setTM2_2)
time.sleep(1)
sendUBX(setTmMagRate)


##
##while not gps_set_success:
##        sendUBX(setNav, len(setTM2))
##        gps_set_success = getUBX_ACK(setNav);
##
##while 1:
##        break
