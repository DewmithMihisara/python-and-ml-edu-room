print("Yard to meter converter")

isContinued = True

while isContinued:
    print("\na. Yard to meter converter")
    print("b. Meter to yard converter\n")

    x = input("Enter the Option : ")

    if( x == "a"):
        value = input("Input the value to convert : ")
        value_in_meters = float(value) * 0.9144
        print(f"{value} yards is equivalent to {value_in_meters} meters.\n")

    elif( x == "b"):
        value = input("Input the value to convert : ")
        value_in_yards = float(value) * 1.0936
        print(f"{value} meters is equivalent to {value_in_yards} yards.\n")

    else:
        print("Invalid conversion type. Please enter 'a' or 'b'.\n")

    isContinued = input("Do you want to convert another value? (y/n): ")