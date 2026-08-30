# This program is a fucntion that calculates Resistance

def calculate_resistance(voltage, current):
    """
args: voltage(float): voltage across a component in volts (V)
      current(float): current throught a component in amperes (A)
return: it returns the calculated value of resistance in ohm (Ω)

Note:  the function raises a Zero division error if current = 0
"""
    return voltage / current

assert calculate_resistance(9, 0.03) == 300
assert calculate_resistance(24, 2) == 12
print(calculate_resistance.__doc__)

def calc_power(voltage, resistance):
    """
    args: voltage(float): voltage across a component in volts (V)
          resistance(float): resistance throught a component in (Ω)
    return: it returns the calculated value of power in Watt (W)
    
    Note:  the function raises a Zero division error if current = 0
    """
    current = voltage / resistance

    return voltage * current

print(calc_power.__doc__)

