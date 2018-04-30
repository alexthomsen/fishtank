import string, sys

import sys
import time as t
from datetime import datetime,time

class State():
    INITIALISING = 1
    SLEEPING = 2
    NORMAL = 3
    HIGHBURST = 4
    FEEDING = 5
    MAINTENANCE = 6
    UNDEFINED = 7

    codes = {INITIALISING:'INITIALISING',
             SLEEPING:'SLEEPING',
             NORMAL:'NORMAL',
             HIGHBURST:'HIGHBURST',
             FEEDING:'FEEDING',
             MAINTENANCE: 'MAINTENANCE',
             UNDEFINED:'UNDEFINED'}

currentState=State.UNDEFINED

def initialize():
    print "State changed to Initializing"
    print "* Setting up GPIO"
    print "* Setting up Temperature monitor"
    print "Initializing completed"

def sleeping():
    print "State changed to Sleeping"
    print "* Light OFF"
    print "* Filer ON"
    print "* Heater ON"
    print "* Left Small Pump ON"
    print "* Right Small Pump OFF"
    print "* Right Big Pump ON for 3 Minutes"
    print "* Diode OFF"

def normal():
    print "State changed to Normal"
    print "* Light ON"
    print "* Filer ON"
    print "* Heater ON"
    print "* Left Small Pump Cycle 5 Min"
    print "* Right Small Pump Opposite Cycle 5 Min"
    print "* Right Big Pump ON for 3 Minutes every 3 hours"
    print "* Diode OFF"

def highBurst():
    print "State changed to High Burst"
    print "* Light ON"
    print "* Filer ON"
    print "* Heater ON"
    print "* Left Small Pump Cycle 5 Min"
    print "* Right Small Pump Cycle 5 Min"
    print "* Right Big Pump Cycle 5 Min"
    print "* Diode OFF"

def feeding():
    print "State changed to Feeding"
    print "* Light ON"
    print "* Filer OFF"
    print "* Heater ON"
    print "* Left Small Pump OFF"
    print "* Right Small Pump OFF"
    print "* Right Big Pump OFF"
    print "* Diode OFF"

def maintenance():
    print "State changed to Maintenance"
    print "* Light ON"
    print "* Filer OFF"
    print "* Heater OFF"
    print "* Left Small Pump OFF"
    print "* Right Small Pump OFF"
    print "* Right Big Pump OFF"
    print "* Diode ON"

if __name__ == '__main__':
    while True:
        if ( currentState == State.UNDEFINED ):
            print "Starting program "
            currentState = initialize();
        
        now = datetime.now()
        now_time = now.time()
        if (time(10,30) <= now_time <= time(14,59)):
            print "Under 14:59"
        elif (time(15,00) <= now_time <= time(15,14)):
            print "Over 15 og under 15:15"
        elif (time(15,15) <= now_time <= time(20,00)):
            print "Over 15:15 og under 20.00"

        t.sleep(1)
