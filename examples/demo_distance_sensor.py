from PiicoDev_MUX import PiicoDev_MUX
from PiicoDev_VL53L1X import PiicoDev_VL53L1X
from PiicoDev_Unified import sleep_ms


mux = PiicoDev_MUX()

mux.channel = 0
sensor_A = PiicoDev_VL53L1X()
mux.channel = 1
sensor_B = PiicoDev_VL53L1X()
mux.channel = 2
sensor_C = PiicoDev_VL53L1X()
mux.channel = 3
sensor_D = PiicoDev_VL53L1X()


while True:
    mux.channel = 0
    distance_A = sensor_A.read()
    mux.channel = 1
    distance_B = sensor_A.read()
    mux.channel = 2
    distance_C = sensor_A.read()
    mux.channel = 3
    distance_D = sensor_A.read()
    print(f'{distance_A:.0f} {distance_B:.0f} {distance_C:.0f} {distance_D:.0f}')
    sleep_ms(100)
