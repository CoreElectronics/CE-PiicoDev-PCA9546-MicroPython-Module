from PiicoDev_MUX import PiicoDev_MUX
from PiicoDev_Potentiometer import PiicoDev_Potentiometer
from PiicoDev_Unified import sleep_ms


mux = PiicoDev_MUX()

mux.channel = 0
pot_A = PiicoDev_Potentiometer()

mux.channel = 1
pot_B = PiicoDev_Potentiometer()

while True:
    mux.channel = 0
    a = pot_A.value
    
    mux.channel = [1,2,3]
    b = pot_B.value
    
    print(a,b)
    sleep_ms(100)