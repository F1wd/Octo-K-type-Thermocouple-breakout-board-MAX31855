# Octo-K-type-Thermocouple-breakout-board-MAX31855
Octo K-type Thermocouple breakout board MAX31855 Review

You could accomplish the same thing with 3 mortys and a jumper cable.

Appears to function as advertized 

For my set up 
  using a raspberry pi 4
  spi1-cs1 as my argon one v2 case blocks spi0
    Add these lines to your boot/config.txt
      >>> dtparam=spi1-1cs,cs0_pin=16 
      >>> dtparam=maxtherm,spi1-1cs,max31855
  
  use the following Pin out for my setup
  "GPIO PINS NOTATION" 
"def __init__(self, SCK, CS, SO, T0, T1, T2):"
"def __init__(self,  21, 16, 19,  5,  6, 13):"
      
     NOTE: The MAX31855 libary uses 
      >>>GPIO.setmode(GPIO.BCM)
If you plan on using anyother supporting libarys for other gpio pins things make sure you are using GPIO.BCM and not GPIO.BOARD,. LITTLE PI gets confused.
