from ohms_law import calculate_resistance
from unit_converter import mm_to_inches, inches_to_mm
from unit_converter import cm_to_inches, inches_to_cm

DEFAULT_CURRENT = 0.5
print("Global value:", DEFAULT_CURRENT)

def show_default():
        DEFAULT_CURRENT = 1.0
        print("Inside function:", DEFAULT_CURRENT)

def display_menu():
    """
    Prints a numbered menu of engineering calculations.

    The menu includes:
        1. calculated resistance (ohm's laws)
        2. Convert length (mm to inches and inches to mm)
        3. Convert length (cm to inches and inches to cm)
        4. Exit
    """
    print("\n--- Engineering Calculator Menu---" )
    print("1. calculate resistance (ohm's laws)")
    print("2. Convert length (mm to inches and inches to mm)")  
    print("3. Convert length (cm to inches and inches to cm)")  
    print("3. Exit")  

def main():
    running = True
   
    show_default(), print("Outside function:", DEFAULT_CURRENT)

    while running:
        display_menu()

        choice = input("Select an option: ")

        if choice == "1":
            voltage = float(input("Enter voltage (V): "))
            current_input = (input("Enter current (A)or press enter for default: "))

            if current_input == "":
                current = DEFAULT_CURRENT
            else:
                current = float(current_input)

            try:
                    resistance = calculate_resistance(voltage, current)
                    print("Resistance = ", resistance, "Ω")
            except ZeroDivisionError: 
                 print("Error: Current cannot be zero")

        elif choice == "2":
            direction = input("Enter conversion (mm_to_in or in_to_mm): ")
            value = float(input("Enter measurement: "))

            if direction == "mm_to_in":
                results = mm_to_inches(value)
                print("Converted value:", round(results,2), "inches")

            elif direction == "in_to_mm":
                results = inches_to_mm(value)
                print("Converted value:",round(results,2), "mm")

            else: 
                print("Invalid conversion option")

        elif choice == "3":
             direction2 = input("Enter conversion (cm_to_in or in_to_cm): ")
             value2 = float(input("Enter the measurement: "))

             if direction2 == "cm_to_in":
                 results2 = cm_to_inches(value2)
                 print("Converted value:",round(results2,3), "inches")

             elif direction2 == "in_to_cm":
                 results2 = inches_to_cm(value2)
                 print("Converted value:",round(results2,3), "inches")

             else:  print("Invalid option")


        
        elif choice == "4":
            running = False
            print("Program closed")

        else:
            print("Invalid menu option")

        print(calculate_resistance.__doc__)
        print(mm_to_inches.__doc__)

if __name__ == "__main__":
    main()

