import winsound
from time import sleep

def beep():
    for x in range(0, 3):
        Freq = 2500 # Set Frequency To 2500 Hertz
        Dur = 500 # Set Duration To 1000 ms == 1 second
        winsound.Beep(Freq,Dur)
        sleep(0.005)
beep()
