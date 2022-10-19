# Import all the libraries needed
import sys
import RPi.GPIO as GPIO
import os
from time import sleep
from gpiozero import LED
import Adafruit_DHT
import urllib2


# Setup pins to be connected
DHTsensor = 23
ledtemp= LED(17)
ledhum= LED(18)

#Setup API key and delay
APIkey = "PR998OE86JF4S5JH"
Delay = 600 #how many seconds between posting data

def getSensorData():
    RHW, TW = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHTsensor)
    # return a dictionary containing temperature and humidity values
    return (str(RHW), str(TW))

def LEDlightup():
	RHW, TW= getSensorData()
    #check temperature value and control led
	if TW >= 36:
		ledtemp.on()
	else: 
		ledtemp.off()

    #check humidity value and control led
	if RHW >= 60:
		ledhum.on()
	else:
		ledhum.off()
	return

# main() function
def main():
    
    print('starting...')

    apiURL = 'https://api.thingspeak.com/update?api_key=%s' % APIkey
    print(apiURL)
    
    while True:
        try:
            RHW, TW = getSensorData()
            wlink = urllib2.urlopen(apiURL + "&field1=%s&field2=%s&field3=%s" % (TW, RHW))
            print (f.read())
            print( TW + " " + " " + RHW)
            LEDlightup()
            wlink.close()
            sleep(int(Delay))
        except:
            print('exiting.')
            break

if _name_ == '_main_':
    main()
