from unit_converter import mm_to_inches, inches_to_mm

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

