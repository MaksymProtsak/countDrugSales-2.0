def createListFor_use_table_in_data(tableInDataList):
    # print("createListFor_use_table_in_data: START")
    listForUpdate = []
    for listObject in tableInDataList:
        listForUpdate.append({"fileName": listObject.rowName,
                              "dateCreated": listObject.dateCreated,
                              "status": listObject.var.get()})
    # print("createListFor_use_table_in_data: FINISH")
    return listForUpdate
