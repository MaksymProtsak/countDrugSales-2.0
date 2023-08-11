def generateHtmlTable(sumDrugObjectList, regionObjectList, totalSumDrugObjectList, updateGuiInfo):
    print("generateHtmlTable: START")

    tableDict = {}
    tableDict["Препарат"] = []
    tableDict["Команда"] = []
    # Get name current True regions
    for keyTableHead in regionObjectList:
        # Append region in dictForHtmlFrame
        if keyTableHead.var.get() == True:
            tableDict[keyTableHead.name] = []

    # Set regions position False
    for keyTableHead in regionObjectList:
        keyTableHead.var.set(False)

    # Fill file html_table_data
    for keyTableHead in sumDrugObjectList:
        tableDict["Препарат"].append(keyTableHead.rowName.capitalize())
        tableDict["Команда"].append(
            str(keyTableHead.rowTotalPercentVar.get())+" %")

    # Fill percent in region list
    for regionName in tableDict:
        for checkButtonObject in regionObjectList:
            if checkButtonObject.name == regionName:
                checkButtonObject.var.set(True)
                updateGuiInfo()

                # Get percent from drugSumRow, and append to dictionary
                for sumDrugObject in sumDrugObjectList:
                    tableDict[regionName].append(
                        sumDrugObject.rowTotalPercentVar.get()+" %")

                    # Set regions position False
                    for keyTableHead in regionObjectList:
                        keyTableHead.var.set(False)

    # print(tableDict)

    # Return checkbutton postionon before start method
    for regionKey in tableDict:
        for checkbuttonObject in regionObjectList:
            if checkbuttonObject.name == regionKey:
                checkbuttonObject.var.set(True)

    # Update after return position of checkbuttons
    updateGuiInfo()

    # Append total sum percent
    for i, keyTableHead in enumerate(tableDict):
        if i == 0:
            tableDict["Препарат"].append('Разом')
        elif i == 1:
            tableDict["Команда"].append(
                totalSumDrugObjectList[0].mainPercent.get()+" %")

    # Set regions position False
    for keyTableHead in regionObjectList:
        keyTableHead.var.set(False)

    # Append total region percent
    for key in tableDict:
        updateGuiInfo()
        for checkButtonObject in regionObjectList:
            if checkButtonObject.name == key:
                checkButtonObject.var.set(True)
                updateGuiInfo()
                percent = totalSumDrugObjectList[0].mainPercent.get()+" %"
                tableDict[key].append(percent)
                checkButtonObject.var.set(False)
                updateGuiInfo()

    # Return checkbutton postionon before start method
    for regionKey in tableDict:
        for checkbuttonObject in regionObjectList:
            if checkbuttonObject.name == regionKey:
                checkbuttonObject.var.set(True)

    # Update after return position of checkbuttons
    updateGuiInfo()

    # Create one region name
    oneWordRegionNameList = {}
    for key in tableDict:
        if key == "Препарат" or key == "Команда":
            pass
        else:
            regionNameOneWord = None
            if key == "АР КРИМ":
                regionNameOneWord = "АР Крим"
                oneWordRegionNameList[key] = regionNameOneWord
            elif key == "ІВАНО-ФРАНКІВСЬКА ОБЛАСТЬ":
                regionNameOneWord = "Івано-Франківська"
                oneWordRegionNameList[key] = regionNameOneWord
            else:
                regionNameOneWord = key.split()
                oneWordRegionNameList[key] = regionNameOneWord[0].capitalize()
    # Append column with one word region name
    for regionName in oneWordRegionNameList:
        if regionName in tableDict:
            oneWordName = oneWordRegionNameList[regionName]
            dataForOneWordName = tableDict[regionName]
            tableDict[oneWordName] = dataForOneWordName

    # Pop two words region name in tableDict
    for regionName in oneWordRegionNameList:
        tableDict.pop(regionName)

    # print(tableDict)
    print("generateHtmlTable: FINISH")
    return tableDict
