from ohms_law import calculate_resistance
from ohms_law import calc_power

results = calculate_resistance(24, 3)
print("Resistance = ",results, "Ω")
print(calculate_resistance.__doc__)

 
results_P = calc_power(12, results)
results_P2 = calc_power(15, results)
print("Power = ",results_P, "W")
print("Power = ",results_P2, "W")