# Perform a scan to detect devices connected to the PiicoDev MUX
from PiicoDev_MUX import PiicoDev_MUX

mux = PiicoDev_MUX(asw=[0,0,0]) # Initialise the MUX, option to set the Address Switches (ASW)

# Scan all channels for connected devices
all_devices = mux.scan()

print("Found the following devices connected to the PiicoDev MUX at address {}".format(mux.address))
for channel in range(mux.number_of_channels):
    devices = all_devices[channel]
    print("    Ch{}: {}".format(channel, devices))
