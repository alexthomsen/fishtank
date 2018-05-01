import string, sys
import sys
import time as t
from datetime import datetime,time,timedelta
from threading import Thread

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

class Light():
    STATE=0
    LastON=datetime.now()

class Filter():
    STATE=0
    LastON=datetime.now()

class Heater():
    STATE=0
    LastON=datetime.now()

class LeftSmallPump():
    STATE=0
    LastON=datetime.now()

class RightSmallPump():
    STATE=0
    LastON=datetime.now()

class RightBigPump():
    STATE=0
    LastON=datetime.now()

global currentState
currentState=State.UNDEFINED


class controller(Thread):

    global currentState

    def __init__(self):
        Thread.__init__(self)


    def initialize(self):
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
   
    def LightState(self,State):
        if (State != Light.STATE):
            Light.STATE = State

            if (State == False):
                print "Light changed to OFF"
            else:
                print "Light changed to ON"



    def LeftSmallPumpState(self,State):
        if (State != LeftSmallPump.STATE):
            LeftSmallPump.STATE = State

            if (State == False):
                print "Left Small Pump state changed to OFF"
                LeftSmallPump.LastON = datetime.now()
            else:
                print "Left Small Pump state changed to ON"
                LeftSmallPump.STATE = True

    def RightSmallPumpState(self,State):
        if (State != RightSmallPump.STATE):
            RightSmallPump.STATE = State

            if (State == False):
                print "Right Small Pump state changed to OFF"
                RightSmallPump.LastON = datetime.now()
            else:
                print "Right Small Pump state changed to ON"
                RightSmallPump.STATE = True

    def RightBigPumpState(self,State):
        if (State != RightBigPump.STATE):
            RightBigPump.STATE = State

            if (State == False):
                print "Right Big Pump state changed to OFF"
                RightBigPump.LastON = datetime.now()
            else:
                print "Right Big Pump state changed to ON"
                RightBigPump.STATE = True

    def CleanUP(self):
        print "Change ALL states to defaults"


    def run(self):
        lastState=0
        while True:
            if (currentState == State.INITIALIZE):
                print "Changing state to " + State.codes[currentState]
            elif (currentState == State.SLEEPING):
                print "Changing state to " + State.codes[currentState]
                while currentState == lastState or lastState == State.UNDEFINED:
                    self.LightState(False)
                    
                    if (LeftSmallPump.STATE == False and (LeftSmallPump.LastON + timedelta(minutes=15) < datetime.now())):
                        self.LeftSmallPumpState(True)
                    else:
                        self.LeftSmallPumpState(False)

                    if (RightSmallPump.STATE == False and (RightSmallPump.LastON + timedelta(minutes=15) < datetime.now()) and LeftSmallPump.STATE != True):
                        self.RightSmallPumpState(True)
                    else:
                        self.RightSmallPumpState(False)

                    t.sleep(10)
                self.CleanUP();
            elif (currentState == State.NORMAL):
                print "Changing state to " + State.codes[currentState]
                while currentState == lastState or lastState == State.UNDEFINED:
                    self.LightState(True)
                    if(RightBigPump.STATE == false):
                        self.LeftSmallPumpState(True)
                        self.RightSmallPumpState(True)

                    if(RightBigPump.STATE == False and RightBigPump.LastON + timedelta(hours=3 < datetime.now() and RightBigPump.LastON + timedelta(hours=3,minutes=1) > datetime.now())):
                        self.RightBigPumpState(True)
                    else:
                        self.RightBigPumpState(False)

                    t.sleep(10)
                seld.CleanUP();
            elif (currentState == State.HIGHBURST):
                while currentState == lastState:
                    print "IN " + State.codes[currentState]
                    t.sleep(10)
            elif (currentState == State.FEEDING):
                while currentState == lastState:
                    print "IN " + State.codes[currentState]
                    t.sleep(10)
            elif (currentState == State.MAINTENANCE):
                while currentState == lastState:
                    print "IN " + State.codes[currentState]
                    t.sleep(10)

            lastState=currentState
            t.sleep(1)

if __name__ == '__main__':
    worker = controller()
    worker.start()
#    worker.join()
    
    while True:
        if ( currentState == State.UNDEFINED ):
            print "Starting program"
            #initialize();

        now = datetime.now()
        now_time = now.time()

        if (time(00,00) <= now_time <= time(17,29)):
            if (currentState != State.SLEEPING):
                currentState = State.SLEEPING
        if (time(17,30) <= now_time <= time(17,59)):
            if (currentState != State.NORMAL):
                currentState = State.NORMAL
        elif (time(18,00) <= now_time <= time(18,14)):
            if (currentState != State.FEEDING):
                currentState = State.FEEDING
        elif (time(18,15) <= now_time <= time(22,59)):
            if (currentState != State.NORMAL):
                currentState = State.NORMAL
        elif (time(23,00) <= now_time <= time(23,59)):
            if (currentState != State.SLEEPING):
                currentState = State.SLEEPING
        t.sleep(1)
