#!/usr/bin/python
import sys
from random import random
from subprocess import call

if (len(sys.argv) != 3):
    print """
Two arguments needed: mean and totalDuration.
Example usage: ./woodenfish.py 5 60
The above will generate a sequence of strike interarrival times 
5 sec apart on average, until approximately 60 sec have passed.
"""
    sys.exit()

def irwinHall(largest):
  rands = [random() for n in range(12)]
  sample = sum(rands) - 6
  return sample * (largest / 6.0)

mean = int(sys.argv[1])
totalDuration = int(sys.argv[2])
strikeTargets = range(0,totalDuration,mean)
strikeTimes = [mean + irwinHall(mean) for t in strikeTargets]

interarrivals = ["%.2f" % t for t in strikeTimes]
print repr(interarrivals) 

myCall = "sox -V1 onestrike.wav silence60s.wav out.wav crop 0 5".split()
for (n, ia) in enumerate(interarrivals):
  myCall[7] = ia
  myCall[4] = "out" + str(n) + ".wav"
  call(myCall)

intermediates = ["out" + str(n) + ".wav" for n in range(len(interarrivals))] 
outfilename = "woodenfish_" + str(mean) + "_" + str(totalDuration) + ".wav"
lastCall = ["sox"] + intermediates + ["twostrikes.wav"]+ [outfilename]
call(lastCall)
call(["rm"] + intermediates)

# convert to m4a for iPod
convertCall = "ffmpeg -v quiet -i woodenfish_m_tD.wav -acodec aac -strict experimental out.m4a".split()
convertCall[4] = outfilename
convertCall[9] = outfilename[:-3] + "m4a"
call(convertCall)
call(["rm"] + [outfilename])

