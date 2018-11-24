#!/usr/bin/env python2

import RFM69
from RFM69registers import *
import datetime
import time
import struct
#WS part
import asyncio
import websockets

test = RFM69.RFM69(RF69_433MHZ, 1, 100, False)
print "class initialized"
print "reading all registers"
results = test.readAllRegs()
for result in results:
    print result
print "Performing rcCalibration"
test.rcCalibration()
#print "setting high power"
#test.setHighPower(True)   #Raspberry pi 3.3V pin cannot supply enough power for this...it's ok as long as you just receive
print "Checking temperature"
print test.readTemperature(0)
#print "setting encryption"
#test.encrypt("sampleEncryptKey")
print "sending blah to 2"
if test.sendWithRetry(2, "blah", 3, 20):
    print "ack recieved"
print "reading"

async def hello(mylist):
    async with websockets.connect('ws:10.226.35.12:1880/rfm69') as websocket:
        await websocket.send(mylist)

while True:
    test.receiveBegin()
    while not test.receiveDone():
        time.sleep(.1)
    print(len(test.DATA)) #print payload size
    #print(test.DATA)
    data = test.DATA[:2]+[0x00, 0x00]+test.DATA[2:] #have to do like this...why?
    #data=test.DATA
    id, uptime, temperature, humidity = struct.unpack("hLhh", "".join([chr(x) for x in data]))
    
    print "id={} uptime={} temperature={} humidity={} from {} RSSI: {}".format(
        id, uptime, temperature, humidity, test.SENDERID, test.RSSI) #Now temperature and humidity must be divided by 10 
    if test.ACKRequested():
        test.sendACK()
    
    asyncio.get_event_loop().run_until_complete(hello(temperature))
    
print "shutting down"
test.shutdown()
