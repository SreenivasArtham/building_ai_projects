import math
import sys
import time
import os
import datetime
import random

print('Square Root :',math.sqrt(16))
print('sys version ',sys.version)
print('sys argv ',sys.argv)
print('Current time in seconds : ',time.time())
start = time.time();
time.sleep(3)
print('Excution Time: ',start-time.time())

print('current workign directory : ',os.getcwd())
print('List of Directories : ',os.listdir('.'))

print('curretnt date and time ',datetime.datetime.now())

print('random integeras in 1 to 10 : ',random.randint(1,10))