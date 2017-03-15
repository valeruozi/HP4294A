
import visa
import sys
import time

class HP4294a:
    def __init___(self,addr,serialcom)
        self.addr = addr
        #rm = resoucemanager()
        Myinstr= rm.get_instrument(self.addr)
        '''Timeout set at 5 sec'''
        self.timeout = 5000 #it has to be longer than any operation
        '''Get and display the device IDN'''
        myinst.write("*IDN?")
        print myinst.read()
        '''Clear status and load the default setup'''
        myinst.write("*CLS")
        myinst.write("*RST")
        '''Set the ASCII format as the data transfer format'''
        Myinstr.write("FORM4") 

    def check_errors(self)
        myinstr.query("OUTPERRO?")
        #print ("Errors: ", myinstr.read()) NO PERCHE E UNA QUERY
        pass
    def trigger(self)
        myinstr.write("TRGS INT")
        pass
    def calibration(self,cal)
        if cal = "OPEN"
            myinst.write("CALA")
        if cal = "SHORT"
            myinst.write("CALB")
        if cal = "LOAD"
            myinst.write("CALC")

class Sweep: 
    def __init__(self,a,b,npoints,delay)
    self.start = a
    self.stop = b 
    self.center = a
    self.span = b
    self.npoints = npoints
    self.delay = delay
    
    SWPP {FREQ|OLEV|DCB}
    SWPT {LIN|LOG|LIST}


    
    def span(self)
    
    def start_stop(self)

class Measure:
    def __init__(self,freq)
        myinst.write("MEAS IMPH")
        [a,b] = myinst.read()
    def get_amplitude(self)
        self.amplitude = a
        return self.amplitude
    def get_phase(self)
        self.phase = b
        return self.phase
