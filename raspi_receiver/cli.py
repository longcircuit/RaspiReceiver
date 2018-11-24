from rfm69py.RFM69 import RFM69
from rfm69py import RFM69registers
import datetime
import time
import struct



def loop():
    radio = RFM69(RF69_433MHZ, 1, 100, False)
    try:
        while True:
            radio.receiveBegin()
            while not radio.receiveDone():
                time.sleep(.1)

            if radio.ACKRequested():
                radio.sendACK()
    finally:
        radio.shutdown()


def main():
    print("RaspiReceiver started")

    try:
        loop()
    except KeyboardInterrupt:
      print("You've exited the program")

