import serial
import binascii
import struct
import datetime
from beep import beep
ser = serial.Serial(20, 9600, timeout=1)

def dec2hex(n):
    """return the hexadecimal string representation of integer n"""
    return "%X" % n
def hex2dec(s):
    """return the integer value of a hexadecimal string s"""
    return int(s, 16)


def timeutcf(barray,edge):
        count =  struct.unpack('<H', barray[4:6])[0]
        wnR =  struct.unpack('<H', barray[6:8])[0]
        wnF =  struct.unpack('<H', barray[8:10])[0]
        towMsR =  struct.unpack('<I', barray[10:14])[0]
        towSubMsR =  struct.unpack('<I', barray[14:18])[0]
        towMsF =  struct.unpack('<I', barray[18:22])[0]
        towSubMsF =  struct.unpack('<I', barray[22:26])[0]
        accEst =  struct.unpack('<I', barray[26:30])[0]

        secondSinceGES_F = wnF*7*24*3600 + towMsF/1000. + towSubMsF/1000000000.
        timeutcF = str(gpsEpochStart + datetime.timedelta(0,secondSinceGES_F))
        secondSinceGES_R = wnR*7*24*3600 + towMsR/1000. + towSubMsR/1000000000.
        timeutcR = str(gpsEpochStart + datetime.timedelta(0,secondSinceGES_R))
        if edge == 'falling':
            return timeutcF
        if edge == 'rising':
            return timeutcR

gpsEpochStart = datetime.datetime(1980,1,6,0,0,0)
while 1:
    if binascii.hexlify(ser.read(1)) == 'b5':
        if binascii.hexlify(ser.read(1)) == '62':
            if binascii.hexlify(ser.read(1)) == '0d':
                if binascii.hexlify(ser.read(1)) == '03':
                    print timeutcf(ser.read(30),'rising')
                    beep()

ser.close()
