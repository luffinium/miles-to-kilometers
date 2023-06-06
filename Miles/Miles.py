def convertToMiles (unitList, unitScale):
    if unitScale == "km":
        unitList[0] = (unitList[0] * 0.62137) 
    return unitList
