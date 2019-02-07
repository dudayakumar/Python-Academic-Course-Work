#Program to troubleshoot diesel engine
#Programmed by Dhivya Udaya Kumar

print("Welcome to diesel engine troubleshoot programming")
print("\n")

while True:
    #Check for status lights
    lightColor = input("Check status lights - Select among the following options \n 1. Red \n 2. Amber \n 3. Green \n ")

    #Logic for "Red" status
    if lightColor == "1" or lightColor.lower() == "red":
        print("Shut off all input lines \n Check meter #3")
        while True:
            try:
                meterReading = int(input("Enter the meter reading: "))
                assert(meterReading > 0), 'Number must be greater than 0'
                break
            except:
                print("Please enter a valid number")

        #Meter reading check
        if meterReading < 50:
            print("Check main line for test pressure.")
            while True:
                pressure = input("Does it indicate a pressure that is- \n 1. Normal \n 2. High \n 3. Low \n")
                #Pressure-check
                if pressure == "1" or pressure == "2" or pressure == "3" or pressure.lower() == "high" or pressure.lower() == "low" or pressure.lower() == "normal":
                    break
                else:
                    print("Please enter a valid input")

            if pressure == "1" or pressure.lower() == "normal":
                print("Refer to motor service manual")
            elif pressure == "2" or pressure == "3" or pressure.lower() == "high" or pressure.lower() == "low":
                print("Refer to main line manual")

        else:
            while True:
                #Velocity check
                velocity = input("Measure flow velocity at inlet 2-B. Is the velocity- \n 1. Normal \n 2. High \n 3. Low \n")
                if velocity == "1" or velocity == "2" or velocity == "3" or velocity.lower() == "normal" or velocity.lower() == "high" or velocity.lower() == "low":
                    break
                else:
                    print("Please enter a valid input")

            if velocity == "1" or velocity.lower() == "normal":
                print("Refer to inlet service manual")
            else:
                print("Refer unit for factory service")
        break

    #Logic for "Amber" status
    elif lightColor == "2" or lightColor.lower() == "amber":
        print("Check fuel line service routine")
        break

    #Logic for "Green" status
    elif lightColor == "3" or lightColor.lower() == "green":
        print("Do restart procedure")
        break
    else:
        print("Please enter a valid input")

print("Programmed by Dhivya Udaya Kumar")