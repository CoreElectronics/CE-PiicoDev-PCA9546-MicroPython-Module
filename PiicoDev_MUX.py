# A simple class to drive the Core Electronics PiicoDev MUX PCA9546
# Michael Ruppe at Core Electronics

from PiicoDev_Unified import *

compat_str = '\nUnified PiicoDev library out of date.  Get the latest module: https://piico.dev/unified \n'

_BASE_ADDRESS = 0x70

def _set_bit(byte, bit_number, value):
    """Sets a bit in a byte to the desired value."""
    if value:
        byte |= (1 << bit_number)
    else:
        byte &= ~(1 << bit_number)
    return byte

class PiicoDev_MUX(object):
    def __init__(self, bus=None, freq=None, sda=None, scl=None, address=_BASE_ADDRESS, asw=None):
        try:
            if compat_ind >= 1:
                pass
            else:
                print(compat_str)
        except:
            print(compat_str)
            
        if type(asw) is list: # preference using the ASW argument
            assert all(x in [0,1] for x in asw) and len(asw) is 3, "asw must be a list of 0 or 1, length=4"
            self._address= _BASE_ADDRESS + 1*asw[0] + 2*asw[1]
        else: self._address = address    
        self.i2c = create_unified_i2c(bus=bus, freq=freq, sda=sda, scl=scl)
        self._channel = []
        self._num_channels = 4
        
    @property
    def channel(self):
        """Returns the list of enabled channels"""
        return sorted(self._channel)
    
    @channel.setter
    def channel(self, channels):
        """Enable channel(s). Accepts an Int or list of Ints. An empty list or None will disable all channels"""
        byte = 0 # default all channels off
        if type(channels) is int: channels = [channels]
        channels = list(set(channels)) # remove duplicates
        assert all(x in [0,1,2,3] for x in channels) and len(channels) <= 4, ".channel must be an integer or list of integers 0->3"
        self._channel=[]
        for chan in channels:
            byte = _set_bit(byte, chan, 1) # set each desired channel bit to 1
            self._channel.append(chan)
        self.i2c.write8(self._address, None, bytes([byte]))
        
    def disable(self):
        """Disable all channels"""
        self.channel = []
    
    def scan(self):
        """Perform a (separate) I2C scan on all ports"""
        temp = self.channel
        devices = []
        for channel in range(self._num_channels):
            self.channel = channel
            dev = self.i2c.i2c.scan()
            dev.remove(self._address)
            devices.append( dev )
#         print("Found the following devices under MUX at address {}".format(self._address))
#         for channel in range(self._num_channels):
#             print("ch{}: {}".format(channel, devices[channel]))
        self.channel = temp
        return devices

