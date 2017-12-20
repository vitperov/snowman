#!/usr/bin/env python
import os, random

def rndmp3 ():
    randomfile = random.choice(os.listdir("wav"))
    print "Playing file " + str(randomfile)
    file = 'wav/'+ randomfile
    os.system ('mpg321 ' + file)

rndmp3 ()
