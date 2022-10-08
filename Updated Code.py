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
