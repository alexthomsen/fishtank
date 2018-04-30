import string, sys

import sys
import time as t
from datetime import datetime,time

class State():
    INITIALIZE = 1
    SLEEPING = 2
    NORMAL = 3
    HIGHBURST = 4
    FEEDING = 5
    MAINTENANCE = 6
    UNDEFINED = 7

    codes = {INITIALIZE:'INITIALIZE',
             SLEEPING:'SLEEPING',
             NORMAL:'NORMAL',
             HIGHBURST:'HIGHBURST',
             FEEDING:'FEEDING',
             MAINTENANCE: 'MAINTENANCE',
             UNDEFINED:'UNDEFINED'}

global currentState
currentState=State.UNDEFINED

def initialize():
    global currentState;
    currentState = State.INITIALIZE;
    print "State changed to Initializing"
    print "* Setting up GPIO"
    print "* Setting up Temperature monitor"
    print "Initializing completed"

def sleeping():
    global currentState;
    currentState = State.SLEEPING;
    print "State changed to Sleeping"
    print "* Light OFF"
    print "* Filer ON"
    print "* Heater ON"
    print "* Left Small Pump ON"
    print "* Right Small Pump OFF"
    print "* Right Big Pump ON for 3 Minutes"
    print "* Diode OFF"

def normal():
    global currentState;
    currentState = State.NORMAL;
    print "State changed to Normal"
    print "* Light ON"
    print "* Filer ON"
    print "* Heater ON"
    print "* Left Small Pump Cycle 5 Min"
    print "* Right Small Pump Opposite Cycle 5 Min"
    print "* Right Big Pump ON for 3 Minutes every 3 hours"
    print "* Diode OFF"

def highBurst():
    global currentState;
    currentState = State.HIGHBURST;
    print "State changed to High Burst"
    print "* Light ON"
    print "* Filer ON"
    print "* Heater ON"
    print "* Left Small Pump Cycle 5 Min"
    print "* Right Small Pump Cycle 5 Min"
    print "* Right Big Pump Cycle 5 Min"
    print "* Diode OFF"

def feeding():
    global currentState;
    currentState = State.FEEDING;
    print "State changed to Feeding"
    print "* Light ON"
    print "* Filer OFF"
    print "* Heater ON"
    print "* Left Small Pump OFF"
    print "* Right Small Pump OFF"
    print "* Right Big Pump OFF"
    print "* Diode OFF"

def maintenance():
    global currentState;
    currentState = State.MAINTENANCE;
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
            initialize();

        now = datetime.now()
        now_time = now.time()

        if (time(00,00) <= now_time <= time(17,29)):
            if (currentState != State.SLEEPING):
                sleeping();
        if (time(17,30) <= now_time <= time(17,59)):
            if (currentState != State.NORMAL):
                normal();
        elif (time(18,00) <= now_time <= time(18,14)):
            if (currentState != State.FEEDING):
                feeding();
        elif (time(18,15) <= now_time <= time(22,59)):
            if (currentState != State.NORMAL):
                normal();
        elif (time(23,00) <= now_time <= time(23,59)):
            if (currentState != State.SLEEPING):
                sleeping();
        t.sleep(1)
