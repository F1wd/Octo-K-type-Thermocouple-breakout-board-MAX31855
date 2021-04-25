
#neem tech supporting libary MAX31855
import MAX31855#

#Help is a wrapper class I wrote to help troubleshooting clarification.
import HELP#

from time import sleep

MAX31855
HELP

"My Argon v2 case blocks the SPI0 pins so.. wish peope would make hats that get along :K..."

"so I used SPI1 on a raspberry PI 4"
"you will need to add this line to your boot config.txt if you plan on using these pins"
"this will also set your CE or CS pin to GPIO pin 16"
"dtparam=spi1-1cs,cs0_pin=16"


"""as well as connecting the GPIO/BCM pins noted below, again GPIO notation"
"MAX31855# driver uses GPIO.setmode(GPIO.BCM)<-gpio notation
if you try and use (GPIO.BOARD)<-pin notation Things get really fun:C so try and stick
with .BCM notation throught your project.
"""
"GPIO PINS"
"def __init__(self, SCK, CS, SO, T0, T1, T2):"
"def __init__(self,  21, 16, 19,  5,  6, 13):"


"were gonna call all these functions supported in the MAX31855 driver"
"after that I made a less documented loop to loop through all the sensors calling each function"
"note i convert the First temp reading to F in each of these function call sets"


"Make THERMY"
THERMY = MAX31855.MAX31855(21, 16, 19, 5, 6, 13)

"param therm_id: id of the thermocouple (0 - 7)"
THERMY.read_data(0)

"Gets the temperature of the reference junction from"
"the most recent poll."
":returns: float representing the temperature in celsius"
TEMPY = THERMY.get_reference_temp()
"HELP.c2f(TEMPY)<- converts DEG C to DEF F possibly not the most accurate conversion but.."
print(HELP.c2f(TEMPY)," DEG F")

"""
Gets the temperature of the most recently polled
thermocouple.
:returns: float representing the temperature in celsius
"""
TEMPY = THERMY.get_thermocouple_temp()
print(TEMPY," DEG C")


print("SELF DIAGNOSTIC",HELP.DRT(THERMY))

"""
Returns the value of latest_data
:returns: the value of latest_data
"""
TEMPY = THERMY.get_latest_data()
print(TEMPY," DEG C")

X=0
while X < 8:
    sleep(.1)
    print("sensor ",X)
    THERMY.read_data(X)
    sleep(.1)
    TEMPY = THERMY.get_reference_temp()
    print(HELP.c2f(TEMPY)," DEG F")
    TEMPY = THERMY.get_thermocouple_temp()
    print(TEMPY," DEG C")
    TEMPY = THERMY.get_latest_data()
    print(TEMPY," DEG C")
    print(THERMY.get_faults())
    print("SELF DIAGNOSTIC",HELP.DRT(THERMY))
    X=X+1
    print("___________________________________________________________")
    print()
    
    
THERMY.cleanup()