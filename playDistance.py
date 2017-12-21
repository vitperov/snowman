#!/usr/bin/env python
import os, random
import serial

filtered = 1800;

def getDistance(ser):
    global filtered
    line = ser.readline().rstrip()
    #print "str=" + line 
    try:
	val = int(line)
	#print "int=" + str(val)

	if val > 1800:
	    val = 1800

	if val < 100:
	    val = 1800

        filtered  = filtered * 0.8 + val *0.2
	#prev = val
	print line + "->" +str(int(filtered))
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

    #filtered = filtered * 0.8 + abs(dx) * 0.2
    #print "dx=" + str(dx)

    if dx < 1100:
	rndmp3()
	#ser.reset_input_buffer()
	ser.flushInput()
	filtered = 1800


