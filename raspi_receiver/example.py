#!/usr/bin/env python2

import RFM69
from RFM69registers import *
import datetime
import time
import struct

try:
    test = RFM69.RFM69(RF69_433MHZ, 1, 100, False)
    #print "class initialized"
    #print "reading all registers"
    #results = test.readAllRegs()
    #for result in results:
    #    print result
    #print "Performing rcCalibration"
    #test.rcCalibration()
    #print "setting high power"
    #test.setHighPower(True)   #Raspberry pi 3.3V pin cannot supply enough power for this...it's ok as long as you just receive
    #print "Checking temperature"
    #print test.readTemperature(0)
    #print "setting encryption"
    #test.encrypt("sampleEncryptKey")
    #print "sending blah to 2"
    #if test.sendWithRetry(2, "blah", 3, 20):
    #    print "ack recieved"
    #print "reading"
    while True:
        test.receiveBegin()
        while not test.receiveDone():
            time.sleep(.1)
        #print(len(test.DATA)) #print payload size
        #print(test.DATA)
        data = test.DATA[:2]+[0x00, 0x00]+test.DATA[2:] #have to do like this...why?
        #data=test.DATA
        id, uptime, temperature, humidity = struct.unpack("hLhh", "".join([chr(x) for x in data]))
        
        #print "id={} uptime={} temperature={} humidity={} from {} RSSI: {}".format(
         #   id, uptime, temperature, humidity, test.SENDERID, test.RSSI) #Now temperature and humidity must be divided by 10 
        print "{},{},{},{},{},{}".format(
            id, uptime, temperature, humidity, test.SENDERID, test.RSSI)#Now temperature and humidity must be divided by 10 
        
        if test.ACKRequested():
            test.sendACK()
#execute this code if CTRL + C is used to kill python script
except KeyboardInterrupt:
  print "You've exited the program"

finally:
    test.shutdown()
    #print "shutting down"
    
