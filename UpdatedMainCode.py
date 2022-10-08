# Import all the libraries we need to run
import sys
import RPi.GPIO as GPIO
import os
from time import sleep
import Adafruit_DHT
import urllib2


# Setup the pins we are connect to
DHTpin = 23

#Setup our API and delay
myAPI = "PR998OE86JF4S5JH"
myDelay = 15 #how many seconds between posting data

def getSensorData():
    RHW, TW = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHTpin)
    
    #Convert from Celius to Farenheit
    TWF = 9/5*TW+32
   
    # return dict
    return (str(RHW), str(TW),str(TWF))

    
# main() function
def main():
    
    print 'starting...'

    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
    print baseURL

    while True:
        try:
            RHW, TW, TWF = getSensorData()
            f = urllib2.urlopen(baseURL + "&field1=%s&field2=%s&field3=%s" % (TW, TWF, RHW))
            print f.read()
            print TW + " " + TWF+ " " + RHW
            f.close()
            sleep(int(myDelay))
        except:
            print 'exiting.'
            break

# call main"""
if _name_ == '_main_':
main()
