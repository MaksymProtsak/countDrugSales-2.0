def updateDefoltRowDataFileJson(rowObjectList, fileToWriteDefoltRowData):
    # print("updateDefoltRowDataFileJson: START")
    from app.getListFromJson import getListFromJson
    from app.writeFileJson import writeFileJson
    fileToEditDefoltRowData = getListFromJson(fileToWriteDefoltRowData)
    # Write Row status to the file
    for i in range(len(rowObjectList)):
        fileToEditDefoltRowData[i]["Препарат"] = rowObjectList[i].variableOfRegion.get(
        )
        fileToEditDefoltRowData[i]['План команди']['Ціна уп.'] = rowObjectList[i].mainDrugPriceVar.get(
        )
        fileToEditDefoltRowData[i]['План команди']['Гроші'] = rowObjectList[i].mainMoneyPlanVar.get(
        )
        fileToEditDefoltRowData[i]['Місяць № 1']['Ціна уп.'] = rowObjectList[i].Month1DrugPriceVar.get(
        )
        fileToEditDefoltRowData[i]['Місяць № 1']['Гроші'] = rowObjectList[i].Month1MoneyPalnVar.get(
        )
        fileToEditDefoltRowData[i]['Місяць № 1']['Факт Упак'] = rowObjectList[i].Month1PacksVar.get(
        )
        fileToEditDefoltRowData[i]['Місяць № 2']['Ціна уп.'] = rowObjectList[i].Month2DrugPriceVar.get(
        )
        fileToEditDefoltRowData[i]['Місяць № 2']['Гроші'] = rowObjectList[i].Month2MoneyPalnVar.get(
        )
        fileToEditDefoltRowData[i]['Місяць № 2']['Факт Упак'] = rowObjectList[i].Month2PacksVar.get(
        )
        fileToEditDefoltRowData[i]['Місяць № 3']['Ціна уп.'] = rowObjectList[i].Month3DrugPriceVar.get(
        )
        fileToEditDefoltRowData[i]['Місяць № 3']['Гроші'] = rowObjectList[i].Month3MoneyPalnVar.get(
        )
        fileToEditDefoltRowData[i]['Місяць № 3']['Факт Упак'] = rowObjectList[i].Month3PacksVar.get(
        )

    writeFileJson(fileToEditDefoltRowData, fileToWriteDefoltRowData)
    # print("updateDefoltRowDataFileJson: FINISH")
