MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Display menu for temperature conversation"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            convert_celsius_fahrenheit()
        elif choice == "F":
            convert_fahrenheit_celsius()

        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you")

def convert_fahrenheit_celsius():
    """Convert fahrenheit to celsius"""
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f}C")

def convert_celsius_fahrenheit():
    """Convert celsius to fahrenheit"""
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")

main()