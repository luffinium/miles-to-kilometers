def convertToKilometers (unitList, unitScale):
    if unitScale == "mi":
        unitList[0] = (unitList[0] / 0.62137) 
    return unitList
