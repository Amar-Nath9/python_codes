def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print("Select operation.")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

while True:
    choice = input("Enter choice (1/2): ")

    if choice in ('1', '2'):
        try:
            temperature = float(input("Enter temperature: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(f"{temperature}°C is {celsius_to_fahrenheit(temperature)}°F")

        elif choice == '2':
            print(f"{temperature}°F is {fahrenheit_to_celsius(temperature)}°C")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() == "no":
            break

    else:
        print("Invalid Input")
    
