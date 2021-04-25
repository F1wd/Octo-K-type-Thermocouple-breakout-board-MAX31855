"import MAX31855#"
"""
Returns a value signififying a particular fault in the most
recent poll.

0 indicates that no faults exist
1 indicates an SCV fault (thermocouple is shorted to VCC)
2 indicates an SCG fault (thermocouple is shorted to GND)
3 indicates an OC fault (the thermocouple is not connected)

:returns: an integer representing the fault

DR.TEMP AKA DRT returns 1 for :D a no fault scnerio and 0 for some issue :(
"""
def DRT(self):
    issue=0
    issue=self.get_faults()
    if issue == 0:
        return 1
    if issue == 1:
        print("thermocouple is shorted to VCC")
        return 0
    if issue == 2:
        print("thermocouple is shorted to GND")
        return 0
    if issue == 3:
        print("the thermocouple is not connected")
        return 0
    print("this wasnt supposed to be able to happen something went wrong with selfdiagnostic")
    return 0
"converts deg c to deg f"
def c2f(temp):
    temp=temp*1.8+32
    return temp