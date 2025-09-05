print("welcome to Fahrenheit 404")
choice = input("do you want to convert:\nto C(enter 'F') or C to F (enter 'C')?")
if choice == "F":
    F = float(input("enter temperture in Fahrenheit:")) 
    c = (F - 32) * 5/9
    print(F"{F}°F is {c:.2f}°C")
elif choice == "C":
    c = float(input("Enter temperature in Celcius: ")) 
    f = (c * 9/5) + 32
    print(f"{c}°C is {f:.2f}°F")   
else:
    print("invalid choice. please enter 'F' or 'C' ")    

conversion = input(input(("Convert F to C or C to F? (Enter 'F' or 'C'): ").strip().upper()))
if conversion == "F":
    fahrenheit = float(input("enter temperature in fahrenheit: "))
    celcius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is {celcius:.2}°C")
elif conversion == "C":
    celcius = float(input("enter tempurture in celcius: "))
    fahrenheit = (celcius * 9/5) + 32
    print(f"{celcius}°C is {fahrenheit:.2f}°C")
else:
    print("invalid input, please enter 'F' or 'C' for conversion")
