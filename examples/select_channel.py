# A simple example to show how to select different channel configurations with the PiicoDev MUX
from PiicoDev_MUX import PiicoDev_MUX
from PiicoDev_Unified import sleep_ms

mux = PiicoDev_MUX(asw=[0,0,0]) # Initialise the MUX, option to set the Address Switches (ASW)

# Scan all channels for connected devices
devices = mux.scan()
print(devices)

# You can select single channels
mux.channel = 0
# ... now interact with devices on channel 0 here

# Or select multiple channels simultaneously
mux.channel = [1,3]
# ... now interact with devices on channels 1 and 3 here

# disable all channels. This is the default state.
mux.channel = []
