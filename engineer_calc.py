from ohms_law import calculate_resistance
from unit_converter import mm_to_inches, inches_to_mm

def display_menu():
    """
    Prints a numbered menu of engineering calculations.

    The menu includes:
        1. calculated resistance (ohm's laws)
        2. Convert length (mm to inches and inches to mm)
        3. Exit
    """
    print("\n--- Engineering Calculator Menu---" )
    print("1. calculated resistance (ohm's laws)")
    print("2. Convert length (mm to inches and inches to mm)")    
    print("3. Exit")  

def main():
    running = True

    while running:
        display_menu()

        choice = input("Select an option: ")

        if choice == "1":
            voltage = float(input("Enter voltage (V): "))
            current = float(input("Enter current (A): "))

            resistance = calculate_resistance(voltage, current)
            print("Resistance = ", resistance, "Ω")

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
            running = False
            print("Program closed")

        else:
            print("Invalid menu option")

        print(calculate_resistance.__doc__)
        print(mm_to_inches.__doc__)

if __name__ == "__main__":
    main()