# This program is a fucntion that calculates Resistance

def calculate_resistance(voltage, current):
    """
args: voltage(float): voltage across a component in volts (V)
      current(float): current throught a component in amperes (A)
return: it returns the calculated value of resistance in ohm (Ω)

Note:  the function raises a Zero division error if current = 0
"""
    return voltage / current

