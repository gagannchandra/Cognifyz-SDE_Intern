# -------------------------------------------
# Program: Temperature Converter
# Author: Gagan Chandra (Original Work)
# Level: Intermediate
# Objective: Convert temperature between Celsius and Fahrenheit
# -------------------------------------------

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9


def temperature_converter():
    """Main function to handle user input and conversion flow."""
    print("🌡️ Welcome to the Temperature Converter!\n")

    while True:
        print("Choose conversion direction:")
        print("1. Celsius ➜ Fahrenheit")
        print("2. Fahrenheit ➜ Celsius")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            try:
                c = float(input("Enter temperature in Celsius: "))
                f = celsius_to_fahrenheit(c)
                print(f"✅ {c}°C = {round(f, 2)}°F\n")
            except ValueError:
                print("⚠️ Please enter a valid number.\n")

        elif choice == "2":
            try:
                f = float(input("Enter temperature in Fahrenheit: "))
                c = fahrenheit_to_celsius(f)
                print(f"✅ {f}°F = {round(c, 2)}°C\n")
            except ValueError:
                print("⚠️ Please enter a valid number.\n")

        elif choice == "3":
            print("👋 Exiting Temperature Converter. Stay cool!")
            break

        else:
            print("⚠️ Invalid choice. Please select 1, 2, or 3.\n")


# Run the program
if __name__ == "__main__":
    temperature_converter()
