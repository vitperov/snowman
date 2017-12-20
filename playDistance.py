#!/usr/bin/env python
import os, random
import serial

prev = 0;

def getDistance(ser):
    global prev
    line = ser.readline()
    #print "str=" + line 
    try:
	val = int(line)
	#print "int=" + str(val)
	if val > 1800:
	    return 0

        dx = val - prev
	prev = val
	#print "DX=" + str(dx)
	return dx
    except:
	pass

    return 0


def rndmp3 ():
    randomfile = random.choice(os.listdir("wav"))
    print "Playing file " + str(randomfile)
    file = 'wav/'+ randomfile
    os.system ('mpg321 ' + file)

ser = serial.Serial('/dev/ttyACM0')
#rndmp3 ()
filtered = 0
while 1==1:
    dx = getDistance(ser)

    filtered = filtered * 0.8 + dx * 0.2
    print "dx=" + str(filtered)

    if filtered > 20:
	rndmp3()


