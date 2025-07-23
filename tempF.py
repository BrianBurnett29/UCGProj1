# Displays the degrees and the equations
def celsius_to_fahrenheit(celsius):
  #Converts Celsius to Fahrenheit. This is the Celcius to Fahrenhiet formula: (0°C × 9/5) + 32 = 32°F
  return (celsius * 9/5) + 32

# Converts Fahrenheit to Celsius. This is the Fahrenhiet to Celcius formula: (32°F − 32) × 5/9 = 0°C
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5/9

# A conventional way to organize the primary logic of a script. Main function to handle user interaction and calculations.
def main(): 
  print("Temperature Conversion Tool")

# Gives you a choice selection to choose from
  while True: 
    print("\nChoose an operation:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Quit")

# Print to show choice numbers
    choice = input("Enter your choice (1/2/3): ")

# If choice functions determine what happens when entering specific information
    if choice == "1":
      try:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
      except ValueError:
        print("Invalid input. Please enter a number.")
    elif choice == "2":
      try:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
      except ValueError:
        print("Invalid input. Please enter a number.")
    elif choice == "3":
      print("Exiting the program.")
      break
    else:
      print("_" * 30)
      print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
  main()