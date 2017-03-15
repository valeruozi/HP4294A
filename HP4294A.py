
import visa
import sys
import time


class HP4294A:
    def __init__(self,myinst):
        self.myinst = myinst
        
    def inizialize(self):
        '''Timeout set at 5 sec'''
        self.myinst.timeout = 5000 #it has to be longer than any operation
        self.myinst.read_termination = '^END'
        self.myinst.write_termination = '^END'
        '''Get and display the device IDN'''
        print myinst.query("*IDN?") 
        '''Clear status and load the default setup'''
        self.myinst.write("*CLS")
        self.myinst.write("*RST")
        '''Set the ASCII format as the data transfer format'''
        self.myinst.write("FORM4") 

    def check_errors(self):
        '''Reads out the oldest error among errors stored in the error queue of the 4294A. The size of the error queue is 10'''
        print self.myinst.query("OUTPERRO?")
    
    def trigger(self,trig,number):
        if trig == 'internal':
            self.myinst.write("TRGS INT")
        elif trig == 'external':
            self.myinst.write("TRGS EXT")
        elif trig == 'bus':
            self.myinst.write("TRGS BUS")
            
        if number == 'single':
            self.myinst.write("SING")
        elif number == 'continuous':
            self.myinst.write("CONT")
            
        '''If the trigger is set to BUS it needs the execution command'''
        if trig == 'bus':
            self.myinst.write("*TRG")
        pass
    
    def hold(self):
        self.myinst.write("HOLD")
        pass
    
    def calibration(self,cal):
        if cal == "open":
            self.myinst.write("CALA")
        if cal == "short":
            self.myinst.write("CALB")
        if cal == "load":
            self.myinst.write("CALC")
        pass
            
    def get_measure(self,sweep,sweep_type,number_type):
        self.sweep = sweep
        self.sweep_type = sweep_type
        self.number_type = number_type
        
        if self.number_type == 'absolute':
            self.myinst.write("MEAS IMPH")
        elif self.number_type == 'complex':
            self.myinst.write("MEAS COMP")
        
        self.sweep1 = Sweep(self.sweep)
        
        '''Specifies the frequency sweep'''
        self.myinst.write("SWPP FREQ")
        
        self.myinst.write("POIN" + str(self.sweep1.npoints))
        
        '''Sets the graphs type'''
        if self.sweep1.type == "linear":
            self.myinst.write("SWPT LIN")
        elif self.sweep1.type == "log":
            self.myinst.write("SWPT LOG")
            
        '''Sets the sweep type'''
        if self.sweep1.sweep_type == 'span'
            self.myinst.write("CENT" + str(self.center))
            self.myinst.write("SPAN" + str(self.span))
        elif self.sweep1.sweep_type == 'start_stop'
            self.myinst.write("STAR" + str(self.start))
            self.myinst.write("STOP" + str(self.stop))
        
        ''' Copies the measured data into the memory array. It is copied to both the A And B traces'''
        self.myinst.write("DATAMEM")
        
        '''Reads out the values(complex number) of all measurement points in the memory array'''
        print self.myinst.query("OUTPMEMO?")
        
    def save_data(self):
        '''Enables/disables the save of the data trace array'''
        self.myinst.write("SAVDTRC ON")
        self.myinst.write("SAVDTRC ON") '''DATA TRACE'''
        self.myinst.write("SAVMTRC ON") '''MEMORY TRACE'''
        self.myinst.write("SAVDAT ON") '''DATA'''
        self.myinst.write("SAVMEM ON") '''MEMORY'''
        self.myinst.write("SAVDASC",".TXT")
        pass
        
class Measure: 
    def __init__(self,A,B):
        self.a = A
        self.b = B

class Sweep: 
    def __init__(self,a,b,npoints,delay,stype): #Unit Hz
        self.start = a
        self.stop = b 
        self.center = a
        self.span = b
        self.npoints = npoints
        self.delay = delay
        '''Sets the sweep type'''
        self.type = stype 

    
rm = visa.ResourceManager()
rm.list_resources()
gpib_adress = raw_input("Type the choosen resource name: ") #"GPIB:19::INSTR"
myinst = rm.get_instrument(gpib_adress)  #addr of the instrument, found on visa's resources
impAnalyzer = HP4294A(myinst)

sweep1 = Sweep(10,1000,100,100,'linear')
measure1 = impAnalyzer.get_measure(sweep1,'start_stop','absolute')
