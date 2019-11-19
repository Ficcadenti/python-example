import time, math, random
import zhinst.ziPython, zhinst.utils
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from numpy import *
plt.ion()

class Oscilloscope(object):
    def __init__(self,device,daq,channel):
        self.device=device
        self.daq=daq
        self.channel=channel
        self.updated=0
        
    def set_parameters(self, bwlimit=0,trigedge=1,triglevel=0, trigholdoff=0.01,trigchannel=-2,t=1):
        settings = [
            [['/', self.device, '/scopes/0/channel'], self.channel-1],
            [['/', self.device, '/scopes/0/bwlimit'], bwlimit],
            [['/', self.device, '/scopes/0/trigedge'], trigedge],
            [['/', self.device, '/scopes/0/triglevel'], triglevel],
            [['/', self.device, '/scopes/0/trigholdoff'], trigholdoff],
            [['/', self.device, '/scopes/0/trigchannel'], trigchannel],
            [['/', self.device, '/scopes/0/time'], t]
        ]
        self.daq.set(settings)
        # wait 1s
        time.sleep(1)
        #clean queue
        self.daq.flush()
  
    def update(self):
            rng=self.daq.getDouble('/' + self.device + '/sigins/'+ str(self.channel-1) + '/range')
            #poll data 0.05s
            dataDict = self.daq.poll(0.05,500)
            #for first oscilloscope shot use plot function and after is
            #used draw function to update figure with new oscilloscope data
            if self.device in dataDict:
                data=dataDict[self.device]['scopes']['0']['wave'][0]['wave']
                datay=data*rng/float(2**15)
                if plt.get_fignums() and self.updated==1:
                    self.line.set_ydata(datay)
                    plt.draw()
                else:
                    #create oscilloscope window
                    plt.figure()
                    plt.grid(True)
                    plt.title('Osciloscope data')
                    plt.xlabel('Time(us)')
                    plt.ylabel('Amplitude(V)')
                    
		    #plot first oscilloscope shot
                    dt=dataDict[self.device]['scopes']['0']['wave'][0]['dt']
                    datax=[x*1e6 for x in arange(0,dt*2048,dt)]
                    plt.axis([0,datax[-1],-2*rng,2*rng])
                    self.line, = plt.plot(datax,datay)
                    self.updated=1


if __name__ == '__main__':

    # Open connection to ziServer
    daq = zhinst.ziPython.ziDAQServer('localhost', 8005)

    # Detect device
    device = zhinst.utils.autoDetect()

    #set channels parameters
    channel_settings = [
        [['/', device, '/sigins/0/diff'], 0],
        [['/', device, '/sigins/0/imp50'], 0],
        [['/', device, '/sigins/0/ac'], 0],
        [['/', device, '/sigins/0/range'], 1],

        [['/', device, '/sigins/1/diff'], 0],
        [['/', device, '/sigins/1/imp50'], 0],
        [['/', device, '/sigins/1/ac'], 0],
        [['/', device, '/sigins/1/range'], 1],

        [['/', device, '/oscs/0/freq'], 100e3],
        [['/', device, '/oscs/1/freq'], 100e3+1],

        [['/', device, '/sigouts/0/add'], 1],
        [['/', device, '/sigouts/0/on'], 1],
        [['/', device, '/sigouts/0/range'], 1],
        [['/', device, '/sigouts/0/amplitudes/6'],0.5],

        [['/', device, '/sigouts/1/add'], 0],
        [['/', device, '/sigouts/1/on'], 1],
        [['/', device, '/sigouts/1/range'],1],
        [['/', device, '/sigouts/1/amplitudes/7'],0.5],
        ]
    daq.set(channel_settings)
    time.sleep(1)

    #select lock-in channel
    channel=1

    #create object Oscilloscope
    a=Oscilloscope(device,daq,channel)

    #set parameters for the scope
    a.set_parameters(bwlimit=0,trigedge=1,triglevel=0,trigholdoff=0.01,trigchannel=-2,t=1)

    # Subscribe to scope data
    path0 = '/' + device + '/scopes/0/wave'
    daq.subscribe(path0)

    #N is number of oscilloscope shots
    N=random.randint(50,100)

    i=0
    while i<N:
        a.update()
        i=i+1
    
    # Unsubscribe     
    daq.unsubscribe(path0)	
    print 'Done!'