#!/usr/bin/env python
import os, random
import serial

filtered = 1800;

def getDistance(ser):
    global prev
    line = ser.readline()
    #print "str=" + line 
    try:
	val = int(line)
	#print "int=" + str(val)
	return val
	if val > 1800:
	    val = 1800

        filtered  = filtered * 0.9 + val *0.1
	#prev = val
	#print "DX=" + str(dx)
	return filtered
    except:
	pass

    return 1800


def rndmp3 ():
    randomfile = random.choice(os.listdir("wav"))
    print "Playing file " + str(randomfile)
    file = 'wav/'+ randomfile
    os.system ('mpg321 ' + file)

ser = serial.Serial('/dev/ttyACM0')
#rndmp3 ()
#filtered = 0
while 1==1:
    dx = getDistance(ser)

    #filtered = filtered * 0.9 + abs(dx) * 0.1
    print "dx=" + str(dx)

    if dx <  800:
	rndmp3()
	filtered = 1800


