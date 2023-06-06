from Miles import convertToMiles
from Kilometers import convertToKilometers
X = True 
while X is True:

    unit = float(input("Enter the number of the measurement.:"))
    while True:
        unitScale = input("Enter two letters to indicate the measurement scale (mi or km).: ")
        if unitScale == "mi" or unitScale =="km":
            break
        
    if unitScale == "mi":
        convertedDistance = convertToKilometers(unit)
    elif unitScale == "km":
        convertedDistance = convertToMiles(unit)

    print ("You entered ", unit, unitScale)
    
    if unitScale == "km":
        print ("The measurement in miles is ",convertedDistance)
    elif unitScale == "mi":
        print ("The measurement in kilometers is ",convertedDistance)
    conTinue = input("Press X to quit or enter to continue processing.")
    if conTinue.upper() == ("X"):
        X = False
        print("End processing of distances.")