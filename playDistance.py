#!/usr/bin/env python
import os, random
import serial

filtered = 2000.0;
buf = ""

def getDistance(ser):
    global filtered
    global buf
    #print "waiting line..."
    buf = buf + ser.read(5)
    arr = buf.split('\n')
    if len(arr) < 2:
	return 2000

    line = arr[0]
    buf = arr[1]
    #print arr
    #line = ser.readline()
    #line = line.rstrip()
    #print "str=" + line 
    try:
	val = float(line)
	print "int=" + str(val)

	if val > 2000:
	    val = 2000.0

	#print "1"

	if val < 100:
	    val = 2000.0

	#print "2"

        filtered  = filtered * 0.7 + val *0.3

	#print "3"
	#prev = val
	print str(val) + "->" +str(filtered)
	return filtered
    except:
	pass

    return 2000


def rndmp3 ():
    randomfile = random.choice(os.listdir("wav"))
    print "Playing file " + str(randomfile)
    file = 'wav/'+ randomfile
    os.system ('mpg321 ' + file)

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1000)
#rndmp3 ()
#filtered = 0
while 1==1:
    dx = getDistance(ser)

    #filtered = filtered * 0.8 + abs(dx) * 0.2
    #print "dx=" + str(dx)

    if dx < 1000:
	rndmp3()
	#ser.reset_input_buffer()
	ser.flushInput()
	filtered = 2000


