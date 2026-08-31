from unit_converter import mm_to_inches, inches_to_mm
from unit_converter import cm_to_inches, inches_to_cm

direction = input("Enter conversion (mm_to_in or in_to_mm): ")

value = float(input("Enter the measurement: "))

if direction == "mm_to_in":
    results = mm_to_inches(value)
    print("Converted value:", round(results,2), "inches")

elif direction == "in_to_mm":
    results = inches_to_mm(value)
    print("Converted value:",round(results,2), "mm")

else: 
    print("Invalid conversion option")

print(mm_to_inches.__doc__)
print(inches_to_mm.__doc__)

direction2 = input("Enter conversion (cm_to_in or in_to_cm): ")

value2 = float(input("Enter the measurement"))

if direction2 == "cm_to_in":
    results2 = cm_to_inches(value2)
    print("Converted value:",results2, "inches")

elif direction2 == "in_to_cm":
    results2 = inches_to_cm(value2)
    print("Converted value:",results2, "cm")

else:  
    print("Invalid option")

print(cm_to_inches.__doc__)
print(inches_to_cm.__doc__)
